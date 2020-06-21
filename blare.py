import os

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

api_usr = os.environ.get('API_USR')
api_key = os.environ.get('API_KEY')

url = 'https://aware.status26.com/api/clients/getlist.json'

print(api_key)

t = requests.get(url, auth=HTTPBasicAuth(api_usr, getpass()))

print(t.content)