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
        return cls._instance

    def get_roots(self):
        return self._make_request("GET", "/roots")

    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        start = time.time()
        response = self._session.request(method, url, **kwargs)
        network_time = time.time() - start
        
        start = time.time()
        data = response.json()
        parse_time = time.time() - start
        
        print(f"Network time: {network_time:.3f}s")
        print(f"Parse time: {parse_time:.3f}s")
        return data

# Usage in Houdini
api_client = APIClient()  # Create once at startup
