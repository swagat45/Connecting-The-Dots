import sys, pathlib, json, time
from src.extractor import process_pdf
from src.selector import persona_extract

IN = pathlib.Path('/in') if pathlib.Path('/in').exists() else pathlib.Path('/app/input')
OUT = pathlib.Path('/out') if pathlib.Path('/out').exists() else pathlib.Path('/app/output')
META = pathlib.Path('/app/meta')

cmd = sys.argv[1] if len(sys.argv) > 1 else 'extract'

if cmd == 'extract':
    OUT.mkdir(parents=True, exist_ok=True)
    for pdf in IN.glob('*.pdf'):
        (OUT / f'{pdf.stem}.json').write_text(json.dumps(process_pdf(pdf)))
elif cmd == 'persona':
    persona = (META / 'persona.txt').read_text()
    job = (META / 'job.txt').read_text()
    OUT.mkdir(parents=True, exist_ok=True)
    start = time.time()
    (OUT/'persona_result.json').write_text(json.dumps(persona_extract(IN, persona, job)))
    assert time.time() - start < 60, 'Timeout'
else:
    raise SystemExit('Unknown command')
