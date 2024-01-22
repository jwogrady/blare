from blare import load_json, dump_json
from blare.api import clients_getAll

from blare.settings import client_status, client_group_id


resp = clients_getAll(client_status, client_group_id)

print(resp.url)

r = load_json(resp.content)
data = dump_json(r)
print(data, file=open('output/clients.json', 'w'))
# print(data)