from core.base_api import BaseAPI
from utils.config import BASE_URL

class LoginAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def login(self, payload):
        return self.api.post("/users/login", json=payload)