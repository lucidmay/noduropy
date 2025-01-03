import requests
import time

class APIClient:
    _instance = None
    _session = None
    BASE_URL = "http://localhost:4647/api"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._session = requests.Session()
            # Warm up common endpoints
            cls._session.get(f"{cls.BASE_URL}/roots")
            print("API Client initialized and warmed up")
        return cls._instance

    def get_roots(self):
        return self._make_request("GET", "/roots")

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        response = self._session.request(method, url, **kwargs)
        return response.json()

# Global instance
client = APIClient() 