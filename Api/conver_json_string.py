import requests
import json

parm = {"page":2,"count":4}
r=requests.get("http://httpbin.org/get",params=parm)
print(r.text,type(r.text))
print(r.status_code)
json_data = json.loads(r.text)
print(json_data)
print(r.json)
