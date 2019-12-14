import requests
import json

r = requests.get("http://httpbin.org/basic-auth/abcd/123",auth=('abcd','123'))
print(r.text)
print(r.status_code)