from blare.utils import request, dump_json, load_json

def getall():
    model ='domains.domains_domains/'
    action = 'getAll'
    params = {
        'order[]': ['id']  # passed as arrayed value.
        }
    resp = request(model=model, action=action, params=params)

    return resp

r = load_json(getall().content)
data = dump_json(r)

data = dump_json(r)
print(data)
print(data, file=open('output/domains.json', 'w'))

'''
 * All public model methods are accessible. Plugin models may also be invoked by
 * simply formatting the model as Plugin.Model
 * (e.g. /api/plugin.model/method.format). Supports XML, JSON, and PHP as format
 * types.
 *
 '''