from blare import request

def getlist(client_id, package_id):
    model ='services/'
    action = 'getlist'
    params = {'client_id': client_id, 'filters[package_id]': package_id}
    resp = request(model=model, action=action, params=params)

    return resp

def getbyclient(client_id, package_id):
    model = 'services/'
    action = 'getallbyclient'
    params = {'client_id': client_id, 'package_id': package_id}
    resp = request(model=model, action=action, params=params)

    return resp
