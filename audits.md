# Feature audits

Every change to the feature cells of [the board and capabilities matrix](readme.md#comparison-at-a-glance), newest first. The rules each audit applies are in the [Methodology](readme.md#methodology) section.

**Depth** says what an audit read:

- **Source**: the README, docs and the cloned source at the given commit.
- **README**: the README only. It misses features the README doesn't mention, so these rows can score lower than they would after a source audit.
- **First compile**: the original 2026-05-01 compile from README, docs and source; depth wasn't recorded per row.

## Latest audit per row

In board order.

| Project | Last audit | Depth |
|---|---|---|
| omniget | 2026-11-25 | Source (`9b9072d`) |
| youwee | 2026-11-25 | Source (`5fed7ac`) |
| GDownloader | 2026-11-25 | Source (`9021cbf`) |
| Arroxy | 2026-11-25 | Source (`6df64a0`) |
| yt-dlp-gui (imsyy) | 2026-11-25 | Source (`e3cd1df`) |
| comine | 2026-11-25 | Source (`eddb61a`) |
| bili-downloader | 2026-11-25 | Source (`4206b45`) |
| neodlp | 2026-11-25 | Source (`7a2d2db`) |
| Parabolic | 2026-11-25 | Source (`1118e6a`) |
| YTSage | 2026-11-25 | Source (`f4c1510`) |
| ytget-gui | 2026-08-31 | README |
| ytDownloader | 2026-08-31 | README |
| varia | 2026-08-31 | README |
| Pulsar | 2026-08-31 | README |
| streamfetch | 2026-08-31 | README |
| mediaharbor | 2026-08-31 | README |
| vibedownloader-desktop | 2026-08-31 | README |
| cosmo-downloader | 2026-08-31 | README |
| avrix-downloader | 2026-08-31 | README |
| yt-channel-downloader | 2026-08-31 | README |
| yt-grabber | 2026-05-01 | First compile |
| YouStealD | 2026-05-01 | First compile |
| arcdlp | 2026-05-01 | First compile |
| ytdlp-gui (aliencaocao) | 2026-05-01 | First compile |
| media-downloader | 2026-05-01 | First compile |
| Sunder | 2026-05-01 | First compile |
| YouTube-Downloader | 2026-05-01 | First compile |
| FastDownloader | 2026-05-01 | First compile |
| pytube-downloader | 2026-05-01 | First compile |
| VidGrabber | 2026-05-01 | First compile |
| YT-Forge | 2026-05-01 | First compile |
| MusicYT-Downloader | 2026-05-01 | First compile |
| ezytdl | 2026-05-01 | First compile |
| VidDownloader | 2026-05-01 | First compile |

## Log

| Date | Project | Depth | Changes |
|---|---|---|---|
| 2026-11-25 | All rows | Source (top 10, arcdlp) | New column **In-app browser** (Authentication): browse the site signed in inside the app and download from the pages you open. Credited: Arroxy (Explore tab). Added with one project, an exception to the two-project rule. Checked and not credited: the sign-in windows of arcdlp, omniget and bili-downloader close once you're signed in; no other top-10 row opens a window for outside sites. Rows 11–34 stay blank until re-audited. Arroxy 29 → 30. |
| 2026-11-25 | omniget | Source (`9b9072d`) | ADD Multi-engine (gallery-dl, librqbit torrents, direct aria2), Concurrent downloads, Scheduler, Cookies from browser, cookies.txt, In-app sign-in (login window, first-party Courses plugin), Proxy, Custom args (editable per-download yt-dlp command), System tray. REMOVE Embed in container: the README says "embedded or sidecar", but the app never passes `--embed-subs`. 30 → 38. |
| 2026-11-25 | youwee | Source (`5fed7ac`) | Second pass over the cells not checked for #17. REMOVE Cookie-free anti-bot: no PO-token or bgutil code; only a Deno runtime and player-client options. Not credited: Resume on restart (the saved queue comes back, but downloads start again from zero). 33 → 32. |
| 2026-11-25 | GDownloader | Source (`9021cbf`) | ADD Concurrent downloads, Skip downloaded (archive and history), Metadata embed, Filename templates (yt-dlp name patterns), Save separate, Format choice, Cookie-free anti-bot (bundled bgutil PO-token provider). Not credited: Global hotkey (a Ctrl+C listener only feeds Clipboard watch). 23 → 30. |
| 2026-11-25 | Arroxy | Source (`6df64a0`) | No change; all 29 cells confirmed. |
| 2026-11-25 | yt-dlp-gui (imsyy) | Source (`e3cd1df`) | ADD URL list (Batch tab), Custom args, System tray, Plugin system (imports third-party yt-dlp plugins). Cookie-free anti-bot kept: a PO token and visitor_data setting. 23 → 27. |
| 2026-11-25 | comine | Source (`eddb61a`) | ADD Trim, Concurrent downloads, SponsorBlock, Metadata embed, Auto-retry, Resume on restart, Convert / transcode, Filename templates, Cookies from browser, cookies.txt (pasted Netscape cookies), Browser extension (developer's own), Auto-update yt-dlp. REMOVE Cookie-free anti-bot: only JavaScript runtimes. Not credited: Custom args (yt-dlp args settings are never used; only aria2 args reach a download). 16 → 27. |
| 2026-11-25 | bili-downloader | Source (`4206b45`) | ADD YouTube (v0.20.1 added YouTube downloads through yt-dlp), SponsorBlock, Auto-update yt-dlp, cookies.txt (pasted cookies.txt content). 21 → 25. |
| 2026-11-25 | neodlp | Source (`7a2d2db`) | ADD HDR (format picker labels HDR10), Trim, Concurrent downloads, Convert / transcode (always re-encode option), Filename templates, System tray, Auto-update yt-dlp. REMOVE Multi-engine: aria2 only as yt-dlp's external downloader. Not credited: Auto-retry (only yt-dlp's `--retries` count). 18 → 24. |
| 2026-11-25 | Parabolic | Source (`1118e6a`) | ADD SponsorBlock, Speed limit, Convert / transcode, cookies.txt, Proxy, Custom args, Auto-update yt-dlp. REMOVE Post-edit: only format conversion and de-duplicating YouTube auto-captions. Not credited: Filename templates (two fixed toggles). 17 → 23. |
| 2026-11-25 | YTSage | Source (`f4c1510`) | ADD Format choice. REMOVE Concurrent downloads (the queue runs one at a time; the setting is fragments per download), Post-edit (the README says burned-in subtitles, but the code only soft-embeds), Cookie-free anti-bot (only a Deno installer). 22 → 20. |
| 2026-11-25 | youwee | Source (`5fed7ac`) | [#17](https://github.com/antonio-orionus/awesome-video-downloaders/issues/17): ADD Galleries, Multi-engine (gallery-dl Gallery page), Concurrent downloads, Skip downloaded (Library-history duplicate check; gallery-dl archive), Convert / transcode (Processing page, which needs an AI provider; official Media Converter plugin), Filename templates (picked metadata fields), Custom args (allowlisted yt-dlp options), Scheduler, Auto-update yt-dlp (checks on launch, updates on one click). 24 → 33. |
| 2026-11-18 | bili-downloader | Source (v0.18.0) | New row. Not credited: Courses (Bilibili's paid courses are a content type of the one site it covers, not a course platform) and Convert / transcode (streams are copied; it re-encodes only to remove watermarks). |
| 2026-10-18 | Arroxy | Not recorded | ADD Trim (v0.6.0 "Download just part of a video", start/end or chapter, via `--download-sections`), In-app sign-in (Explore tab sign-in for private and members-only videos). |
| 2026-10-18 | arcdlp | Not recorded | New column **In-app sign-in**: log in to the site inside the app's own browser window instead of exporting cookies. Credited: Arroxy, arcdlp ("built-in browser login window"). Other rows stay blank until re-audited against it. |
| 2026-09-05 | Arroxy | Not recorded | ADD Global hotkey. |
| 2026-08-31 | Top 20 rows: Arroxy, youwee, GDownloader, yt-dlp-gui (imsyy), neodlp, Parabolic, YTSage, comine, ytget-gui, ytDownloader, varia, Aither-Download-Manager, streamfetch, mediaharbor, Pulsar, omniget, cosmo-downloader, vibedownloader-desktop, avrix-downloader, yt-channel-downloader | README | Re-audit against READMEs; the matrix grew to 40 columns. |
| 2026-05-01 | All rows | First compile | Feature data compiled from each project's README, docs and source. |
