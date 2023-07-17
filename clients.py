from blare import load_json, dump_json
from blare.clients import getAll

from blare.settings import client_status, client_group_id


resp = getAll(client_status, client_group_id)

print(resp.url)

r = load_json(resp.content)
data = dump_json(r)
print(data, file=open('clients.txt', 'w'))
print(data)