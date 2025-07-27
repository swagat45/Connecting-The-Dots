<p align="center">
  <img src="demo.gif" width="460"><br>
  <h3>Connecting&nbsp;the&nbsp;Dots<br><sub>Adobe India Hackathon 2025 • CPU-only • Offline • &lt;1 GB Image</sub></h3>
</p>

<p align="center">
  <a href="https://github.com/swagat45/Connecting-The-Dots/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/swagat45/Connecting-The-Dots/ci.yml?branch=main&label=CI&logo=github&style=flat-square">
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
| 🔍 | **Heading extraction F1** 0.92 (EN) / 0.88 (JP) |
| 🧑‍🔬 | **Persona relevance** – MiniLM ranks what matters |
| 📴 | **Offline-ready** – judges need no internet |
| 🧹 | **Single-command build** – `docker build .` (≈ 820 MB) |
| 🧑‍💻 | **CI smoke-test** on every push / tag |

---

<a id="quick-start"></a>
## 🚀 Quick Start

```bash
# Build once
docker build -t connectdots:latest .

# Round-1 A – heading JSONs
docker run -v $PWD/sample_docs:/in  -v $PWD/out1a:/out connectdots:latest

# Round-1 B – persona ranking
docker run -v $PWD/sample_docs:/app/input \
           -v $PWD/out1b:/app/output      \
           -v $PWD/meta:/app/meta         \
           connectdots:latest persona

---

<a id="metrics"></a>

| Metric         | English      | Japanese     |
| -------------- | ------------ | ------------ |
| **F1 (H1–H3)** | **0.92**     | **0.88**     |
| **Throughput** | 72 ms / page | 81 ms / page |

---
<a id="architecture"></a>


## 🖼️ Architecture

```mermaid
graph TD
    A[PDFs] --> |PyMuPDF / Tesseract| B[Heading Detector]
    B --> C[MiniLM Embeddings]
    C --> |dot-product| D[Section Ranker]
    D --> E[JSON Output]

---

<a id="repo-layout"></a>

## 📂 Repo Layout

.
├── Dockerfile         # builds offline image
├── verify.sh          # local smoke tests
├── sample_docs/       # 3 PDFs for quick checks
├── meta/              # persona.txt & job.txt
├── src/               # extractor.py, selector.py, …
└── models/            # MiniLM weights baked during build






