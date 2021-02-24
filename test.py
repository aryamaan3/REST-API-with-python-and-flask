import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "day at zoo", "views": 100000, "likes": 800},
        {"name": "birthday song", "views": 3000, "likes": 20},
        {"name": "python eats otter", "views": 200, "likes": 5}]

print("je fais un put pour ajouter 3 videos au db")

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

print("get video : ")
index = input("0, 1 ou 2\n")
response = requests.get(BASE + "video/" + index)
print(response.json())

print("update, changer la valeur")
key = input("name, views ou likes\n")
value = input("nouvelle valeur : ")
response = requests.patch(BASE + "video/" + index, {key: value})
print(response.json())
