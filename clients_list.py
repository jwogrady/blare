from blare.clients import clients_getAll
from blare.utils import load_json, dump_json
# Clients Report

resp = clients_getAll(client_status="active", client_group_id=1)

print(resp.content, file=open('output/clients_resp.json', 'w'))

load = load_json(resp.content)

print(load, file=open('output/clients_list_load.json', 'w'))

print(dump_json(load), file=open('output/clients_list_dump.json', 'w'))

list = []

r = load_json(resp.content)
for x in r['response']:
    list.append([x['id'],x['id_value'],x['id_code'],x['company_id']])

print(80 * "-")
print(*list, sep="\n")
print(80 * "-")
print(f"Count: {len(list)}")