'''
For running all requests using cmd (newman) - Postman

npm i -g newman
newman run PET_STORE.postman_collection.json
newman run PET_STORE.postman_collection.json -e "Pet_store_variable.postman_environment"
npm i -g newman-reporter-html
newman run PET_STORE.postman_collection.json -e "Pet_store_variable.postman_environment" -r html
'''

import requests

currId = 0

payLoad = {
  "id": 91,
  "category": {
    "id": 4,
    "name": "animal4"
  },
  "name": "hehe4",
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

# POST Request
def post():
    postResponse = requests.post('https://petstore.swagger.io/v2/pet', json=payLoad)

    global currId
    currId = postResponse.json()["id"]
    return currId


# GET Request
def get():
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{currId}')

    print(f"GET status code - {response.status_code}")
    print(f"GET response json - {response.json()}")



# DELETE Request
def delete():
    deleteResponse = requests.delete(f'https://petstore.swagger.io/v2/pet/{currId}')

    print(f"delete{deleteResponse.status_code}")
    print(f"{deleteResponse.json()}")

print(post())
get()
delete()