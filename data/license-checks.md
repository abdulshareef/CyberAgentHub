# License check log

Append-only record of license checks done after the initial listing. Entries here take precedence over `data/agents.json` until it is regenerated.

| Date | Tool | Result | Status | Evidence |
|---|---|---|---|---|
| 2026-11-07 | PentestGPT | MIT | project-stated | README states MIT (LICENSE.md); repository metadata on a third-party index also reports `mit`. Repo is labelled a research prototype. |
| 2026-11-07 | HexStrike AI | MIT | project-stated | README states MIT; a 2025 write-up said no LICENSE file was present then, so confirm the file exists before redistribution. Community forks exist (e.g. a Polish fork by netcuter) and the author runs a companion commercial platform. |
