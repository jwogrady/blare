from blare import load_json, dump_json
from blare.staff import getlist, get

payload = {'status': 'active'}
resp = getlist(payload)
payload = {'staff_id': 1}
resp2 = get(payload)


r = load_json(resp.content)
r2 = load_json(resp2.content)

data = dump_json(r)
data2 = dump_json(r2)
print(data, file=open('output/staff_getlist.json', 'w'))
print(data2, file=open('output/staff_get.json', 'w'))