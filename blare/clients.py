from blare.utils import request

def clients_getAll(client_status, client_group_id):
    model ='clients/'
    action = 'getall'
    params = {'status': client_status, 'client_group_id': client_group_id}
    resp = request(model=model, action=action, params=params)

    return resp
