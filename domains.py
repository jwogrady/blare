from blare import load_json, dump_json
from blare.services import getlist

from blare.settings import service_client_id, service_package_id


resp = getlist(service_client_id, service_package_id)


r = load_json(resp.content)


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