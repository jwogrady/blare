from blare import request

def getAll(client_status, client_group_id):
    model ='clients/'
    action = 'getall'
    params = {'client_status': client_status, 'filters[client_group_id]': client_group_id}
    resp = request(model=model, action=action, params=params)

    return resp