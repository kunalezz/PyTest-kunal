from core.base_api import BaseAPI
from utils.config import BASE_URL

class RegisterAPI:

    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def register(self, payload):
        return self.api.post("/shoppers", json=payload)