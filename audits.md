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
| omniget | 2026-11-26 | Source (`9e3c424`) |
| LibreGet | 2026-11-25 | Source (`9b9072d`) |
| youwee | 2026-11-25 | Source (`5fed7ac`) |
| GDownloader | 2026-11-25 | Source (`9021cbf`) |
| Arroxy | 2026-11-25 | Source (`6df64a0`) |
| comine | 2026-11-25 | Source (`eddb61a`) |
| VidBee | 2026-11-28 | Source (`587f0d0`) |
| yt-dlp-gui (imsyy) | 2026-11-25 | Source (`e3cd1df`) |
| bili-downloader | 2026-11-25 | Source (`4206b45`) |
| ytget-gui | 2026-11-25 | Source (`db2af48`) |
| neodlp | 2026-11-25 | Source (`7a2d2db`) |
| Parabolic | 2026-11-25 | Source (`1118e6a`) |
| ytDownloader | 2026-11-25 | Source (`b1696ca`) |
| YTSage | 2026-11-25 | Source (`f4c1510`) |
| mediaharbor | 2026-11-25 | Source (`6a02153`) |
| ezytdl | 2026-11-25 | Source (`3e12deb`) |
| Pulsar | 2026-11-25 | Source (`3197392`) |
| vibedownloader-desktop | 2026-11-25 | Source (`4620c9d`) |
| yt-grabber | 2026-11-25 | Source (`f7bf3a5`) |
| varia | 2026-11-25 | Source (`fcc91fe`) |
| streamfetch | 2026-11-25 | Source (`c2a82ea`) |
| media-downloader | 2026-11-25 | Source (`1e388f7`) |
| FastDownloader | 2026-11-25 | Source (`fec7981`) |
| arcdlp | 2026-11-25 | Source (`ee1b41f`) |
| YT-Forge | 2026-11-25 | Source (`4c3793d`) |
| yt-channel-downloader | 2026-11-25 | Source (`f682e60`) |
| cosmo-downloader | 2026-11-25 | Source (`ed09ef3`) |
| ytdlp-gui (aliencaocao) | 2026-11-25 | Source (`e26967f`) |
| pytube-downloader | 2026-11-25 | Source (`c501ed5`) |
| Sunder | 2026-11-25 | Source (`038efeb`) |
| YouTube-Downloader | 2026-11-25 | Source (`81dc908`) |
| avrix-downloader | 2026-11-25 | Source (`22ac3b7`) |
| VidGrabber | 2026-11-25 | Source (`24d8f8b`) |
| VidDownloader | 2026-11-25 | Source (`3003517`) |

## Log

