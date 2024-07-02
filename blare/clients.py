from blare.utils import request

def clients_getAll(client_status=2, client_group_id=1):
    model ='clients/'
    action = 'getall'
    params = {'status': client_status, 'client_group_id': client_group_id}
    resp = request(model=model, action=action, params=params)

    return resp
