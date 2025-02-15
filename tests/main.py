import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from noduro.api import APIClient
from noduro.entity.version import Version, VersionStatus
from noduro.entity.utils import Thing


def main():
    client = APIClient()
    # root = client.get_roots()
    # print(root)
    # name = "testComponent6"
    # parent_node_tb = "nodes-c2a555ef-69cd-46a6-baba-9d78c1674868"
    # parent_node_id = "@root/show:triplet/seq:triplet_TKR/shot:TKR_1001/testComponent4"


    # res = client.create_component_node(name, parent_node_tb, parent_node_id)
    # print(res)

    publish = Version.new(
        version=0,
        userid=None,
        comment="test",
        entries={"assembly": "assembly.usda"},
        status=VersionStatus.Active,
        software="houdini",
        thumbnail="thumbnail.png",
        metadata={"assembly": "assembly.usda"},
        properties={},
        main_entry="assembly.usda"
    )

    fullpath = "nodes-358c793c-9a59-4ac9-bd7a-2fb551746543&@root/assembly:myass/shots/seq:VK/shot:VK_1003/fx"
    tb, id = fullpath.split("&")
    component_node_id = Thing.from_str(tb, id)
    res = client.publish_new(publish, component_node_id)
    print(res)

if __name__ == "__main__":
    main()

