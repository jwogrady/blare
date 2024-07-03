from blare.utils import request

def services_getlist(client_id, package_id):
    model ='services/'
    action = 'getlist'
    params = {'client_id': client_id, 'filters[package_id]': package_id}
    resp = request(model=model, action=action, params=params)

    return resp


def getAllByClient(client_id, status):
    model ='services/'
    action = 'getallbyclient'
    params = {'client_id': client_id, 'status': status}
    resp = request(model=model, action=action, params=params)

    return resp