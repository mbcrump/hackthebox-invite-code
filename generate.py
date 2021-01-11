#!/usr/bin/env python3
# create a code to use with
# hackthebox.eu

import requests
import base64
import datetime

url = 'https://www.hackthebox.eu/api/invite/generate'
headers = {'content-type': 'application/json', 'user-agent': 'I bet you wish you knew'}
x = requests.post(url, headers=headers)
data = x.json()
value = data['data']['code']

base = base64.b64decode(value)

x = datetime.datetime.now()

print ('<link rel="stylesheet" href="https://mbcrump.github.io/runpython2/mystyle.css">')
print ('<main>')
print ('<ol class="gradient-list">')
print ('<li>')
print ("Your hackthebox invite code is : " + base.decode('utf-8') + "Generated on: " + x)
print ('</li>')

