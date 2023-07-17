from blare import request

def getAll(client_status, client_group_id):
    model ='clients/'
    action = 'getall'
    payload = {'client_status': client_status, 'filters[client_group_id]': client_group_id}
    resp = request(model=model, action=action, payload=payload)

    return resp