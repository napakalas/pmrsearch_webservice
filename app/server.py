import os

from sanic import Sanic
from sanic.response import json

SANIC_PREFIX = "SANIC_"

app = Sanic(name='NGINX_SANIC_VUE')

from pmrsearch import PMRSearcher
searcher = PMRSearcher()

@app.route("/search/<tag>")
async def search(request, tag):
    query = request.args.get('query')
    context = request.args.get('context', '')
    context = [] if len(context)==0 else context.split(',')
    topk = int(request.args.get(topk, 5))
    min_sim = float(request.args('minsim', 0.8))
    c_weight = float(request.args('cweight', 0.8))
    if tag=='exposure':
        return json(searcher.search_exposure(query=query, context=['Liver'], topk=topk,  min_sim=min_sim, c_weight=c_weight))
    elif tag=='workspace':
        return json(searcher.search_workspace(query=query, context=['Liver'], topk=topk,  min_sim=min_sim, c_weight=c_weight))
    elif tag=='cellml':
        return json(searcher.search_cellml(query=query, context=['Liver'], topk=topk,  min_sim=min_sim, c_weight=c_weight))
    elif tag=='all':
        return json(searcher.search_all(query=query, context=['Liver'], topk=topk,  min_sim=min_sim, c_weight=c_weight))
    
    return json([])


# while in docker files from static will be served by ngnix
app.static('/static', './static')
if __name__ == "__main__":
    for k, v in os.environ.items():
        if k.startswith(SANIC_PREFIX):
            _, config_key = k.split(SANIC_PREFIX, 1)
            app.config[config_key] = v
    app.run(
        host="0.0.0.0",
        port=8000,
        workers=1,
        auto_reload=True,
        access_log=False,
    )
