from blare.services import getAllByClient
from blare.utils import load_json, dump_json
# services Report

resp = getAllByClient(client_id=1, status="active")

print(resp.content, file=open('output/services_resp.json', 'w'))

load = load_json(resp.content)

print(load, file=open('output/services_list_load.json', 'w'))

print(dump_json(load), file=open('output/services_list_dump.json', 'w'))

r = load_json(resp.content)

list = []
for x in r['response']:
    if x['package_group_id'] == "4":
        list.append([1, x['id'], x['name'], x['status']])

print(list)