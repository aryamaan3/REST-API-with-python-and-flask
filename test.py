import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "video/1")
print(response.json())
input()
response = requests.patch(BASE + "video/1", {"views": 100})
print(response.json())
