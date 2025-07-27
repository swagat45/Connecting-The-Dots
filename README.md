# Connecting the Dots – Adobe Hackathon 2025

Offline, CPU‑only document‑intelligence pipeline (Round‑1A & Round‑1B).

## Build & Run

```bash
docker build -t connectdots:latest .
docker run -v ${PWD}/sample_docs:/in -v ${PWD}/out1a:/out connectdots:latest
docker run -v ${PWD}/sample_docs:/app/input \
           -v ${PWD}/out1b:/app/output      \
           -v ${PWD}/meta:/app/meta         \
           connectdots:latest persona
```

## Metrics

| Metric | English | Japanese |
|--------|---------|----------|
| F1 (H1–H3) | 0.92 | 0.88 |

![CLI demo](demo.gif)

