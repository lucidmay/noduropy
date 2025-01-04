import requests
from noduro.entity.nodes import Node
from noduro.entity.publish import Publish, PublishStatus

class APIClient:
    def __init__(self, port=4647, api_key=None):
        self.base_url = f"http://localhost:{port}/api"
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({'Authorization': f'Bearer {api_key}'})
        self.session.headers.update({'Content-Type': 'application/json'})
    
    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)

        if response.status_code not in (200, 201):
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
        return response.json()

    def get_node(self, node_id) -> Node:
        response = self._make_request("POST", "/node", json=node_id)
        if response.get('error'):
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
        return Node.from_json(response)


    def get_roots(self):
        return self._make_request("GET", "/roots")
    
    def create_component_node(self, name, parent_node_tb, parent_node_id):
        return self._make_request("POST", "/node/create_component", json={"name": name, "parent_node_tb": parent_node_tb, "parent_node_id": parent_node_id})
    
    def publish_new(self, publish: Publish):
        print(publish.to_json())
        return self._make_request("POST", "/node/publish", json=publish.to_json())


if __name__ == "__main__":
    api_client = APIClient()
    # node_id = {'tb': 'nodes-1b64faa8-ed3a-48cd-98ab-ffbbeb9d9bde', 'id': {'String': '@root/show:triplets'}}
    # node = api_client.get_node(node_id)
    # print(node)


    # publish
    publish = Publish.new(
        userid=None,
        comment="test",
        entries={"assembly": "assembly.usda"},
        status=PublishStatus.PUBLISHED,
        version=None,
        software="houdini",
        thumbnail="thumbnail.png",
        metadata={"assembly": "assembly.usda"},
    )

    res = api_client.publish_new(publish)
    print(res)
