from core.base_api import BaseAPI
from utils.config import BASE_URL


class WishlistAPI:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    # GET Wishlist
    def get_wishlist(self, shopper_id, headers):
        return self.api.get(
            f"/shoppers/{shopper_id}/wishlist",
            headers=headers
        )

    # POST Add to Wishlist
    def add_to_wishlist(self, shopper_id, headers, product_id, quantity):
        payload = {
            "productId": product_id,
            "quantity": quantity
        }

        return self.api.post(
            f"/shoppers/{shopper_id}/wishlist",
            headers=headers,
            json=payload
        )