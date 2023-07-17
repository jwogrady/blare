from blare import request

def getbyclient(client_id, package_id):
    model = 'services/'
    action = 'getallbyclient'
    payload = {'client_id': client_id, 'filters[package_id]': package_id}
    resp = request(model=model, action=action, payload=payload)

    return resp

# usage
# r = services_getbyclient(100, 200).content
# t = load_json(r)
# print(dump_json(t))