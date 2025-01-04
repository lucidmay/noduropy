import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from noduro.api import APIClient

def main():
    client = APIClient()
    # root = client.get_roots()
    # print(root)
    name = "testComponent3"
    parent_node_tb = "nodes-c2a555ef-69cd-46a6-baba-9d78c1674868"
    parent_node_id = "@root/show:triplet/seq:triplet_TKR/shot:TKR_1001"


    res = client.create_component_node(name, parent_node_tb, parent_node_id)
    print(res)

if __name__ == "__main__":
    main()

