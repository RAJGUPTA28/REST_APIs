import requests
requests.get("https://randomuser.me/api/")
# <Response [200]>


#GET
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()

#POST
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()


#PUT
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()
#{'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}

#PATCH
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
response.json()

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
response.json()
#{'userId': 1, 'id': 10, 'title': 'Mow lawn', 'completed': True}