| Date | Project | Depth | Changes |
|---|---|---|---|
| 2026-11-28 | VidBee | Source (`587f0d0`) | New row (nexmoe/VidBee, Electron, MIT, v2.5.0). Credited 29: YouTube, 1000+ sites; Audio-only, Format picker, Trim, Playlists, URL list, Concurrent downloads, Skip downloaded (a library check that reuses finished files still on disk); Metadata embed, Thumbnail embed, Auto-retry (its own queue backoff), Resume on restart (crash recovery resumes with `--continue`), Filename templates (four filename styles, plus a custom template per RSS subscription), AI summary (your own provider or VidBee Cloud); Convert / transcode, Embed chapters; Save separate, Embed in container, Post-edit (burned-in captions, local speech recognition, translation); Cookies from browser, cookies.txt, Proxy, Custom args; Browser extension (its own), Channel / RSS auto, System tray (`closeToTray` is on by default, with no setting in the UI), Auto-update yt-dlp, MCP server (51 tools on loopback with a token, on by default). Two rulings, now in the column table: **Convert / transcode** counts when the app's own AI agent starts the ffmpeg re-encode (it has no button and the README never mentions it; the agent runs on your own provider key or VidBee Cloud), and **Custom args** counts a setting that points the app to a yt-dlp config file. Not credited: Format choice (the UI exports SRT only; VTT exists only as a tool parameter of the agent and MCP), HDR, SponsorBlock, Speed limit, Hardware encoding (software x264/VP9 only), Split by chapters, Loudness (`loudnorm` appears only inside the voice-dubbing mix), Clipboard watch (the clipboard is read only when you open Add URL), Scheduler (the only timer is the 3 h feed check), Global hotkey, Plugin system (bundled agent packages and SKILL.md prompt files, not app or yt-dlp plugins), In-app sign-in and In-app browser (no login or browsing window), Cookie-free anti-bot (a player-client override and a Deno runtime), Torrents, Music services, Galleries, Courses, Multi-engine (yt-dlp is the only download engine). The board has 34 rows. |
| 2026-11-27 | All 33 rows | Source, five columns only (each row's clone at its latest commit) | New group **Processing**: **Convert / transcode** moves into it from Quality of life, beside four new columns, each checked in every row's source. **Hardware encoding**: omniget, LibreGet, GDownloader, comine, ytDownloader, ezytdl, Pulsar, vibedownloader-desktop. **Split by chapters**: omniget, LibreGet, youwee, Parabolic, ytget-gui, yt-grabber, arcdlp. **Embed chapters**: omniget, LibreGet, youwee, GDownloader, Arroxy, yt-dlp-gui (imsyy), comine, bili-downloader, neodlp, Parabolic, ytget-gui, ytDownloader, YTSage, mediaharbor, Pulsar, media-downloader, arcdlp. **Loudness**: omniget, LibreGet, ytget-gui, YTSage. Not credited: bili-downloader's hardware encoders (watermark removal only), YT-Forge (a comment about VideoToolbox, no hardware encoding), old Arroxy's split by chapters (in its yt-dlp bridge, but nothing in the UI turns it on), mediaharbor's ReplayGain (its player reads the tags; nothing writes them), ezytdl's chapters (`--add-metadata` only when it has no FFmpeg of its own). |
| 2026-11-27 | YouTube-Downloader | Source (`81dc908`) | ADD Convert / transcode: its Advanced Quality Settings window builds an `ffmpeg` re-encode with a codec (H.264, H.265, AV1, MPEG-4), CRF or bitrate, preset and tune (`main.py:618`). |
| 2026-11-27 | yt-channel-downloader | Source (`f682e60`) | ADD Convert / transcode: for a video format the user picks (MP4, WebM, AVI, MOV, MKV, FLV, 3GP) it copies the streams when they fit and re-encodes when they don't (`media_postprocessors.py`, `VideoContainerPP`). |
| 2026-11-27 | ytget-gui, mediaharbor | Source (`eb5242c`, `6a02153`) | ADD Format choice: each has a "Convert subtitles to SRT" setting, now in the column rule. bili-downloader and Sunder convert subtitles to one fixed format with no setting, so they stay blank. |
| 2026-11-26 | omniget | Source (`9e3c424`) | New row for the original, tonhowtf/omniget, back on GitHub since 2026-11-12 after its account suspension. Credited 42: the 40 of LibreGet's row plus Embed in container (the Manifest tracks tool passes `--embed-subs`) and In-app browser (Built-in Browser: headless Chrome streamed into the app window by default, downloads media sniffed from the pages you open). Courses come from first-party connectors (Hotmart, Udemy and others by tonhowtf) in the app's signed catalog. Not credited: Music services, Cookie-free anti-bot (the PO-token provider is an environment variable, with no setting). The board has 33 rows. |
| 2026-11-26 | LibreGet | — | Renamed from omniget: the row's repo, OpenSelena/omniget, is now OpenSelena/libreget, an independent fork. Features unchanged; checked against `b0a0f33` for the two columns the original gained: no `--embed-subs` and no embedded browser. |
| 2026-11-25 | YouStealD, MusicYT-Downloader | Source | Moved from the board to the Windows-only section: both release Windows installers and zips only and hardcode Windows binaries. The board has 32 rows. |
| 2026-11-25 | ezytdl | Source (`3e12deb`) | ADD Music services (Spotify links matched to YouTube audio, as spotDL does), Convert / transcode, Trim, Filename templates, Concurrent downloads, Metadata embed, Thumbnail embed, Format picker, HDR (format picker labels dynamic range), Playlists, URL list, Proxy, Custom args, Clipboard watch, System tray, Auto-update yt-dlp (notification with one-click update). Not credited: Browser extension and Cookies from browser (its extension handler looks unwired). 3 → 19. |
| 2026-11-25 | yt-grabber | Source (`f7bf3a5`) | ADD URL list, Concurrent downloads, Skip downloaded (folder check), Convert / transcode, Filename templates, Custom args, Cookie-free anti-bot (bundled bgutil plugin behind a setting), cookies.txt (loaded from its profile folder). Not credited: Auto-update yt-dlp (a button in Settings only). 8 → 16. |
| 2026-11-25 | YouStealD | Source (`64c3c75`) | ADD Cookies from browser, Channel / RSS auto (stream monitor), Skip downloaded (`--download-archive`), Auto-update yt-dlp (updates itself after a yt-dlp error), Convert / transcode (`--recode-video`). REMOVE System tray (no tray code). It ships Windows binaries only. 8 → 12. |
| 2026-11-25 | media-downloader | Source (`1e388f7`) | ADD Playlists, URL list, Auto-retry (its own second pass), Auto-update yt-dlp (at startup), Embed in container. 7 → 12. |
| 2026-11-25 | FastDownloader | Source (`fec7981`) | ADD Format picker, Concurrent downloads, Thumbnail embed, Auto-retry (its own retry loop), Auto-update yt-dlp. 6 → 11. |
| 2026-11-25 | arcdlp | Source (`ee1b41f`) | ADD Proxy, Metadata embed, Thumbnail embed. REMOVE Cookies from browser (cookies come only from its own login windows) and Cookie-free anti-bot (only a Deno runtime). Not credited: Auto-update yt-dlp (a button in Settings only). 8 → 9. |
| 2026-11-25 | YT-Forge | Source (`4c3793d`) | ADD 1000+ sites, Playlists, Convert / transcode (H.264 conversion), In-app sign-in, Cookie-free anti-bot (mints PO tokens itself), Auto-update yt-dlp. REMOVE Thumbnail embed (saved as a separate file). 4 → 9. |
| 2026-11-25 | ytdlp-gui (aliencaocao) | Source (`e26967f`) | No change; all 7 cells confirmed. |
| 2026-11-25 | pytube-downloader | Source (`c501ed5`) | ADD Concurrent downloads, Auto-retry. 5 → 7. |
| 2026-11-25 | MusicYT-Downloader | Source (`13835fc`) | ADD Playlists, Format picker, Convert / transcode (re-encodes to MP3 320k). It hardcodes Windows binaries. 4 → 7. |
| 2026-11-25 | Sunder | Source (`038efeb`) | ADD Cookies from browser, cookies.txt, Auto-update yt-dlp (one-click update offered when yt-dlp is outdated). REMOVE Auto-retry (the automatic retry is for playback only), Save separate (subtitles become lyrics and the file is deleted), System tray (closing quits the app), Global hotkey (in-window and media keys only). 7 → 6. |
| 2026-11-25 | YouTube-Downloader | Source (`81dc908`) | REMOVE Thumbnail embed (saved as a separate file), Resume on restart (pause and resume within a session only). 6 → 4. |
| 2026-11-25 | VidGrabber | Source (`24d8f8b`) | ADD Auto-update yt-dlp (at startup). REMOVE Thumbnail embed (saved as a separate file). 4 → 4. |
| 2026-11-25 | VidDownloader | Source (`3003517`) | ADD Convert / transcode (ffmpeg WebM to MP4 or MP3). 3 → 4. |
| 2026-11-25 | ytget-gui | Source (`db2af48`) | ADD Music services and Multi-engine (spotDL as its own downloader), Filename templates (per-site naming rules), URL list (import links from a text file), Custom args, Clipboard watch, Scheduler, System tray. REMOVE Cookie-free anti-bot: only a player-client override and a Deno runtime. 16 → 23. |
| 2026-11-25 | ytDownloader | Source (`b1696ca`) | ADD Filename templates, Concurrent downloads, URL list (batch mode), System tray, Global hotkey, cookies.txt, Auto-update yt-dlp, Format choice. REMOVE SponsorBlock: only a custom-args example, no setting of its own. 14 → 21. |
| 2026-11-25 | varia | Source (`fcc91fe`) | ADD Concurrent downloads, Resume on restart (saved state per download, resumed at startup). REMOVE Cookie-free anti-bot: only a Deno runtime. Cookies from browser kept: its own extension reads the browser's cookies. 14 → 15. |
| 2026-11-25 | Pulsar | Source (`3197392`) | ADD SponsorBlock, Concurrent downloads, Filename templates (title constructor), Auto-update yt-dlp (Pulsar-Bridge, its yt-dlp wrapper, updated at startup). 1000+ sites kept: it accepts any URL yt-dlp supports. 13 → 17. |
| 2026-11-25 | streamfetch | Source (`c2a82ea`) | ADD Auto-update yt-dlp. Resume on restart kept (Resume continues from the partial file); Auto-retry kept (the app re-queues failed jobs with a fallback strategy). 12 → 13. |
| 2026-11-25 | mediaharbor | Source (`6a02153`) | ADD cookies.txt, Filename templates, Custom args, Skip downloaded (library check), Cookie-free anti-bot (PO-token provider setting), In-app sign-in (Qobuz login window), Multi-engine (votify, gamdl, OrpheusDL). 12 → 19. |
| 2026-11-25 | vibedownloader-desktop | Source (`4620c9d`) | ADD cookies.txt, Browser extension (its own), Trim, Convert / transcode (built-in editor), Auto-update yt-dlp, Save separate, Format choice. REMOVE 1000+ sites: it accepts nine platforms only. Its lossless Spotify FLAC code is never used, so the board trait changed. 11 → 17. |
| 2026-11-25 | cosmo-downloader | Source (`ed09ef3`) | ADD Convert / transcode (ffmpeg re-encode with codec and bitrate). REMOVE Thumbnail embed (thumbnail saved as a separate file only), Resume on restart (restored jobs start again from zero), Cookie-free anti-bot (only a Deno runtime). 10 → 8. |
| 2026-11-25 | avrix-downloader | Source (`22ac3b7`) | REMOVE Playlists (`noplaylist` is always on), Metadata embed and Thumbnail embed (only audio extraction and a thumbnail file), URL list (one URL field), Resume on restart (the queue list only), System tray (no tray code). 10 → 4. |
| 2026-11-25 | yt-channel-downloader | Source (`f682e60`) | ADD Skip downloaded (skips files already in the download folder). REMOVE Courses (no course platforms), Thumbnail embed (thumbnail saved as a file only). 9 → 8. |
| 2026-11-25 | All rows | Source (top 10) | New columns **AI summary** (Quality of life: the app summarizes a video's content with an AI model in its own UI) and **MCP server** (Automation: exposes the app's features to AI agents over the Model Context Protocol). AI summary credited: youwee (AI summary page), omniget (Settings → AI video summaries). MCP server credited: omniget (Tools → AI → MCP server), bili-downloader (local MCP server). Not credited: bili-downloader's AI summary (Bilibili's own summary, passed to AI clients only over MCP); Arroxy's MCP server (behind the unreleased `agentControl` flag). Rows without a source audit stay blank until one covers them. omniget 38 → 40, youwee 32 → 33, bili-downloader 25 → 26. |
| 2026-11-25 | All rows | Source (top 10, arcdlp) | New column **In-app browser** (Authentication): browse the site signed in inside the app and download from the pages you open. Credited: Arroxy (Explore tab). Added with one project, an exception to the two-project rule. Checked and not credited: the sign-in windows of arcdlp, omniget and bili-downloader close once you're signed in; no other top-10 row opens a window for outside sites. Rows without a source audit stay blank until one covers them. Arroxy 29 → 30. |
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
