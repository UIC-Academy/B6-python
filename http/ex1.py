import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/5")
print(response)
print(response.json())
print(response.status_code)


response = requests.post(
    url="https://jsonplaceholder.typicode.com/posts",
    json={
        "title": "Eshmat",
        "body": "Toshmat",
        "userId": 1
    }
)
print(response)
print(response.json())
print(response.status_code)


response = requests.put(
    url="https://jsonplaceholder.typicode.com/posts/5",
    json={
        "title": "Eshmat",
        "body": "Toshmat",
        "userId": 1
    }
)
print(response)
print(response.json())
print(response.status_code)

response = requests.delete(
    url="https://jsonplaceholder.typicode.com/posts/5"
)
print(response)
print(response.status_code)