import requests
import json

from requests.auth import HTTPBasicAuth

from blare.settings import blesta_url, blesta_format, blesta_usr, blesta_key


def make_url(model, action):
    url = blesta_url
    format = blesta_format
    url_parts = [url, model, action, format]
    url = ''.join(url_parts)
    return url


def request(model, action, payload):
    url = make_url(model, action)
    basic = HTTPBasicAuth(username=blesta_usr, password=blesta_key)
    response = requests.get(url=url, auth=basic, params=payload)
    return response


def load_json(r):
    jason_objects = json.loads(r)
    return jason_objects


def dump_json(r):
    r = json.dumps(r, indent=2)
    return r
