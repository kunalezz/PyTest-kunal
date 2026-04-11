from core.base_api import BaseAPI
from utils.config import BASE_URL

class UpdateUserData:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def update_user_data(self, shopperId, payload, headers):
        return self.api.patch(f"/shoppers/{shopperId}", json=payload, headers=headers)