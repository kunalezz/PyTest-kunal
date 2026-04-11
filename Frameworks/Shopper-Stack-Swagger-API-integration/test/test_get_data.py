from API.ShopperProfile.get_user_data import GetUserData
from core.auth import get_auth_data

get_data = GetUserData()

def test_get_user_data(auth_data, headers):
    data = get_auth_data()
    shopper_id = data["shopper_id"]

    response = get_data.get_user_data(shopper_id, headers=headers)

    assert response.status_code == 200, response.text

    print("STATUS:", response.status_code)
    print(f"shopper_id: {shopper_id}")