'''import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

postData = {
  "city": "city1",
  "country": "country1",
  "email": "coverdrive@gmail.com",
  "firstName": "name1",
  "gender": "MALE",
  "lastName": "ln1",
  "password": "string",
  "phone": 9876554321,
  "state": "state1",
  "zoneId": "ALPHA"
}

loginData = {
    "email": "coverdrive@gmail.com",
    "password": "string",
    "role": "SHOPPER"
}

base_url = "https://www.shoppersstack.com"
# jwtToken = 0
# id = 0

def userRegistration():
    post = requests.post(f"{base_url}/shopping/shoppers", json=postData,verify=False)

    print(post.status_code)
    return post.json()

def userLogin():

    loginUser = requests.post(f"{base_url}/shopping/users/login", json=loginData,verify=False)

    print(loginUser.status_code)

    global jwtToken, id
    jwtToken = loginUser.json()['data']['jwtToken']
    id = loginUser.json()['data']['userId']

    return loginUser.json()

def getUserData():
    header = { "Authorization": f"Bearer {jwtToken}"}
    userData = requests.get(f"{base_url}/shopping/shoppers/{id}",  headers=header, verify=False)
    print(userData.status_code)

    return userData.json()

print(userRegistration())
print(userLogin())
print(getUserData())'''


'''
Now using session
'''


import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

postData = {
  "city": "city1",
  "country": "country1",
  "email": "coverdrive@gmail.com",
  "firstName": "name1",
  "gender": "MALE",
  "lastName": "ln1",
  "password": "string",
  "phone": 9876554321,
  "state": "state1",
  "zoneId": "ALPHA"
}

loginData = {
    "email": "coverdrive@gmail.com",
    "password": "string",
    "role": "SHOPPER"
}

base_url = "https://www.shoppersstack.com"
session = requests.Session()
# jwtToken = 0
# id = 0

def userRegistration():
    post = session.post(f"{base_url}/shopping/shoppers", json=postData,verify=False)

    print(post.status_code)
    return post.json()

def userLogin():

    loginUser = session.post(f"{base_url}/shopping/users/login", json=loginData,verify=False)

    print(loginUser.status_code)

    global jwtToken, id
    jwtToken = loginUser.json()['data']['jwtToken']
    id = loginUser.json()['data']['userId']

    return loginUser.json()

def getUserData():
    session.headers.update({
        "Authorization": f"Bearer {jwtToken}"
    })
    userData = session.get(f"{base_url}/shopping/shoppers/{id}", verify=False)
    print(userData.status_code)

    return userData.json()

print(userRegistration())
print(userLogin())
print(getUserData())