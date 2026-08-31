#!/usr/bin/env python3
"""Refresh the mechanical cells of The board in readme.md.

For every row, fetch stars / last push / license via `gh api repos/<owner>/<repo>`
and update the ⭐, Last push, and License cells. Feature cells, scores, and row
order are never touched. Requires the gh CLI. Use --dry-run to preview changes.
"""

import argparse
import json
import re
import subprocess
import sys

README = "readme.md"
BOARD_HEADING = "### The board"
NEXT_HEADING = "### Capabilities matrix"

OLD_HEADER = ["#", "Project", "⭐", "Stack", "Platforms", "License", "Distribution", "Score", "Headline traits"]
NEW_HEADER = ["#", "Project", "⭐", "Last push", "Stack", "Platforms", "License", "Distribution", "Score", "Headline traits"]
NEW_SEP = "|---:|---|---:|---:|---|---|---|---|---|---|"

FIELD_LABELS = {2: "⭐", 3: "Last push", 6: "License"}
REPO_RE = re.compile(r"github\.com/([\w.-]+/[\w.-]+)")
SKIP_LICENSES = {"NOASSERTION", "OTHER"}


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def join_row(cells):
    return "| " + " | ".join(cells) + " |"


def row_name(project_cell):
    return re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", project_cell)


def fetch_repo(repo):
    proc = subprocess.run(["gh", "api", f"repos/{repo}"], capture_output=True, text=True)
    if proc.returncode != 0:
        detail = proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else "unknown error"
        print(f"  ! {repo}: gh api failed: {detail}", file=sys.stderr)
        return None
    data = json.loads(proc.stdout)
    return {
        "stars": data.get("stargazers_count"),
        "pushed": (data.get("pushed_at") or "")[:10],
        "license": (data.get("license") or {}).get("spdx_id"),
    }


def refresh_row(cells, dry_run):
    match = REPO_RE.search(cells[1])
    if not match:
        print(f"  ! {row_name(cells[1])}: no GitHub repo link, skipped")
        return False
    repo = match.group(1).removesuffix(".git")
    data = fetch_repo(repo)
    if data is None:
        return False
    changes = []
    for idx, label in FIELD_LABELS.items():
        value = {"⭐": str(data["stars"]) if data["stars"] is not None else None,
                 "Last push": data["pushed"] or None,
                 "License": data["license"] if data["license"] and data["license"] not in SKIP_LICENSES else None}[label]
        if value is not None and value != cells[idx]:
            changes.append(f"{label} {cells[idx] or '—'} → {value}")
            if not dry_run:
                cells[idx] = value
    if changes:
        print(f"  {row_name(cells[1])}: {'; '.join(changes)}")
    return bool(changes)


def main():
    ap = argparse.ArgumentParser(description="Refresh stars, last push, and license cells in The board.")
    ap.add_argument("--dry-run", action="store_true", help="print changes without writing readme.md")
    ap.add_argument("--strict", action="store_true", help="exit non-zero if any repo fetch fails")
    args = ap.parse_args()

    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.splitlines()
    try:
        start = lines.index(BOARD_HEADING)
        end = lines.index(NEXT_HEADING, start)
    except ValueError:
        sys.exit(f"could not find {BOARD_HEADING!r} / {NEXT_HEADING!r} in {README}")

    out = lines[:start + 1]
    header_seen = sep_seen = False
    changed = failures = 0

    for line in lines[start + 1:end]:
        if not line.startswith("|"):
            out.append(line)
            continue
        cells = split_row(line)
        if not header_seen and cells in (OLD_HEADER, NEW_HEADER):
            out.append(join_row(NEW_HEADER))
            header_seen = True
        elif not sep_seen and header_seen and all(c.startswith("---") for c in cells):
            out.append(NEW_SEP)
            sep_seen = True
        elif header_seen and sep_seen and cells and cells[0].isdigit():
            if len(cells) == len(OLD_HEADER):
                cells.insert(3, "")
            if len(cells) != len(NEW_HEADER):
                sys.exit(f"unexpected row width ({len(cells)} cells): {cells[:3]}")
            if refresh_row(cells, args.dry_run):
                changed += 1
            out.append(join_row(cells))
        else:
            out.append(line)

    if header_seen != sep_seen:
        sys.exit("board header/separator upgrade did not apply cleanly")

    if args.dry_run:
        print(f"dry run: {changed} row(s) would change, {failures} fetch failure(s)")
        if failures and args.strict:
            sys.exit(f"{failures} repo fetch(es) failed")
        return

    new_text = "\n".join(out + lines[end:])
    if text.endswith("\n"):
        new_text += "\n"
    if new_text != text:
        with open(README, "w", encoding="utf-8") as fh:
            fh.write(new_text)
    print(f"done: {changed} row(s) updated, {failures} fetch failure(s)")
    if failures and args.strict:
        sys.exit(f"{failures} repo fetch(es) failed")


if __name__ == "__main__":
    main()
