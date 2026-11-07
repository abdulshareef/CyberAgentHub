# Verification checklist

An entry is listed as **Verified** only when a curator has done all of the following on the day recorded in `verified_on`:

1. Repository is public and the project is reachable (not a placeholder or empty repo).
2. A LICENSE file exists and its text matches the SPDX identifier recorded.
3. Any extra terms (EULA, NOTICE, commercial/enterprise edition, non-commercial clauses) are noted in `notes`.
4. The project is genuinely agentic (LLM or agent loop that plans and uses tools), not just a scanner with an AI label.
5. No obvious malware, credential harvesting or deceptive naming (for example, implying endorsement by a vendor). Install scripts were read, not just the README.
6. Maintainer identity is plausible (org/profile age, history). For submissions, the submitter confirms they are the author or have the author's permission.
7. Free-to-use is true for the listed edition. Paid-only tools are not listed; free cores of commercial products are listed with a note.

Status values: `verified-on-repo`, `project-stated`, `unverified`.
Repo state values: `active`, `active (early)`, `in development`, `archived`.
