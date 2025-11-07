import requests

response = requests.post('http://localhost:8000/advertisement',
                        json={"title": "adv_7",
                              "description": "desc_adv7",
                              "price":700.5,
                              "author": "aut_adv7"
                              })
print(response.text)
print(response.status_code)

response = requests.get('http://localhost:8000/advertisement/1')

print(response.text)
print(response.status_code)


response = requests.get("http://127.0.0.1:8000/advertisement", params={"title": "adv_7"})

print(response.status_code)
print(response.json())


response = requests.patch("http://127.0.0.1:8000/advertisement/1",
                          json={"title": "new_adv_69"})

print(response.status_code)
print(response.json())

response = requests.get('http://localhost:8000/advertisement/1')

print(response.text)
print(response.status_code)

response = requests.delete('http://localhost:8000/advertisement/1',)

print(response.text)
print(response.status_code)

response = requests.get('http://localhost:8000/advertisement/1')

print(response.text)
print(response.status_code)