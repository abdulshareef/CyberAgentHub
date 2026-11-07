# CyberAgentHub

**A free, curated directory of agentic AI tools for cybersecurity, digital forensics and every sub-field.**

Agentic AI has made it easy to build security tools, and new ones appear weekly. CyberAgentHub tracks them in one place with a plain-language description, the license, and the project's current state, so you can find what is free to use and what the fine print says.

> **37 entries** · 5 with license read directly from the repository · everything else flagged until checked · last data update: 2026-11-07

## How to read the listings

| Label | Meaning |
|---|---|
| **Verified** | The license was read on the project's repository page by a curator. |
| **Project-stated** | The license is claimed in the project's own README/wiki but the LICENSE file was not independently checked yet. |
| **Unverified** | Listed from public research; license not yet checked. Check the repo before reuse. |

Listing is not endorsement. We do not host, audit or warrant any tool. Many tools here are dual-use: use them only on systems you own or have written permission to test.

## Pentest & Red Team
| Tool | What it does | License | State |
|---|---|---|---|
| [CAI (Cybersecurity AI)](https://github.com/aliasrobotics/cai) | Open framework for building cybersecurity agents with hierarchical multi-agent patterns, aimed at bug bounty and autonomous pentesting; basis of several research papers. | Not yet checked | archived (reported 2026-08-28) |
| [cochise](https://github.com/andreashappe/cochise) | Research agent for autonomous assumed-breach penetration testing of Active Directory networks (ACM TOSEM 2025). | Not yet checked | active |
| [ctf-agent (Veria Labs)](https://github.com/verialabs/ctf-agent) | Autonomous CTF-solving agent that runs several models in parallel; reported first place at the BSidesSF 2026 CTF. | Not yet checked | active |
| [hackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT) | Minimal research framework showing how little code is needed to have an LLM assist with ethical-hacking tasks such as Linux privilege escalation. | Not yet checked | active |
| [PentAGI](https://github.com/vxcontrol/pentagi) | Self-hosted fully autonomous multi-agent penetration-testing system (Go backend, web UI) that plans and runs security tools inside Docker. | MIT (Verified) | active |
| [Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) | Go-based autonomous pentest platform where agents coordinate through a shared blackboard; supports cloud and local models and exposes an MCP server. | Not yet checked | active |
| [PentestAgent (GHOSTCREW)](https://github.com/GH05TCREW/pentestagent) | Agent framework for black-box security testing covering bug bounty, red-team and pentest workflows; backed by an AsiaCCS 2025 paper. | Not yet checked | active |
| [PentestGPT](https://github.com/GreyDGL/PentestGPT) | Early, widely cited LLM-driven penetration-testing agent framework; accompanied by a USENIX Security 2024 paper. | Not yet checked | active |
| [Shannon](https://github.com/KeygraphHQ/shannon) | White-box AI pentester for web apps and APIs: reads source code, maps attack paths, then exploits the running app and reports only exploit-confirmed findings (PDF, Markdown, SARIF). | AGPL-3.0 (Verified) | active |
| [Strix](https://github.com/usestrix/strix) | Autonomous multi-agent AI pentester that runs targets dynamically in a sandbox, validates findings with working proofs-of-concept, and can scan in CI/CD. Open-source core with separate paid cloud and enterprise editions. | Apache-2.0 (Verified) | active |
| [VulnBot](https://github.com/KHenryAegis/VulnBot) | Multi-agent collaborative pentesting framework built around a penetration task graph; academic project. | Not yet checked | active |

## SOC & Threat Hunting
| Tool | What it does | License | State |
|---|---|---|---|
| [Agentic SOC Platform](https://github.com/FunnyWolf/agentic-soc-platform) | Open-source security-operations platform combining SOAR playbooks with LLM agents for alert-to-case convergence, investigation, enrichment and knowledge capture; integrates Splunk and ELK. | Not yet checked | active |
| [Agentic Threat Hunting Framework (ATHF)](https://github.com/Nebulock-Inc/agentic-threat-hunting-framework) | Framework for building threat-hunting systems that remember past hunts, learn from them and act with increasing autonomy. | Not yet checked | active |
| [AI Agent SOC Triage](https://github.com/Citadel-Cloud-Management/ai-agent-soc-triage) | Python triage agent that classifies alerts against MITRE ATT&CK, scores severity, extracts IOCs and can run response playbooks; works with Splunk, Sentinel and Elastic. | MIT (Project-stated) | active |
| [AI-Powered SOC Alert Triage Agent](https://github.com/xBlackwater/AI-Powered_SOC-Alert-Triage-Agent-) | Capstone-style triage agent built on Hermes Agent: selectively enriches IOCs with free threat-intel APIs, maps behaviour to MITRE ATT&CK and outputs a ranked triage report. | MIT (Verified) | active |
| [AI-SOC (research implementation)](https://github.com/waitesgithub/AI_SOC) | Dockerised reference implementation of an LLM-augmented SOC covering alert triage, RAG-based threat intelligence over MITRE ATT&CK and log summarisation, grounded in a published survey. | Apache-2.0 (Project-stated) | active |
| [Autonomous AI SOC Analyst](https://github.com/ravishkarathnayaka/autonomous-ai-soc-analyst) | Tier-1 SOC agent that ingests Sysmon, CloudTrail and Zeek telemetry, enriches indicators, builds an attack graph and issues a true/false-positive verdict with containment suggestions. Runs with a local LLM via Ollama. | MIT (Verified) | active |
| [seclab-taskflow-agent](https://github.com/GitHubSecurityLab/seclab-taskflow-agent) | YAML-driven multi-agent taskflow framework from GitHub Security Lab that pairs LLM agents with CodeQL for vulnerability research. | Not yet checked | active |
| [Vigil](https://github.com/Vigil-SOC/vigil) | Open-source agentic SOC with a dozen specialist agents (triage, investigation, hunting, forensics, threat intel, malware and network analysis), Markdown playbooks and MCP-based integrations. Keeps a human approving response actions. | Apache-2.0 (Project-stated) | active |

## Digital Forensics & IR
| Tool | What it does | License | State |
|---|---|---|---|
| [AgentDFIR](https://github.com/efij/AgentDFIR) | Forensics for AI agents themselves: collects and reconstructs activity from Claude Code, Codex CLI, Cursor, Gemini CLI and Copilot, and flags orphan agents, cross-agent messaging and destructive commands. Go CLI. | Not yet checked | active |
| [Agentic-DFIR](https://github.com/Juwon1405/agentic-dfir) | Autonomous DFIR agent for the SANS SIFT Workstation that enforces evidence-integrity rules in its architecture (typed forensic operations) rather than relying on prompts, and produces a traceable report. | MIT (Project-stated) | active |
| [ForceCode DFIR](https://github.com/newCYS/ForceCode-DFIR) | Terminal-native DFIR environment orchestrating specialised agents for artifact, memory, network, timeline and malware analysis plus reporting; its author describes it as still evolving. | Not yet checked | active (early) |
| [Sentinel DFIR-CTI Agent](https://github.com/krshydv/sentinel-dfir-cti-agent) | Academic-style hybrid framework combining ML anomaly detection, rules, correlation, IOC/ATT&CK enrichment and a planned agent layer for forensics and threat intelligence. | Not yet checked | in development |

## Malware & Reverse Engineering
| Tool | What it does | License | State |
|---|---|---|---|
| [Agentic Malware Analysis](https://github.com/mrphrazer/agentic-malware-analysis) | Kali-based container with 50+ RE tools and a Claude Code/Codex skill that runs a multi-phase malware-analysis workflow through Binary Ninja or Ghidra MCP backends and writes IOC-bearing reports. | Not yet checked | active |
| [Open-ReverseLab](https://github.com/LING71671/open-reverselab) | Reverse-engineering agent lab exposing 100+ MCP tools across Ghidra, Frida, x64dbg and Rizin, plus an executable knowledge base, for PE/APK/binary analysis and CTFs. | Not yet checked | active |
| [pyghidra-mcp](https://github.com/clearbluejar/pyghidra-mcp) | MCP server exposing Ghidra analysis (decompile, xrefs, project-wide queries) to LLM agents with compact, token-efficient tool descriptions. | Not yet checked | active |

## MCP Servers & Skills
| Tool | What it does | License | State |
|---|---|---|---|
| [Anthropic-Cybersecurity-Skills (community)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Large library of structured cybersecurity skills (800+ across ~30 domains) for AI agents, following the agentskills.io standard and mapped to frameworks such as MITRE ATT&CK and NIST CSF. | Not yet checked | active |
| [BloodHound-MCP-AI](https://github.com/MorDavid/BloodHound-MCP-AI) | Natural-language interface to BloodHound: wraps Cypher queries as about 75 tools for Active Directory attack-path analysis. | Not yet checked | active |
| [HexStrike AI](https://github.com/0x4m4/hexstrike-ai) | MCP server that lets AI clients drive 150+ security tools through a team of specialised agents. | Not yet checked | active |
| [MCP-Kali-Server](https://github.com/Wh0am123/MCP-Kali-Server) | Lightweight API bridge, packaged in Kali's repositories, letting AI clients run tools like nmap, sqlmap and hydra for assisted testing and CTFs. | Not yet checked | active |
| [mcp-security-hub](https://github.com/FuzzingLabs/mcp-security-hub) | Collection of about 38 containerised MCP servers wrapping 300+ security tools for recon, web, binary analysis, cloud and fuzzing. | Not yet checked | active |
| [MetasploitMCP](https://github.com/GH05TCREW/MetasploitMCP) | MCP bridge to the Metasploit Framework for module selection, payload generation and session handling from an AI client. | Not yet checked | active |
| [PortSwigger MCP Server](https://github.com/PortSwigger/mcp-server) | Official Burp Suite extension bridging Burp with MCP clients such as Claude Desktop. | Not yet checked | active |

## Vulnerability Research
| Tool | What it does | License | State |
|---|---|---|---|
| [ATLANTIS (DARPA AIxCC)](https://github.com/Team-Atlanta/aixcc-afc-atlantis) | Open-sourced cyber reasoning system from the AIxCC 2025 winning team, combining fuzzing, symbolic execution and LLM agents to find and fix vulnerabilities. | Not yet checked | active |
| [Buttercup (DARPA AIxCC)](https://github.com/trailofbits/buttercup) | Trail of Bits' cyber reasoning system from the DARPA AI Cyber Challenge finals (2nd place) for automated vulnerability discovery and patching. | Not yet checked | active |

## Securing AI Agents
| Tool | What it does | License | State |
|---|---|---|---|
| [Agent Threat Rules (ATR)](https://github.com/Agent-Threat-Rule/agent-threat-rules) | Open detection-rule standard for AI-agent threats, positioned as Sigma for AI agents. | Not yet checked | active |
| [Agentic Radar](https://github.com/splx-ai/agentic-radar) | CLI scanner that maps agentic workflows (LangGraph, CrewAI, OpenAI Agents and others), their tools and data flows, and flags security risks. | Not yet checked | active |

## Licensing notes worth knowing
Some entries carry terms that matter for commercial or hosted use: Shannon is AGPL-3.0 with paid editions, PentAGI ships an EULA and NOTICE beside its MIT license, and Strix has paid cloud/enterprise editions beside its Apache-2.0 core. Full per-entry notes are in [`data/agents.json`](data/agents.json) (to be added).

## Submit your agent
Built a free agentic AI tool for security or forensics? [Open a submission](../../issues/new?template=submit-agent.yml). A maintainer reviews each one against [VERIFICATION.md](VERIFICATION.md) before it is listed. Newest releases are added at the top.

## Data and copyright
Descriptions are written by curators in their own words. Each tool remains the property of its authors under its own license; names and logos belong to their owners. Listing a tool does not grant any rights to it. Open an issue to correct or remove an entry.
