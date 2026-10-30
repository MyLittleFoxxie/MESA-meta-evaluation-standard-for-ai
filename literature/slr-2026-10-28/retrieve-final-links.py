import retrieve,concurrent.futures
jobs=[('R294-pdf','https://aclanthology.org/2024.emnlp-main.812.pdf'),('R295-pdf','https://aclanthology.org/2024.acl-long.511.pdf'),('R327-pdf','https://aclanthology.org/2025.findings-emnlp.431.pdf'),('R331-pdf','https://aclanthology.org/2024.findings-emnlp.726.pdf'),('R341-pdf','https://www.medrxiv.org/content/medrxiv/early/2025/05/07/2025.03.04.25323131.full.pdf'),('C03-pdf','https://zenodo.org/records/18954286/files/AI%20Benchmark%20Half-Life%20in%20Recursive%20Corpora.pdf')]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(retrieve.fetch,jobs):print(r['id'],r.get('file'),r.get('error'),flush=True)
