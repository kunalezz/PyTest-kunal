import requests

class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, headers=None, params=None):
        return self.session.get(f"{self.base_url}{endpoint}", headers=headers, params=params, verify=False)

    def post(self, endpoint, headers=None, json=None, params=None):
        return self.session.post(f"{self.base_url}{endpoint}", headers=headers, json=json, params=params, verify=False)

    def put(self, endpoint, headers=None, json=None, params=None):
        return self.session.put(f"{self.base_url}{endpoint}", headers=headers, json=json, params=params, verify=False)

    def patch(self, endpoint, headers=None, json=None, params=None):
        return self.session.patch(f"{self.base_url}{endpoint}", headers=headers, json=json, params=params, verify=False)

    def delete(self, endpoint, headers=None, params=None):
        return self.session.delete(f"{self.base_url}{endpoint}", headers=headers, params=params, verify=False)

