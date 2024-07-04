'''
 * All public model methods are accessible. Plugin models may also be invoked by
 * simply formatting the model as Plugin.Model
 * (e.g. /api/plugin.model/method.format). Supports XML, JSON, and PHP as format
 * types.
 *
 '''

from blare.utils import request, dump_json, load_json

def domains_getall():
    model ='domains.domains_domains/'
    action = 'getAll'
    params = {
        'order[]': ['id']  # passed as arrayed value.
        }
    resp = request(model=model, action=action, params=params)

    return resp