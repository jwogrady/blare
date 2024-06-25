from blare import load_json, dump_json
from blare.api import clients_getAll

from blare.settings import client_status, client_group_id

"""
"response": [
    {
      "id": "1",
      "id_format": "{num}",
      "id_value": "1500",
      "user_id": "2",
      "client_group_id": "1",
      "primary_account_id": null,
      "primary_account_type": null,
      "status": "active",
      "id_code": "1500",
      "contact_id": "1",
      "first_name": "John",
      "last_name": "O'Grady",
      "company": "Status26 Inc.",
      "email": "john@status26.com",
      "address1": "PO BOX 608",
      "address2": "",
      "city": "Denton",
      "state": "TX",
      "zip": "76202",
      "country": "US",
      "group_name": "Status26",
      "company_id": "1"
    },
"""


resp = clients_getAll(client_status, client_group_id)

print(resp.url)

list = []

r = load_json(resp.content)
for x in r['response']:
    list.append(x['company'])

data = dump_json(r)
print(data, file=open('output/clients.json', 'w'))
print(data)

print(500 * "-")

print(*list, sep="\n")