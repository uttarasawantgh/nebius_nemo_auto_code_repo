# NemotronCoderAI: Hybrid Edge-to-Cloud Agentic Developer Loop & Cell Tower Safety System

[![GitHub Repository](https://img.shields.io/badge/GitHub-nebius__nemo__auto__code__repo-blue?style=flat-square&logo=github)](https://github.com/uttarasawantgh/nebius_nemo_auto_code_repo)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![NVIDIA DGX & NeMo](https://img.shields.io/badge/NVIDIA-DGX%20Spark%20%2F%20NeMo-76B900?style=flat-square&logo=nvidia&logoColor=white)](https://developer.nvidia.com/)
[![Nebius Token Factory](https://img.shields.io/badge/Nebius-Token%20Factory%20(Nemotron--3--Ultra)-orange?style=flat-square)](https://nebius.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

---

## Overview

**NemotronCoderAI** is an advanced hybrid edge-to-cloud agentic developer loop and infrastructure safety monitoring platform built for mobile cell tower environments. Designed to operate across local NVIDIA DGX Spark hardware and the Nebius Cloud infrastructure, the system orchestrates zero-egress local intelligence with massive cloud reasoning power. 

By integrating **NeMo-Switchyard** dynamic routing, the **Nebius Token Factory (powered by NVIDIA Nemotron-3-Ultra 550B)**, and the **Claude Agent SDK**, the platform provides real-time structural health monitoring, automated code auditing, and programmatic Human-in-the-Loop (HITL) safety governance.

---

## Architecture & Core Components

1. **Local Micro-Edge Routing Tier (0.5B / 1.5B / 7B-VL):** 
   - Runs locally on DGX Spark edge nodes.
   - Handles routine structural telemetry pings, instant triage, and zero-egress local privacy tasks.
   - Computes dynamic economic penalty weights ($\lambda$) and token confidence scores.
2. **Cloud Reasoning & Token Factory Tier (550B):** 
   - Utilizes **NVIDIA Nemotron-3-Ultra (550B)** via the Nebius Token Factory.
   - Powers complex cross-site topological load correlations, multi-tower physics simulations, and deep analytical reasoning.
3. **Agentic Execution & Safety Governance:** 
   - Integrated with the Claude Agent SDK and programmatic HITL priority gates (`P0`, `P1`, `P2`) for automated code auditing, vulnerability scanning, and refactoring patch verification (`router.py`).

---

## Project Structure

```text
nebius_nemo_auto_code_repo/
├── agent_runner.py              # Main execution loop for agentic tasks
├── app.py                       # Interactive Streamlit dashboard
├── claude_switchyard_agent.py   # Agentic logic integrating Claude SDK & Switchyard
├── core/
│   └── router.py                # NeMo-Switchyard dynamic routing and confidence logic
├── embedded_router_harness.py   # Edge harness testing script for local DGX deployment
├── nebius_tools/
│   ├── client.py                # Nebius Token Factory API client connector
│   └── code_auditor.py          # Automated code auditing and patch generation
├── scripts/
│   └── auto_dev_loop.py         # Autonomous developer loop pipeline
├── tests/                       # Test suite (app, router, Nebius direct API tests)
├── requirements.txt             # Python dependencies
├── about_project.md             # Comprehensive project story, LaTeX math, and write-up
└── README.md                    # Project documentation

---

## 🚀 Installation & DGX Spark Setup Guide

### 1. Prerequisites
* NVIDIA DGX Spark / On-Premise GPU Node (CUDA 12.0+)
* Python 3.10 or higher
* Docker & NVIDIA Container Toolkit installed

### 2. Clone Repository & Setup Virtual Environment
```bash
git clone https://github.com/uttarasawantgh/techex_amsterdam_repo.git
cd techex_amsterdam_repo

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Launch Local vLLM Inference Engines
Initialize the three local vLLM model containers across distinct ports:

```bash
# Port 8001: 7B-VL Multimodal Engine
python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-7B-Instruct --port 8001 &

# Port 8002: 1.5B Operational Engine
python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-1.5B-Instruct --port 8002 &

# Port 8003: 0.5B Micro-Edge Filter
python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-0.5B-Instruct --port 8003 &
```

---

## 🎮 Step-by-Step Live Demo Guide

To demonstrate the full bidirectional governance architecture, execute the following test cases across the **Streamlit UI** environment.

---

### 🖥️ Part 1: Streamlit UI Demonstrations

Launch the Streamlit web dashboard:
```bash
streamlit run app.py
```

#### Test Case 1: The Critical Test Case (Hard Safety & HITL Intercept)
* **Objective:** Demonstrate automated hard-safety circuit breaking and Human-In-The-Loop (HITL) operator control.
* **Selection:** Select `CRITICAL: Multi-Tower Windshear Torsion (Tower 4)` from the scenario dropdown.
* **Prompt Payload:**  
  `CRITICAL ALERT: Complex multi-tower cascading structural torsion detected across Tower 4 and adjacent relay masts following high-velocity windshear. Thermal and stress fractures span multiple concealed structural joints.`
* **Expected Result:**  
  The dashboard flags the alert, halts automated action, and locks into **`ESCALATE_HITL`**. Scroll down to inspect the **HITL Safety Gate** and click `✅ AUTHORIZE SECURE LOCAL PULL [y]` to simulate operator intervention.

#### Test Case 2: The Routine Test Case (Micro-Edge Baseline)
* **Objective:** Demonstrate sub-second zero-cost telemetry filtering on the micro-edge profile.
* **Selection:** Select `ROUTINE: Scheduled Structural Telemetry Ping` from the scenario dropdown.
* **Prompt Payload:**  
  `INFO: Routine 15-minute telemetry heartbeat. All structural load cells, tilt sensors, and wind velocity gauges reporting nominal baselines.`
* **Expected Result:**  
  Resolves instantly via `0.5B Micro-Edge Filter` as **`LOCAL_RESOLVED`** with $0.00 cloud egress cost.

---

## 🛠️ Tech Stack

* **Inference Engine:** [vLLM](https://github.com/vllm-project/vllm) (Local OpenAI-compatible REST endpoints)
* **Models:** Qwen2.5 Series (`0.5B-Instruct`, `1.5B-Instruct`, `VL-7B-Instruct`), Nemotron-3-Ultra 550B Cloud AI model
* **Frontend UI:** Streamlit
* **Backend Runtime:** Python 3.10 / PyTorch / OpenAI Python API
* **Hardware Target:** NVIDIA DGX Spark / Local CUDA Acceleration

---

## 👤 Author & Acknowledgments

* **Author:** Uttara Sawant  
* **GitHub:** [@uttarasawantgh](https://github.com/uttarasawantgh)
* **Gemini:** Utilized as an AI collaborator for architectural troubleshooting, debugging complex structural normalization logic, and optimizing code documentation. 
