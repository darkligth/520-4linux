import requests, json

# re = requests.get('https://viacep.com.br/ws/0500100/json/')
# print(re.json)

headers = {"content-type":"application/json"}
data = {"nome":"Felipe", "idade":"28"}

re = requests.post(
    "http://127.0.0.1:5000/",
    data=data,
#   headers=headers
)
#print(re.json())