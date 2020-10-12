#!/usr/bin/python

# https://www.youtube.com/watch?v=BYl3-c2JSL8

# Code does not work for some reason and can't be bothered just follow the video and you'll get it and use burpsuite or sth

import requests, urllib

url = "http://natas31.natas.labs.overthewire.org/index.pl"
auth = ("natas31", "hay7aecuungiuKaezuathuk9biin0pu1")

s = requests.Session()

r = requests.Request('POST', url, auth=auth)

r = r.prepare()

r.body = '''
-----------------------------4074623675611050622373364753
Content-Disposition: form-data; name="file"; filename="Warframe.desktop"
Content-Type: application/x-desktop

[Desktop Entry]
Name=Warframe
Comment=Play this game on Steam
Exec=steam steam://rungameid/230410
Icon=steam_icon_230410
Terminal=false
Type=Application
Categories=Game;

-----------------------------4074623675611050622373364753
Content-Disposition: form-data; name="submit"

Upload
-----------------------------4074623675611050622373364753--
''' 

r.headers['Content-Type'] = 'multipart/form-data; boundary=---------------------------4074623675611050622373364753'
r.headers['Content-Length'] = len(r.body)
r.headers['Connection'] = 'close'

res = s.send(r)
print(res.text)
print(r.headers)

