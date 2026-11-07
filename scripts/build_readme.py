#!/usr/bin/env python3
"""Regenerate README.md listing tables from data/agents.json."""
import json, collections, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
agents = json.loads((root / "data" / "agents.json").read_text())

BADGE = {
    "verified-on-repo": "Verified",
    "project-stated": "Project-stated",
    "unverified": "Unverified",
}
ORDER = ["Pentest & Red Team", "SOC & Threat Hunting", "Digital Forensics & IR",
         "Malware & Reverse Engineering", "MCP Servers & Skills",
         "Vulnerability Research", "Securing AI Agents"]

def esc(s): return s.replace("|", "\\|")

def lic(a):
    if a['license_status'] == 'unverified' and a['license'] == 'Unverified':
        return 'Not yet checked'
    return f"{esc(a['license'])} ({BADGE[a['license_status']]})"

def row(a):
    return (f"| [{esc(a['name'])}]({a['repo']}) | {esc(a['summary'])} | "
            f"{lic(a)} | "
            f"{esc(a['repo_state'])} |")

by_cat = collections.defaultdict(list)
for a in agents: by_cat[a["category"]].append(a)
newest = sorted(agents, key=lambda a: a["added"], reverse=True)[:10]
n_ver = sum(a["license_status"] == "verified-on-repo" for a in agents)

out = [f"""# CyberAgentHub

**A free, curated directory of agentic AI tools for cybersecurity, digital forensics and every sub-field.**

Agentic AI has made it easy to build security tools, and new ones appear weekly. CyberAgentHub tracks them in one place with a plain-language description, the license, and the project's current state, so you can find what is free to use and what the fine print says.

> **{len(agents)} entries** · {n_ver} with license read directly from the repository · everything else flagged until checked · last data update: {max(a['added'] for a in agents)}

## How to read the listings

| Label | Meaning |
|---|---|
| **Verified** | The license was read on the project's repository page by a curator. |
| **Project-stated** | The license is claimed in the project's own README/wiki but the LICENSE file was not independently checked yet. |
| **Unverified** | Listed from public research; license not yet checked. Check the repo before reuse. |

Listing is not endorsement. We do not host, audit or warrant any tool. Many tools here are dual-use: use them only on systems you own or have written permission to test.

## Newest additions
| Tool | What it does | License | State |
|---|---|---|---|
""" + "\n".join(row(a) for a in newest) + "\n"]

for cat in ORDER:
    if cat not in by_cat: continue
    out.append(f"\n## {cat}\n| Tool | What it does | License | State |\n|---|---|---|---|\n")
    out.append("\n".join(row(a) for a in sorted(by_cat[cat], key=lambda a: a['name'].lower())) + "\n")

out.append("""
## Licensing notes worth knowing
Some entries carry terms that matter for commercial or hosted use. See each entry's `notes` field in [`data/agents.json`](data/agents.json), for example copyleft licenses (AGPL-3.0), paid editions beside a free core, or extra EULA/NOTICE files.

## Submit your agent
Built a free agentic AI tool for security or forensics? [Open a submission](../../issues/new?template=submit-agent.yml). A maintainer reviews each one against [VERIFICATION.md](VERIFICATION.md) before it is listed. Newest releases are added at the top.

## Data and copyright
Descriptions are written by curators in their own words. Each tool remains the property of its authors under its own license; names and logos belong to their owners. Listing a tool does not grant any rights to it. Open an issue to correct or remove an entry.

The listing data is machine-readable in [`data/agents.json`](data/agents.json). Regenerate this page with `python3 scripts/build_readme.py`.
""")
(root / "README.md").write_text("".join(out))
print("README.md written,", len(agents), "entries")
