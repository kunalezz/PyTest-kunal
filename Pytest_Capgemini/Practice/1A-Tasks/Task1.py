import requests
response = requests.get('https://petstore.swagger.io/v2/store/inventory')

responseJson = response.json()

expected = 200
actual = response.status_code

assert expected == actual, f"{actual}"

print(responseJson['available'])