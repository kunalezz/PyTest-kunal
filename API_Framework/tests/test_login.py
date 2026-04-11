from api.login.login_api import LoginAPI
from utils.read_data import read_json

login_api = LoginAPI()

def test_valid_login():
    data = read_json("test_data/login_data.json")

    payload = data["valid_user"]

    response = login_api.login(payload)

    assert response.status_code == 200

    res_json = response.json()
    shopper_id = res_json["data"]["userId"]
    print("SHOPPER ID:", shopper_id)

def test_invalid_login():
    data = read_json("test_data/login_data.json")

    payload = data["invalid_user"]

    response = login_api.login(payload)

    assert response.status_code in [400, 401]
