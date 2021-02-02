import requests
from config import creds
import json
import getpass

def get_token():
    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password', 'username': creds['username'], 'password': creds['password']}
    auth = requests.auth.HTTPBasicAuth(creds['app_id'], creds['secret_key'])
    r = requests.post(base_url + 'api/v1/access_token',
                    data=data,
                    headers={'user-agent': '{} by {}'.format(creds['app_name'], creds['username'])},
            auth=auth)
    token = r.json()
    with open('token_data.json', 'w') as f:
        json.dump(token, f)