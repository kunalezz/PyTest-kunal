from utils.read_data import read_json
from API.ShopperProfile.update_user_data import UpdateUserData
from core.auth import get_auth_data

update_data = UpdateUserData()

def test_update_user_data(auth_data, headers):
    data = read_json("test_data/update_data.json")

    auth = get_auth_data()
    shopper_id = auth["shopper_id"]
    response = update_data.update_user_data(shopper_id, data, headers=headers)

    assert response.status_code == 200, response.text

    print("STATUS:", response.status_code)
    print(f"shopper_id: {shopper_id}")