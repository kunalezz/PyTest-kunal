from api.wishlist.get_wishlist import WishlistAPI

def test_add_to_wishlist(auth_data, headers):
    wishlist_api = WishlistAPI()

    shopper_id = auth_data["shopper_id"]

    response = wishlist_api.add_to_wishlist(
        shopper_id=shopper_id,
        headers=headers,
        product_id=51,      #use valid product id
        quantity=1
    )

    print(response.json())

    assert response.status_code in [200, 201], f"Failed: {response.text}"


def test_get_wishlist(auth_data, headers):
    wishlist_api = WishlistAPI()

    shopper_id = auth_data["shopper_id"]

    response = wishlist_api.get_wishlist(shopper_id, headers)

    print(response.json())

    assert response.status_code == 200