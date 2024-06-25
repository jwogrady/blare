from blare import load_json, dump_json
from blare.api import clients_getAll

from blare.settings import client_status, client_group_id

resp = clients_getAll(client_status, client_group_id)

print(resp.url)

list = []

r = load_json(resp.content)
for x in r['response']:
    list.append([x['id'],x['id_value'],x['id_code'],x['company_id']])

data = dump_json(r)
print(data, file=open('output/clients.json', 'w'))
print(data)

print(80 * "-")

print(*list, sep="\n")
print(80 * "-")
print(f"Count: {len(list)}")
