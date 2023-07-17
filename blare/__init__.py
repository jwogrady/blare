import requests
import json

from requests.auth import HTTPBasicAuth
from dotenv import dotenv_values

config = dotenv_values(".env")
usr = config['BLESTA_USR']
key = config['BLESTA_KEY']



def make_url(model, action):
    url = config['BLESTA_URL']
    format = config['BLESTA_FORMAT']
    url_parts = [url, model, action, format]
    url = ''.join(url_parts)
    return url


def request(model, action, payload):
    url = make_url(model, action)
    basic = HTTPBasicAuth(username=usr, password=key)
    response = requests.get(url=url, auth=basic, params=payload)
    return response


def load_json(r):
    jason_objects = json.loads(r)
    return jason_objects


def dump_json(r):
    r = json.dumps(r, indent=2)
    return r
