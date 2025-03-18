from hyperfabric_SDK import get_devices, get_fabrics, get_fabric, get_fabric_node, \
    update_fabric, add_fabric_connections, delete_fabric, commit_fabric_candidate, \
    add_fabric_nodes, set_ports, add_management_ports, add_fabric_vrfs, \
    add_fabric_vnis, create_fabric, add_fabric_static_routes
import sys
from pprint import pprint
import auth_config


def main(fabName, auth):
    """
    Orchestrates a series of tests against the Hyperfabric API for fabric creation,
    node/connection management, and fabric deletion.
    """

    print("------------------------------------ Getting Information ------------------------------------")

    # Get a list of fabrics
    fabrics = get_fabrics(auth)
    if fabrics:
        print(f"Found {len(fabrics['fabrics'])} total fabrics")
    else:
        print("Failed to retrieve fabrics.")

    # Get all devices
    devices = get_devices(auth)
    if devices:
        print(f"Found {len(devices['devices'])} total devices")
    else:
        print("Failed to retrieve devices.")

    print("------------------------------------ Fabric Creation Test ------------------------------------")

    # Create a new fabric
    input("Press any key to test creation of fabric")  # Pause
    fabric_id = create_fabric(
        auth,
        fabric_name=fabName,
        description="A test fabric",
        location="HQ Location",
        address="Test Address",
        city="Test City",
        country="US",
        labels=["test", "example"],
    )

    if fabric_id:
        fabric = fabric_id["fabrics"][0]["fabricId"]
        print(f"Successfully created fabric with UUID: {fabric}")
    else:
        print("Fabric Creation Failed")
        sys.exit(1)

    print("------------------------------------ Adding Nodes Test ------------------------------------")

    # Add nodes to our fabric
    nodes = [
        {"name": "node-leaf1", "description": "LEAF-1", "enabled": True, "serialNumber": "RESTAA2001", "modelName": "HF6100-60L4D", "roles": ["LEAF"], "labels": ["sdk_test"]},
        {"name": "node-leaf2", "description": "LEAF-2", "enabled": True, "serialNumber": "RESTAA2002", "modelName": "HF6100-60L4D", "roles": ["LEAF"]},
        {"name": "node-spine1", "description": "SPINE-1", "enabled": True, "serialNumber": "RESTAA2003", "modelName": "HF6100-32D", "roles": ["SPINE"]},
        {"name": "node-spine2", "description": "SPINE-2", "enabled": True, "serialNumber": "RESTAA2004", "modelName": "HF6100-32D", "roles": ["SPINE"]},
    ]

    addnodes = add_fabric_nodes(auth, fabName, nodes)
    if addnodes:
        print(f"Added nodes: {addnodes}")
    else:
        print("Failed to add nodes")

    print("------------------------------------ Commit Changes Test ------------------------------------")

    # Commit changes
    commit = commit_fabric_candidate(auth, fabric_name=fabName, name="default", comments="API SDK commit - nodes")
    print(f"Commit response: {commit}")

    print("------------------------------------ Get Single Fabric Node Test ------------------------------------")

    # Get a single fabric node
    this_node = get_fabric_node(auth, fabName, "node-leaf2")
    if this_node:
        print(f"Get single node result: {this_node}")
        leaf2_uuid = this_node['nodeId']
    else:
        print("Failed to retrieve a single fabric node")
        leaf2_uuid = None  # Handle the case where node retrieval fails (important!)

    print("------------------------------------ Fabric GET Tests ------------------------------------")

    # Test unique fabric GET call with UUID
    this_fabric = get_fabric(auth, fabric)
    if this_fabric:
        print("Fabric GET UUID test passed")
    else:
        print("Fabric GET UUID test failed")

    # Test unique fabric GET call with name
    this_fabric = get_fabric(auth, fabName)
    if this_fabric:
        print("Fabric GET name test passed")
    else:
        print("Fabric GET name test failed")

    print("------------------------------------ Fabric Update Test ------------------------------------")

    # Update the fabric
    input("Press any key to test update of fabric")  # Pause
    fabUpdate = {
        "name": fabName,
        "description": "Updated fabric description",
        "location": "Updated Location",
        "address": "Updated Address",
        "city": "Updated City",
        "country": "BE",
        "labels": ["label1", "label2"],
        "topology": "SPINE_LEAF",
    }
    update = update_fabric(auth, fabName, fabUpdate)
    if update:
        pprint(update)
    else:
        print("Update failed")

    print("------------------------------------ Add Fabric Connections Test ------------------------------------")

    # Add fabric connections
    conns = [
        {"local": {"portName": "Ethernet1_1", "nodeName": "node-leaf1"}, "remote": {"portName": "Ethernet1_1", "nodeName": "node-spine1"}},
        {"local": {"portName": "Ethernet1_2", "nodeName": "node-leaf1"}, "remote": {"portName": "Ethernet1_1", "nodeName": "node-spine2"}},
        {"local": {"portName": "Ethernet1_1", "nodeName": "node-leaf2"}, "remote": {"portName": "Ethernet1_2", "nodeName": "node-spine1"}},
        {"local": {"portName": "Ethernet1_2", "nodeName": "node-leaf2"}, "remote": {"portName": "Ethernet1_2", "nodeName": "node-spine2"}},
    ]

    # Add connections to the fabric
    input("Press any key to add connections to fabric")  # Pause
    add_conns = add_fabric_connections(auth, fabName, conns)
    if add_conns:
        pprint(add_conns)
    else:
        print("Add connections to fabric: failed")

    print("------------------------------------ Add Management Ports Test ------------------------------------")

    # Add management information to nodes
    mgmt_info = [
        {
            "name": "eth0",
            "ipv4Address": "10.1.1.200/24",
            "ipv4Gateway": "10.1.1.1",
            "ipv6Address": "2a02:1243:5687:0:9c09:2c7a:7c78:9ffc/64",
            "ipv6Gateway": "2a02:1243:5687:0:8d91:ba6b:b24d:9b41",
            "dnsAddresses": ["8.8.8.8", "10.48.168.15"],
            "proxyAddress": "https://proxy.esl.cisco.com:8080",
            "proxyUsername": "admin",
            "proxyPassword": "cisco",
            "enabled": True,
            "cloudUrls": ["https://hypershield.cisco.com"],
            "setProxyPassword": True,
            "noProxy": ["10.0.0.0/8", "172.0.0.0/8", "cisco.com", "localhost", "127.0.0.1", ".local"],
        }
    ]
    add_mgmt = add_management_ports(auth, fabName, "node-leaf1", mgmt_info)
    if add_mgmt:
        print(f"Added mgmt info to node-leaf1: {add_mgmt}")
    else:
        print("Could not update mgmt info to node-leaf1")

    print("------------------------------------ Commit Changes After Mgmt Port Config ------------------------------------")

    # Commit changes
    commit = commit_fabric_candidate(auth, fabric_name=fabName, name="default", comments="API SDK commit - mgmt info")
    print(f"Commit response: {commit}")

    print("------------------------------------ Configure Ports Test ------------------------------------")

    # Configure ports
    port_config = [
        {"name": "Ethernet1_1", "enabled": True, "roles": ["FABRIC_PORT"]},
        {"name": "Ethernet1_2", "enabled": True, "roles": ["FABRIC_PORT"]},
        {"name": "Ethernet1_5", "enabled": True, "roles": ["HOST_PORT"]},
        {"name": "Ethernet1_6", "enabled": True, "roles": ["HOST_PORT"]},
    ]

    all_successful = True  # Use a flag to track success
    for node in ["node-leaf1", "node-leaf2"]:
        port_info = set_ports(auth, fabName, node, port_config)
        if port_info:
            print(f"Configured ports on {node}: {port_info}")
        else:
            print(f"Failed to configure ports on {node}")
            all_successful = False  # Set the flag to False

    #Print the Success or Fail message
    if all_successful:
        print("Configuring Ports - Sucessfully Concluded")
    else:
        print("Configuring Ports - Errors Encountered")

    print("------------------------------------ Commit Changes After Port Config ------------------------------------")

    # Commit changes
    commit = commit_fabric_candidate(auth, fabric_name=fabName, name="default", comments="API SDK commit - port config")
    print(f"Commit response: {commit}")

    print("------------------------------------ Add VRFs and VNIs Test ------------------------------------")

    # Create VRF and VNIs
    print("Adding VRF and VNI items")
    vrfs = [
        {"name": "Vrf-main", "enabled": True},
        {"name": "Vrf-secondary", "description": "VRF for non-prod", "labels": ["non-prod", "VRF for testing"], "enabled": True},
        {"name": "Vrf-extranet", "enabled": True},
    ]
    vrf_info = add_fabric_vrfs(auth, fabName, vrfs)
    if vrf_info:
        print(f"Configured following VRFs: {vrf_info}")
    else:
        print("Failed to add VRFs to fabric")

    vnis = [
        {
            "name": "vni-frontend",
            "description": "VNI for Web FE",
            "vrfId": "Vrf-main",
            "vni": "21001",
            "enabled": True,
            "svis": [{"enabled": True, "ipv4Addresses": ["10.1.1.1/24"], "ipv6Addresses": ["2001:db8::1/64"]}],
            "members": [
                {"vlanId": "1001", "untagged": False, "port": {"nodeId": "*", "portName": "Ethernet1_5"}},
                {"vlanId": "2001", "untagged": False, "port": {"nodeId": leaf2_uuid, "portName": "Ethernet1_6"}},
            ],
            "labels": ["Web FE"],
        },
        {
            "name": "vni-backend",
            "vni": "21002",
            "enabled": True,
            "description": "VNI for Backend - no SVI",
            "vrfId": "Vrf-main",
        },
    ]
    vni_info = add_fabric_vnis(auth, fabName, vnis)
    if vni_info:
        print(f"Added VNI config {vni_info}")
    else:
        print("Failed to add VNI config")
    
    print("------------------------------------ Commit Changes Test ------------------------------------")

    # Commit changes
    commit = commit_fabric_candidate(auth, fabric_name=fabName, name="default", comments="API SDK commit - VRFs and VNIs")
    print(f"Commit response: {commit}")


    print("------------------------------------ Adding Static Routes ------------------------------------")

    static_routes = [
        {
          "name": "Vrf-main",
          "enabled": True,
          "routes": [
            {
              "prefix": "10.88.88.0/24",
              "nextHop": "10.1.1.254",
              "discard": False
            },
            {
              "prefix": "10.99.99.0/24",
              "preference": 10,
              "nextHop" : "10.1.1.254",
              "discard": False
            }
          ]
        }
       ]
    routes = add_fabric_static_routes(auth, fabName, "Vrf-main", static_routes)
    if routes:
        print(f"Added static routes {routes}")
    else:
        print("Failed to add static routes")

    print("------------------------------------ Fabric Deletion Test ------------------------------------")

    # Delete the fabric
    input("Press any key to test deletion of fabric")  # Pause
    deletion = delete_fabric(auth, fabName)
    print(f"Deletion response code: {deletion}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <fabric_name>")
        sys.exit(1)

    fabName = sys.argv[1]
    auth = auth_config.get_api_headers()
    main(fabName, auth)
