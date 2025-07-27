<p align="center">
  <img src="demo.gif" width="460"><br>
  <h3>Connecting&nbsp;the&nbsp;Dots<br><sub>Adobe India Hackathon 2025 • CPU-only • Offline • &lt;1 GB Image</sub></h3>
</p>

<p align="center">
  <a href="https://github.com/swagat45/Connecting-The-Dots/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/swagat45/Connecting-The-Dots/ci.yml?label=CI&logo=github&style=flat-square">
  </a>
  <img src="https://img.shields.io/badge/Image-size-≈820 MB-blue?style=flat-square">
  <img src="https://img.shields.io/github/languages/code-size/swagat45/Connecting-The-Dots?style=flat-square">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square">
</p>

---

<details open>
<summary><b>📑 Table of Contents</b></summary>

- [✨ Why you’ll like it](#why)
- [🚀 Quick Start](#quick-start)
- [📊 Metrics](#metrics)
- [🖼️ Architecture](#architecture)
- [📂 Repo Layout](#repo-layout)
- [📝 Approach (300 words)](#approach)
- [🤝 License](#license)
</details>

---

<a id="why"></a>
## ✨ Why you’ll like it

|   | Capability |
|---|------------|
| 🔍 | **Heading extraction** – F1 0.92 (EN) / 0.88 (JP) |
| 🧑‍🔬 | **Persona relevance** – MiniLM embeddings rank the sections *that matter* |
| 📴 | **Offline-ready** – no network during judging |
| 🧹 | **Single-command build** – `docker build .` (image ≈ 820 MB) |
| 🧑‍💻 | **CI smoke-test** on every push/tag |

<a id="quick-start"></a>
<p align="center">
  <a href="https://github.com/swagat45/Connecting-The-Dots/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/swagat45/Connecting-The-Dots/ci.yml?branch=main&label=CI&logo=github">
  </a>
  <img src="https://img.shields.io/badge/Image-size-≈820 MB-blue">
  <img src="https://img.shields.io/badge/Latency-7-9 s%20%2F%20100pp-brightgreen">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

## ✨ What this repository does

| Round | Goal | How it’s solved |
|-------|------|-----------------|
| **1 A – Heading Detection** | Extract H1-H3 outline for every PDF page | PyMuPDF font-size heuristic + MiniLM fallback <br>F1 ≈ 0.92 (EN) / 0.88 (JP) |
| **1 B – Persona-Driven Extraction** | Rank the most relevant sections & sub-chunks for a given persona + job | Dot-product similarity ( MiniLM ) + stop-word filter |

*No GPU, no internet at runtime – all models are baked into the Docker image.*

---
graph TD
    A[PDFs] -->|PyMuPDF<br>or Tesseract (JP)| B[Heading Detector]
    B --> C[MiniLM Embeddings]
    C -->|dot-product| D[Section Ranker]
    D --> E[JSON (Output)]
---


## 🚀 Quick start

```bash
# build once
docker build -t connectdots:latest .

# Round-1A: heading JSONs
docker run -v $PWD/sample_docs:/in  -v $PWD/out1a:/out connectdots:latest

# Round-1B: persona ranking
docker run -v $PWD/sample_docs:/app/input \
           -v $PWD/out1b:/app/output      \
           -v $PWD/meta:/app/meta         \
           connectdots:latest persona
## 🚀 Quick Start

```bash
# Build image
docker build -t connectdots:latest .

# Round-1 A – heading JSONs
docker run -v $PWD/sample_docs:/in  -v $PWD/out1a:/out \
           connectdots:latest

# Round-1 B – persona ranking
docker run -v $PWD/sample_docs:/app/input \
           -v $PWD/out1b:/app/output      \
           -v $PWD/meta:/app/meta         \
           connectdots:latest persona
