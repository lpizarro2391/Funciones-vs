import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
requests.get('https://api.github.com', verify=False)
