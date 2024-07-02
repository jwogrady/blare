from blare.utils import load_json, dump_json
from blare.services import services_getlist
from blare.clients import clients_getAll
from blare.packages import packages_getlist, packages_getall
from blare.staff import staff_getlist, staff_get


# Domain Report
r = load_json(services_getlist(client_id=815, package_id=112).content)

def print_client_domains():
    client_domains = {"client": [], "domain": []}
    for x in r['response']:
        if x["client_company"] not in client_domains['client']:
            client_domains["client"].append(x["client_company"])
        client_domains['domain'].append(x["name"])
    return client_domains

t = print_client_domains()
data = dump_json(t)
print(data, file=open('output/domains.json', 'w'))
print(data)

# Clients Report

resp = clients_getAll(client_status="active", client_group_id=1)

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


# Packages Report

resp = packages_getlist(page=1, status="active")
print(resp.content)

resp = packages_getall(company_id=1, status="active")
print(resp.content)


list = []

r = load_json(resp.content)
for x in r['response']:
    list.append([x['id']])

data = dump_json(r)
print(data, file=open('output/packages.json', 'w'))
print(data)

print(80 * "-")

print(*list, sep="\n")
print(80 * "-")
print(f"Count: {len(list)}")

# Staff Report

payload = {'status': 'active'}
resp = staff_getlist(payload)
payload = {'staff_id': 1}
resp2 = staff_get(payload)

r = load_json(resp.content)
r2 = load_json(resp2.content)

data = dump_json(r)
data2 = dump_json(r2)
print(data, file=open('output/staff_getlist.json', 'w'))
print(data2, file=open('output/staff_get.json', 'w'))


# Services

payload = {'client_id': 815, 'package_id': 112}
resp = services_getlist(**payload)

r = load_json(resp.content)
data = dump_json(r)
print(data, file=open('output/services.json', 'w'))

print(data)