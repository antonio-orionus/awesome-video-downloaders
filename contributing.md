# Contribution Guidelines

Thanks for taking the time to contribute!

Please ensure your suggestion meets the inclusion criteria below before opening a pull request.

## Inclusion criteria

A project is eligible if **all** of the following are true:

- **User-facing app.** It has a graphical UI (desktop, mobile, browser extension, or web UI). Libraries, raw CLIs, and bare yt-dlp wrappers without a UI do not belong here.
- **Open source.** The source is publicly available under an OSI-approved license (or comparable). Closed-source apps are out of scope.
- **Actively maintained.** A commit, release, or issue response within the last 12 months. Archived or clearly abandoned projects will be removed.
- **Working release.** There is a downloadable build, package, or hosted instance that a user can actually run — not just source code with no setup path.
- **Genuine functionality.** The app must successfully download video or audio at the time of submission. AI-generated repos with no working binary, broken builds, or vapor projects will be rejected.
- **Not a duplicate.** It does something meaningfully different from existing entries (different platform, different focus, different UX). Yet another minimal yt-dlp GUI without a clear distinction will likely be rejected.
- **In scope.** Downloads video or audio from YouTube and/or other sites. Pure media players, format converters, and torrent clients are out of scope.
- **English-readable README.** The repo's README must be understandable in English (multilingual is fine).

## Adding an entry

1. Pick the right section: Cross-platform desktop GUIs, Windows-only desktop apps, Android apps, iOS and macOS apps, Browser extensions and userscripts, or Self-hosted.
2. Add the entry in this exact format:

   ```
   - [owner/name](https://github.com/owner/name) - Short description ending with a period.
   ```

3. Sort by relevance within the section — established, well-maintained projects toward the top; newer or less-polished entries lower.
4. Open a pull request. The title should be `Add owner/name`. The description should briefly explain why the project meets the criteria above.

## Description style

- One sentence is best. Two short sentences max.
- Sentence case. End with a period.
- No marketing language ("blazing fast", "next-generation", "premium", "🚀").
- No emojis at the start. The Awesome badge is the only decoration.
- Don't restate the section name (e.g. don't write "A cross-platform downloader for…" inside the cross-platform section).
- Mention what's distinctive: what platforms, what sites, what UX.

## Updating an entry

If a project is renamed, relocates, changes scope, or its description becomes inaccurate, open a PR to update it.

## Removing an entry

Open a PR with the reason in the body — archived, deleted, broken, out of scope, duplicate, etc. Maintainers may also remove entries that fall out of compliance during routine review.

## Self-promotion

You may submit your own project, but you must explicitly disclose the relationship in the PR description. Self-submissions are held to the same criteria as everything else.

## Code of conduct

By participating, you agree to abide by the project [Code of Conduct](code-of-conduct.md).
