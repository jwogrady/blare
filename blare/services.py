from blare.utils import request

def services_getlist(client_id, package_id):
    model ='services/'
    action = 'getlist'
    params = {'client_id': client_id, 'filters[package_id]': package_id}
    resp = request(model=model, action=action, params=params)

    return resp