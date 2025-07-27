import fitz, numpy as np
from pathlib import Path

def _font_stats(page):
    fonts=[s[3] for b in page.get_text('dict')['blocks'] for l in b.get('lines',[]) for s in l.get('spans',[])]
    return np.percentile(fonts,[50,75,90]).tolist()

def process_pdf(pdf:Path):
    doc=fitz.open(pdf)
    med,up,top=_font_stats(doc[0])
    outline=[]; full={}
    for i,p in enumerate(doc,1):
        page_txt=[]
        for b in p.get_text('dict')['blocks']:
            for l in b.get('lines',[]):
                for s in l.get('spans',[]):
                    txt=s[4].strip(); sz=s[3]
                    if txt: page_txt.append(txt)
                    if not txt: continue
                    if sz>=top:lvl='H1'
                    elif sz>=up:lvl='H2'
                    elif sz>=med:lvl='H3'
                    else: continue
                    outline.append({'level':lvl,'text':txt,'page':i})
        full[str(i)]=' '.join(page_txt)
    return {'title':outline[0]['text'] if outline else pdf.stem,
            'outline':outline,'outline_text':full}
