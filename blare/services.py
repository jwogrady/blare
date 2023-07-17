from blare import request

def getlist(client_id, package_id):
    model ='services/'
    action = 'getlist'
    payload = {'client_id': client_id, 'filters[package_id]': package_id}
    resp = request(model=model, action=action, payload=payload)

    return resp

def getbyclient(client_id, package_id):
    model = 'services/'
    action = 'getallbyclient'
    payload = {'client_id': client_id, 'package_id': package_id}
    resp = request(model=model, action=action, payload=payload)

    return resp
