from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from pathlib import Path
import json, time

_model = SentenceTransformer('src/models/all-MiniLM-L6-v2')

def _chunk(t, size=512, overlap=128):
    w=t.split()
    for i in range(0,len(w),size-overlap):
        yield ' '.join(w[i:i+size])

def persona_extract(inp:Path, persona:str, job:str, top_k=15, sub_k=40):
    docs=list(inp.glob('*.json'))
    meta=f'{persona}. {job}'
    m_emb=_model.encode(meta, normalize_embeddings=True)
    ranked=[]
    for f in docs:
        data=json.loads(f.read_text())
        for o in data['outline']:
            txt=' '.join(w for w in o['text'].split() if w.lower() not in ENGLISH_STOP_WORDS)
            scr=float(util.dot_score(m_emb,_model.encode(txt,normalize_embeddings=True)))
            ranked.append({**o,'document':f.stem,'score':scr})
    ranked.sort(key=lambda x:-x['score'])
    subs=[]
    for sec in ranked[:top_k]:
        pdata=json.loads((inp/f'{sec["document"]}.json').read_text())['outline_text']
        for ch in _chunk(pdata.get(str(sec['page']),'') ):
            subs.append({'document':sec['document'],'page':sec['page'],
                         'refined_text':ch,'parent_section_title':sec['text'],
                         'score':float(util.dot_score(m_emb,_model.encode(ch,normalize_embeddings=True)))})
    subs.sort(key=lambda x:-x['score'])
    now=time.strftime('%Y-%m-%dT%H:%M:%S')
    return {'metadata':{'input_documents':[d.name for d in docs],
                        'persona':persona,'job':job,'processed_at':now},
            'extracted_sections':[ {k:v for k,v in s.items() if k!='score'} | {'importance_rank':i+1} for i,s in enumerate(ranked[:top_k])],
            'subsections':[ {k:v for k,v in s.items() if k!='score'} for s in subs[:sub_k]]}
