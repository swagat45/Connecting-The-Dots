<p align="center">
  <img src="demo.gif" width="450"><br>
  <b>Connecting&nbsp;the&nbsp;Dots – Adobe India Hackathon 2025</b><br>
  <sub>CPU-only, offline, ≤1 GB image • Round-1A & Round-1B</sub>
</p>

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
