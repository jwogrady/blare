import requests
import json

from requests.auth import HTTPBasicAuth

from dotenv import dotenv_values

env = dotenv_values(".env")

blesta_usr = env['BLESTA_USR']
blesta_key = env['BLESTA_KEY']

blesta_url = env['BLESTA_URL']
blesta_format = env['BLESTA_FORMAT']

def make_url(model, action):
    url = blesta_url
    format = blesta_format
    url_parts = [url, model, action, format]
    url = ''.join(url_parts)
    return url


def request(model, action, params):
    url = make_url(model, action)
    basic = HTTPBasicAuth(username=blesta_usr, password=blesta_key)
    response = requests.get(url=url, auth=basic, params=params)
    return response


def load_json(r):
    jason_objects = json.loads(r)
    return jason_objects


def dump_json(r):
    r = json.dumps(r, indent=2)
    return r