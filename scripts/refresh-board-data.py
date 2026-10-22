#!/usr/bin/env python3
"""Refresh the mechanical cells of The board in readme.md.

For every row, fetch stars / last push / license via `gh api repos/<owner>/<repo>`
and update the ⭐ and Pushed cells and the license in the Project cell's <sub> line
(`stack · license · ...`). Feature cells, scores, and row order are never touched. Requires the gh CLI. Use --dry-run to preview changes.
"""

import argparse
import json
import re
import subprocess
import sys

README = "readme.md"
BOARD_HEADING = "### The board"
NEXT_HEADING = "### Capabilities matrix"

HEADER = ["#", "Project", "⭐", "Pushed", "Score", "Stands out for"]

REPO_RE = re.compile(r"github\.com/([\w.-]+/[\w.-]+)")
SUB_RE = re.compile(r"<sub>(.*?)</sub>")
SKIP_LICENSES = {"NOASSERTION", "OTHER"}


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def join_row(cells):
    return "| " + " | ".join(cells) + " |"


def row_name(project_cell):
    return re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", project_cell.split("<br>")[0])


def format_stars(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def get_license(project_cell):
    m = SUB_RE.search(project_cell)
    parts = m.group(1).split(" · ") if m else []
    return parts[1] if len(parts) > 1 else None


def set_license(project_cell, value):
    m = SUB_RE.search(project_cell)
    parts = m.group(1).split(" · ")
    parts[1] = value
    return project_cell[:m.start(1)] + " · ".join(parts) + project_cell[m.end(1):]


def fetch_repo(repo):
    proc = subprocess.run(["gh", "api", f"repos/{repo}"], capture_output=True, text=True)
    if proc.returncode != 0:
        detail = proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else "unknown error"
        print(f"  ! {repo}: gh api failed: {detail}", file=sys.stderr)
        return None
    data = json.loads(proc.stdout)
    return {
        "stars": data.get("stargazers_count"),
        # YYYY‑MM with a non-breaking hyphen (U+2011) so the narrow cell never wraps
        "pushed": (data.get("pushed_at") or "")[:7].replace("-", "\u2011"),
        "license": (data.get("license") or {}).get("spdx_id"),
    }


def refresh_row(cells, dry_run):
    """Return (changed, fetch_failed)."""
    match = REPO_RE.search(cells[1])
    if not match:
        print(f"  ! {row_name(cells[1])}: no GitHub repo link, skipped")
        return False, False
    repo = match.group(1).removesuffix(".git")
    data = fetch_repo(repo)
    if data is None:
        return False, True
    license_ = data["license"] if data["license"] not in SKIP_LICENSES else None
    if license_ and get_license(cells[1]) is None:
        sys.exit(f"{row_name(cells[1])}: Project cell has no `<sub>stack · license</sub>` line")
    changes = []

    def update(label, old, new):
        if new is not None and new != old:
            changes.append(f"{label} {old or '—'} → {new}")
            return not dry_run
        return False

    stars = format_stars(data["stars"]) if data["stars"] is not None else None
    if update("⭐", cells[2], stars):
        cells[2] = stars
    if update("Pushed", cells[3], data["pushed"] or None):
        cells[3] = data["pushed"]
    if update("License", get_license(cells[1]), license_):
        cells[1] = set_license(cells[1], license_)
    if changes:
        print(f"  {row_name(cells[1])}: {'; '.join(changes)}")
    return bool(changes), False


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
    header_seen = False
    changed = failures = 0

    for line in lines[start + 1:end]:
        cells = split_row(line) if line.startswith("|") else []
        if cells == HEADER:
            header_seen = True
        elif header_seen and cells and cells[0].isdigit():
            if len(cells) != len(HEADER):
                sys.exit(f"unexpected row width ({len(cells)} cells): {cells[:3]}")
            row_changed, row_failed = refresh_row(cells, args.dry_run)
            changed += row_changed
            failures += row_failed
            line = join_row(cells)
        out.append(line)

    if not header_seen:
        sys.exit(f"board header {join_row(HEADER)!r} not found")

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
