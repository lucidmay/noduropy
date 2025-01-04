import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from noduro.api import APIClient
from noduro.entity.publish import Publish, PublishStatus


def main():
    client = APIClient()
    # root = client.get_roots()
    # print(root)
    # name = "testComponent6"
    # parent_node_tb = "nodes-c2a555ef-69cd-46a6-baba-9d78c1674868"
    # parent_node_id = "@root/show:triplet/seq:triplet_TKR/shot:TKR_1001/testComponent4"


    # res = client.create_component_node(name, parent_node_tb, parent_node_id)
    # print(res)

    publish = Publish.new(
        userid=None,
        comment="test",
        entries={"assembly": "assembly.usda"},
        status=PublishStatus.Active,
        version=None,
        software="houdini",
        thumbnail="thumbnail.png",
        metadata={"assembly": "assembly.usda"},
    )

    res = client.publish_new(publish)
    print(res)

if __name__ == "__main__":
    main()

