from blare import request

# Clients
def clients_getAll(client_status, client_group_id):
    model ='clients/'
    action = 'getall'
    params = {'client_status': client_status, 'filters[client_group_id]': client_group_id}
    resp = request(model=model, action=action, params=params)

    return resp

# Services
def services_getlist(client_id, package_id):
    model ='services/'
    action = 'getlist'
    params = {'client_id': client_id, 'filters[package_id]': package_id}
    resp = request(model=model, action=action, params=params)

    return resp

def services_getbyclient(client_id, package_id):
    model = 'services/'
    action = 'getallbyclient'
    params = {'client_id': client_id, 'package_id': package_id}
    resp = request(model=model, action=action, params=params)

    return resp

# Staff
def staff_get(params):
    model ='staff/'
    action = 'get'
    resp = request(model=model, action=action, params=params)
    return resp

def staff_getlist(params):
    model ='staff/'
    action = 'getlist'
    resp = request(model=model, action=action, params=params)
    return resp