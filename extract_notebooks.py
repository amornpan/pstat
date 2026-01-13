import json
import os

notebooks = [
    r"C:\Users\Asus\pstat\2025-12-27\datavis.ipynb",
    r"C:\Users\Asus\pstat\2026-01-03\distributions.ipynb",
    r"C:\Users\Asus\pstat\2026-01-03\test_of_means.ipynb",
    r"C:\Users\Asus\pstat\2026-01-10\chisq.ipynb",
    r"C:\Users\Asus\pstat\2026-01-10\correlation.ipynb",
]

for nb_path in notebooks:
    if os.path.exists(nb_path):
        print(f"\n{'='*80}")
        print(f"FILE: {nb_path}")
        print('='*80)
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        for i, cell in enumerate(nb.get('cells', [])[:80]):
            if cell['cell_type'] == 'markdown':
                print(f"\n[MARKDOWN {i}]")
                print(''.join(cell['source']))
            elif cell['cell_type'] == 'code':
                print(f"\n[CODE {i}]")
                print(''.join(cell['source']))
                if cell.get('outputs'):
                    for out in cell['outputs'][:2]:
                        if out.get('output_type') == 'stream' and out.get('text'):
                            text = ''.join(out['text']) if isinstance(out['text'], list) else out['text']
                            print(f"[STREAM OUTPUT]: {text[:800]}")
                        elif out.get('output_type') == 'execute_result':
                            if out.get('data', {}).get('text/plain'):
                                txt = out['data']['text/plain']
                                txt = ''.join(txt) if isinstance(txt, list) else txt
                                print(f"[RESULT]: {txt[:800]}")
                        elif out.get('output_type') == 'display_data':
                            if out.get('data', {}).get('text/plain'):
                                txt = out['data']['text/plain']
                                txt = ''.join(txt) if isinstance(txt, list) else txt
                                print(f"[DISPLAY]: {txt[:300]}")
    else:
        print(f"NOT FOUND: {nb_path}")
