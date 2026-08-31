# AGENTS.md

## Board and matrix ordering

Entries in **The board** table and the **Capabilities matrix** share the same row order (same position numbers).

### Sort rules
1. **Primary: score descending.** Higher score = higher position.
2. **Tie-breaking within the same score: insertion order.** Ties are *not* re-sorted by star count — entries keep the order they were added.

### Updating a score
When a new feature raises an entry's score:
- Determine which score tier it now belongs to.
- Place it at the *end* of that tier (last among ties), consistent with insertion-order tie-breaking.
- If the new position number happens to be the same as the old one (e.g., the entry was already adjacent to the tier above), no row reordering is needed — just update the score and feature cells.
- Update both the board table and the capabilities matrix to stay in sync.

## Board data freshness

The board's ⭐, **Last push**, and License cells are mechanical snapshots; the feature cells and Score are the manual, audited part.

- ⭐ / Last push / License: refresh with `python3 scripts/refresh-board-data.py` (`--dry-run` first). A daily GitHub Action (`.github/workflows/refresh-board-data.yml`) runs the same script and commits the diff. Never touch feature cells or row order here.
- Feature cells / Score: only change through a re-audit of the project's README/docs/source (clone under `refs/<name>/` for grep checks). After re-auditing a row, append `YYYY-MM-DD — <Project>.` to the **Re-audits** list in the Methodology section. Sort rules above still apply if the score changes.
- Blank matrix cells and blank Last push cells mean "not observed", not "no".
- Full feature re-audits (READMEs → feature cells → re-rank): use the `reaudit-board` skill (`.opencode/skills/reaudit-board/`) and `scripts/apply-board-audit.py`.
