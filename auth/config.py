import getpass
import json

username = getpass.getuser()
final_dir = 'Desktop'
location = '/Users/{}/{}/rcreds.json'.format(username, final_dir)

with open(location) as cred_file:
        creds = json.load(cred_file)