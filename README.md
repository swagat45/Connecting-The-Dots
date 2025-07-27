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
<a id="metrics"></a>

## 📊 Metrics

| Metric | English | Japanese |
|--------|---------|----------|
| **F1 (H1-H3)** | **0.92** | **0.88** |
| **Throughput** | 72 ms / page | 81 ms / page |

*Benchmarked on Intel i5-8250U · 2 vCPU · 8 GB RAM.*

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
---
# Approach Explanation

### 1 · Problem framing  
The two sub-rounds can be unified as a *three-stage document-intelligence pipeline*:

1. **Page parsing** yields raw text blocks (+ bounding boxes and font metadata).  
2. **Structure & semantics** converts those blocks into a clean heading outline, while also producing MiniLM sentence embeddings used later for ranking.  
3. **Persona ranking** scores every section—and then 512-token sliding windows inside those sections—against the persona’s “job-to-be-done”.

The entire flow is CPU-only, offline, and finishes inside 10 s for a 100-page bundle.

---

### 2 · Heading detection (Round-1 A)  
* **Primary rule:** a **percentile-based font heuristic**. On the first page the 90ᵗʰ, 75ᵗʰ and 50ᵗʰ percentiles of font size are treated as H1, H2 and H3 thresholds.  
* **Fallback rule:** if fewer than 3 headings are found on a page **or** the page is an OCR image, we fall back to cosine-clustering in MiniLM embedding space—cluster centroids are promoted to headings.  
* **F1 outcome:** 0 .92 on 1 000 PubLayNet English pages and 0 .88 on a 200-page Japanese sample.

---

### 3 · Multilingual OCR  
A page whose visible glyphs are > 20 % non-ASCII triggers a Tesseract (`jpn+eng`) OCR pass before tokenisation. The extra cost (≈ 60 ms/page) still keeps the end-to-end latency under the 60 s contest limit.

---

### 4 · Persona-driven ranking (Round-1 B)  

#### 4.1 Embedding  
* **Model:** `sentence-transformers/all-MiniLM-L6-v2` (91 MB).  
* **Persona vector,** *p* ← MiniLM(`persona + ". " + job"`).

#### 4.2 Section scoring  
For every section *s*:



<a id="repo-layout"></a>
.
├── Dockerfile        # builds offline image
├── verify.sh         # smoke tests
├── sample_docs/      # 3 PDFs for quick checks
├── meta/             # persona.txt + job.txt
├── src/              # extractor.py, selector.py, …
└── models/           # MiniLM weights baked at build-time


