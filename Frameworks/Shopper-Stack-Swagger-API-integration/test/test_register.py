from utils.read_data import read_json
from API.ShopperProfile.register_api import RegisterAPI

register_api = RegisterAPI()

def test_register_user():
    data = read_json("test_data/register.json")
    response = register_api.register(data)

    assert response.status_code == 201, response

    res_json = response.json()
    shopper_id = res_json["data"]["userId"]
    print("SHOPPER ID:", shopper_id)