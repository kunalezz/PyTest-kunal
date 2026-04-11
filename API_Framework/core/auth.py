from api.login.login_api import LoginAPI
from utils.read_data import read_json

login_api = LoginAPI()

def get_auth_data():
    data = read_json("test_data/login_data.json")
    payload = data["valid_user"]

    response = login_api.login(payload)

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.json())

    assert response.status_code == 200

    res_json = response.json()

    token = res_json["data"]["jwtToken"]
    shopper_id = res_json["data"]["userId"]   # confirm key

    return {
        "token": token,
        "shopper_id": shopper_id
    }