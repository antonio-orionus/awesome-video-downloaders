#!/usr/bin/env python3
"""Apply feature-audit results to The board and the Capabilities matrix.

Subcommands:
  status          print each row's currently credited features (input for audit prompts)
  apply           apply feature additions from a JSON file, re-score, and re-rank
  verify          check board/matrix alignment, score math, and sort order

adds.json format: {"owner/repo": ["Feature name", ...], ...}
Run `apply --dry-run` first; rows are never reordered except by the score rules.
"""

import argparse
import json
import re
import sys

README = "readme.md"
GROUP_SIZES = [7, 9, 7, 4, 5, 8]
GROUP_NAMES = ["S", "D", "Q", "Su", "A", "Au"]
REPO_RE = re.compile(r"github\.com/([\w.-]+/[\w.-]+)")


def load():
    src = open(README, encoding="utf-8").read()
    cols = re.findall(r'<th align="center">([^<]+)</th>', src)
    expected_n = sum(GROUP_SIZES)
    assert len(cols) == expected_n, f"expected {expected_n} feature columns, got {len(cols)}"
    groups, offset = [], 0
    for size in GROUP_SIZES:
        groups.append(cols[offset:offset + size])
        offset += size
    return src, cols, groups


def matrix_rows(src):
    start = src.index('<tbody>') + len('<tbody>')
    end = src.index('</tbody>')
    rows = {}
    for line in [l for l in src[start:end].splitlines() if l.startswith('<tr><td>')]:
        repo = REPO_RE.search(line).group(1)
        cells = re.findall(r'<td align="center">(.*?)</td>', line)
        assert len(cells) == sum(GROUP_SIZES), (repo, len(cells))
        rows[repo] = cells
    return rows


def board_rows(src):
    board = src.split('### The board')[1].split('### Capabilities matrix')[0]
    rows = {}
    for line in [l for l in board.splitlines() if re.match(r'\| \d+ \|', l)]:
        parts = [p.strip() for p in line.strip().strip('|').split('|')]
        rows[REPO_RE.search(parts[1]).group(1)] = parts
    return rows


def counts_for(cells, cols, groups):
    counts = [sum(1 for n in g if cells[cols.index(n)] == '✅') for g in groups]
    return sum(counts), counts


def breakdown(counts):
    return " ".join(f"{n}{c}" for n, c in zip(GROUP_NAMES, counts))


def cmd_status(args):
    src, cols, groups = load()
    brows = board_rows(src)
    mrows = matrix_rows(src)
    order = sorted(brows, key=lambda r: int(brows[r][0]))[:args.top]
    for repo in order:
        name = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', brows[repo][1])
        yes = [n for n in cols if mrows[repo][cols.index(n)] == '✅']
        total, _ = counts_for(mrows[repo], cols, groups)
        print(f"{brows[repo][0]:>2}. {name} ({repo}) [{total}]: {', '.join(yes) if yes else '(none)'}")



