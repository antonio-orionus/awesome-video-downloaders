---
name: reaudit-board
description: Re-audit Awesome Video Downloaders comparison rows against upstream READMEs — spawn parallel per-repo audit subagents, apply feature additions with scripts/apply-board-audit.py, re-rank board/matrix. Use when re-auditing entries, checking if repos gained features, or refreshing the feature comparison (NOT for star/last-push refreshes — use scripts/refresh-board-data.py for that).
---

# Re-audit the board

Re-checks the feature comparison (top N rows) against each project's README, applies
feature-cell additions, re-scores, and re-ranks. Mechanical data (⭐, Last push, License)
is NOT part of this — the daily CI refreshes it.

## Workflow

### 1. Fresh mechanical data first

```bash
python3 scripts/refresh-board-data.py
```

### 2. Extract current status per row

```bash
python3 scripts/apply-board-audit.py status --top 20
```

This prints each row's currently credited features — the audit agents need this list.

### 3. Spawn one parallel subagent per repo

Use the `general` subagent type, one task per repo, all in a single message. Skip rows
audited within the last few weeks (check the **Re-audits** list in the Methodology
section). The prompt template — fill in `<OWNER/REPO>`, `<NAME>`, and `<CURRENT STATUS>`:

```text
RESEARCH ONLY — do not write or edit any files. You are verifying a feature-comparison
table entry for the GitHub project <OWNER/REPO> ("<NAME>").

1. Fetch the root README: try https://raw.githubusercontent.com/<OWNER/REPO>/HEAD/README.md
   first; if that fails try https://github.com/<OWNER/REPO> (repo page renders README).
   If both fail, reply "FETCH FAILED" and stop.
2. Judge ONLY what the README (badges, tables, feature lists included) clearly documents.
   Roadmap/planned/TODO items do NOT count.

FEATURES:
1. YouTube (explicit YouTube support) · 2. 1000+ sites (claims 1000+/1800+/2000+ sites or
"hundreds of sites" — quote exact wording) · 3. Torrents · 4. Music services (dedicated
Spotify/Tidal/Qobuz/Deezer/Apple Music — YouTube Music alone does NOT count, note it
separately) · 5. Galleries (image galleries/boards, gallery-dl style) · 6. Courses
(Udemy/Hotmart/Teachable) · 7. Multi-engine (a second download engine: aria2,
gallery-dl, spotDL — not just yt-dlp) · 8. Audio-only (MP3/M4A/Opus extraction) ·
9. Format picker (choose quality/format before download) · 10. HDR (explicit HDR
support) · 11. Trim (cut segment by start/end time) · 12. Playlists · 13. URL list
(paste multiple URLs/batch) · 14. Concurrent downloads (configurable parallel queue) ·
15. Skip downloaded (archive/skip-already-downloaded tracking) · 16. Speed limit
(bandwidth cap) · 17. SponsorBlock · 18. Metadata embed · 19. Thumbnail embed ·
20. Auto-retry (automatic retry of failures) · 21. Resume on restart (resume unfinished
download after app restart) · 22. Convert / transcode (re-encode/compress after
download) · 23. Filename templates (custom naming with variables) · 24. Subtitles Save
separate (sidecar file) · 25. Subtitles Embed in container (mkv/mp4) · 26. Subtitle
Format choice (SRT/VTT/ASS) · 27. Subtitle Post-edit (beyond save: merge, burn-in,
translation, generation like Whisper) · 28. Cookies from browser · 29. cookies.txt file ·
30. Proxy · 31. Custom args (user-supplied extra yt-dlp arguments) · 32. Cookie-free
anti-bot (PO tokens/bgutil-like, no login) · 33. Browser extension · 34. Clipboard watch
(monitor clipboard for URLs) · 35. Channel / RSS auto (auto-download new videos from
channels/RSS) · 36. Scheduler (timed downloads) · 37. System tray (minimize to
tray/background) · 38. Global hotkey · 39. Auto-update yt-dlp (app keeps yt-dlp current
by itself) · 40. Plugin system (install third-party app plugins)

CURRENT TABLE STATUS (✅ already credited): <CURRENT STATUS>

YOUR JOB: find (a) ADD candidates — README-documented features missing from the status;
(b) FLAGS — current ✅ items the README explicitly contradicts. Silence about an existing
✅ is NOT a flag; ignore it.

OUTPUT: one line per noteworthy finding: `- <Feature name>: ADD|FLAG — "<short quote>"`.
Then one line per distinctive feature the 40 columns do NOT cover (feeds future column
candidates): `- UNIQUE: <feature> — "<short quote>"`. Keep UNIQUE honest — only features
a comparison shopper would care about, not generic polish (themes, languages counts).
Final line exactly: `SUMMARY: ADD=<names or none>; FLAG=<names or none>; UNIQUE=<count>`
```

### 4. Verify before applying

- Re-check every agent ADD against the CURRENT TABLE STATUS you passed in — agents
  sometimes re-propose features the table already credits.
- Independently fetch the README yourself for any repo gaining more than 2 features or
  entering the top 3, and confirm the quotes. Apply judgment calls consistently:
  CLI-only companion features don't count for the desktop app; a tray *notification*
  is not System tray; library/player integration with Spotify et al. is not Music
  services (downloading from them is); a JS-runtime dependency note is not Cookie-free
  anti-bot unless it documents a user-facing mechanism.

### 5. Apply

Write a JSON file `{"owner/repo": ["Feature", ...]}` and run:

```bash
python3 scripts/apply-board-audit.py apply adds.json --dry-run   # review ranking first
python3 scripts/apply-board-audit.py apply adds.json
python3 scripts/apply-board-audit.py verify
```

The script re-scores, re-ranks (score descending, ties keep current order), and keeps
board/matrix rows aligned.

### 6. Hand-edit the prose the script cannot know

- **Methodology → Re-audits**: append `YYYY-MM-DD — <Project>` for each row audited.
- **Pick by use case**: update lines affected by new features (e.g. channel auto-download).
- **Headline traits** in the board for rows whose story changed materially.
- **List description bullets** for big movers.

### 7. Verify and commit

```bash
python3 scripts/apply-board-audit.py verify
```

Then commit (user-facing commit message describing the audit results, not "update").
