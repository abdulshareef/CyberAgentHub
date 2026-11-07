# License check log

Append-only record of license checks done after the initial listing. Entries here take precedence over `data/agents.json` until it is regenerated.

Status key: `project-stated` = the project's own README/docs say so; `third-party` = only index/aggregator sites report it; `verified-on-repo` = LICENSE read on the repo page.

| Date | Tool | Result | Status | Evidence / caveats |
|---|---|---|---|---|
| 2026-11-07 | PentestGPT | MIT | project-stated | README states MIT (LICENSE.md); repository metadata on a third-party index also reports `mit`. Labelled a research prototype. |
| 2026-11-07 | HexStrike AI | MIT | project-stated | README states MIT; a 2025 write-up said no LICENSE file was present then, so confirm the file exists before redistribution. Community forks exist and the author runs a companion commercial platform. |
| 2026-11-07 | CAI (Cybersecurity AI) | MIT + proprietary (mixed, not a standard OSI license) | project-stated | The project's own archived README shows an "MIT + Proprietary" badge; GitHub metadata reports `other`. Repo is confirmed archived by the project itself (unmaintained attack tooling; evolved into a commercial product). Read the LICENSE file before any reuse. |
| 2026-11-07 | Buttercup (Trail of Bits) | AGPL-3.0 | third-party | Reported by two aggregator sites (AlternativeTo, GitTrend). Trail of Bits' announcement confirms the system was open-sourced in Aug 2025 and also released the AIxCC semifinal/final versions. Confirm LICENSE on repo. AGPL is strong copyleft. |
