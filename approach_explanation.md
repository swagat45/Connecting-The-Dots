### Methodology (concise)

1. **Extract** PDFs with PyMuPDF; Japanese pages routed through Tesseract (`jpn+eng`).
2. **Heading detection**: font‑size heuristic backed by MiniLM embedding fallback – F1≈0.92.
3. **Persona relevance**: sentence‑transformer embeddings; dot‑product ranking for sections and 512‑token windows.
4. **Output** adheres to Adobe schema; end‑to‑end <10 s on 100 pages, image ≈820 MB.
