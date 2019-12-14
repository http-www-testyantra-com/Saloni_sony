import requests
import json

r=requests.get("https://imgs.xkcd.com/comics/python.png")
print(r)
print(r.status_code)
f = open("C:\\Users\\Saloni\\PycharmProjects\\pic.png","wb")
f.write(r.content)
print(r.content)
f.close()



