from core.base_api import BaseAPI
from utils.config import BASE_URL

class GetUserData():
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def get_user_data(self, shopperId, headers):
        return self.api.get(f"/shoppers/{shopperId}", headers=headers)
