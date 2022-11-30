import requests
import json

status='available'
params={'status': 'available'}
headers={'accept': 'application/json', 'Content-Type': 'application/json'}
base_url="https://petstore.swagger.io/"

res1=requests.get(base_url + 'v2/pet/findByStatus', params=params, headers=headers)
print(res1.status_code)
print(res1.text)
print(res1.json)
print(type(res1.json()))

### My requests - task 19.3.3

datapet={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "MyKitty",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res1=requests.post(base_url+'v2/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(datapet, ensure_ascii=False))
print("POST - adding pet request:", res1.status_code)
print(res1.text)

res2 = requests.put(base_url+'v2/pet', headers=headers, data=json.dumps(datapet, ensure_ascii=False))
print("PUT - edit pet request:", res2.status_code)
print(res2.text)

petID = res2.json()['id']

res3 = requests.get(base_url+'v2/pet/'+str(petID), params=params, headers=headers)
print("GET - get pet request:", res3.status_code)
print(res3.text)

res4 = requests.delete(base_url+'v2/pet/'+str(petID), params=params, headers=headers)
print("DELETE - delete pet request:", res4.status_code)
print(res4.text)

