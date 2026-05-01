# CLAUDE.md

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