def cmd_apply(args):
    src, cols, groups = load()
    adds = json.load(open(args.file, encoding="utf-8"))
    mrows = matrix_rows(src)
    brows = board_rows(src)

    for repo, feats in adds.items():
        if repo not in mrows:
            sys.exit(f"unknown repo in adds file: {repo}")
        for feat in feats:
            if feat not in cols:
                sys.exit(f"unknown feature {feat!r} for {repo} (valid: {', '.join(cols)})")
            if mrows[repo][cols.index(feat)] == '✅':
                sys.exit(f"{repo} already has {feat!r} credited — check the status output first")

    changed = []
    for repo, feats in adds.items():
        for feat in feats:
            mrows[repo][cols.index(feat)] = '✅'
        changed.append(repo)

    order = sorted(brows, key=lambda r: (-counts_for(mrows[r], cols, groups)[0], int(brows[r][0])))
    if args.dry_run:
        print("dry run — new ranking:")
        for i, repo in enumerate(order, 1):
            total, counts = counts_for(mrows[repo], cols, groups)
            mark = " *changed*" if repo in changed else ""
            name = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', brows[repo][1])
            print(f" {i:>2}. {total:>3}  {name:<24} {breakdown(counts)}{mark}")
        return

    lines_m = []
    lines_b = []
    for newpos, repo in enumerate(order, 1):
        total, counts = counts_for(mrows[repo], cols, groups)
        b = brows[repo][:]
        b[0] = str(newpos)
        b[8] = f"**{total}** · {breakdown(counts)}"
        lines_b.append("| " + " | ".join(b) + " |")
        name = re.search(r'>([^<]+)</a></td>', mlines_src(src, repo)).group(1)
        lines_m.append(f'<tr><td>{newpos}</td><td><a href="https://github.com/{repo}">{name}</a></td>' + ''.join(f'<td align="center">{c}</td>' for c in mrows[repo]) + '</tr>')

    start = src.index('<tbody>') + len('<tbody>')
    end = src.index('</tbody>')
    src = src[:start] + "\n" + "\n".join(lines_m) + "\n" + src[end:]

    board = src.split('### The board')[1].split('### Capabilities matrix')[0]
    out, i = [], 0
    for line in board.splitlines():
        if re.match(r'\| \d+ \|', line):
            out.append(lines_b[i]); i += 1
        else:
            out.append(line)
    assert i == len(brows)
    # splitlines()/join() drops board's trailing newline(s); re-attach them so the
    # heading stays on its own line (refresh-board-data.py needs it as its own line).
    gap = board[len("\n".join(board.splitlines())):]
    src = src.replace(board, "\n".join(out) + gap)
    open(README, "w", encoding="utf-8").write(src)
    print(f"applied {sum(len(v) for v in adds.values())} feature cell(s) across {len(adds)} repo(s); board re-ranked")


def mlines_src(src, repo):
    start = src.index('<tbody>')
    end = src.index('</tbody>')
    return next(l for l in src[start:end].splitlines() if l.startswith('<tr><td>') and f'/{repo}"' in l)


def cmd_verify(args):
    src, cols, groups = load()
    brows = board_rows(src)
    mrows = matrix_rows(src)
    problems = []
    if set(brows) != set(mrows):
        problems.append(f"board/matrix repo sets differ: {set(brows) ^ set(mrows)}")
    bpos = {r: int(brows[r][0]) for r in brows}
    mlines = {REPO_RE.search(l).group(1): l for l in src[src.index('<tbody>'):src.index('</tbody>')].splitlines() if l.startswith('<tr><td>')}
    for repo, bparts in brows.items():
        mpos = int(mlines[repo].split('</td>')[0].split('<td>')[1])
        if bpos[repo] != mpos:
            problems.append(f"{repo}: board position {bpos[repo]} != matrix {mpos}")
        total, counts = counts_for(mrows[repo], cols, groups)
        expected = f"**{total}** · {breakdown(counts)}"
        if bparts[8] != expected:
            problems.append(f"{repo}: score cell {bparts[8]!r} != {expected!r}")
    seq = [bpos[r] for r in sorted(brows, key=lambda r: int(brows[r][0]))]
    if seq != list(range(1, len(brows) + 1)):
        problems.append("positions are not 1..N")
    order = sorted(brows, key=lambda r: int(brows[r][0]))
    sscores = [counts_for(mrows[r], cols, groups)[0] for r in order]
    if sscores != sorted(sscores, reverse=True):
        problems.append("scores not in descending order")
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print(f"OK: {len(brows)} rows, positions aligned, scores match matrix cells, order descending")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("status", help="print current credited features per row")
    s.add_argument("--top", type=int, default=34, help="limit to first N rows")
    a = sub.add_parser("apply", help="apply additions from a JSON file and re-rank")
    a.add_argument("file", help="JSON file: {\"owner/repo\": [\"Feature\", ...]}")
    a.add_argument("--dry-run", action="store_true", help="show new ranking without writing")
    sub.add_parser("verify", help="check table integrity")
    args = ap.parse_args()
    {"status": cmd_status, "apply": cmd_apply, "verify": cmd_verify}[args.cmd](args)


if __name__ == "__main__":
    main()
