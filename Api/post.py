import requests
import json

parm = {"username":'parey',"password":'9898'}
r = requests.post("http://httpbin.org/post",data=parm)
print(r.text)
print(r.status_code)
