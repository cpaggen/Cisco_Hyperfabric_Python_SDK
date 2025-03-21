# Python SDK Documentation

This document provides a detailed description of the Python SDK functions.

## /bearerTokens

### `get_bearer_tokens(auth, include_metadata=False)`

Retrieves a list of bearer tokens.

**Args:**

*   `auth`: Authentication credentials.
*   `include_metadata` (bool, optional): Include metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the list of bearer tokens, or `None` on error.

**Example:**
```python
tokens = get_bearer_tokens(auth, include_metadata=True)
if tokens:
    print(tokens)
else:
    print("Error retrieving bearer tokens.")
```

### `create_bearer_token(auth, name, description, scope, notBefore, notAfter)`

Creates a new bearer token.

**Args:**

*   `auth`: Authentication credentials.
*   `name` (str): The user provided name for the token.
*   `description` (str): A description for the token.
*   `scope` (str): The permission scope of the token.
*   `notBefore` (str): Sets the time at which the token can be used.
*   `notAfter` (str): Sets the time after which the token cannot be used.

**Returns:**

*   `dict`: JSON response of the new created token or `None` on error.

**Example:**
```python
token = create_bearer_token(auth, "my-token", "A test token", "read", "2023-01-01T00:00:00Z", "2024-01-01T00:00:00Z")
if token:
    print(token)
else:
    print("Error creating bearer token.")
```

## /bearerTokens/{tokenId}

### `get_bearer_token(auth, tokenId, include_metadata=False)`

Retrieves a specific bearer token by its ID.

**Args:**

*   `auth`: Authentication credentials.
*   `tokenId` (str): The ID of the bearer token.
*   `include_metadata` (bool, optional): Include metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the bearer token, or `None` on error.

**Example:**
```python
token = get_bearer_token(auth, "token123", include_metadata=True)
if token:
    print(token)
else:
    print("Error retrieving bearer token.")
```

### `delete_bearer_token(auth, tokenId)`

Deletes a specific bearer token by its ID.

**Args:**

*   `auth`: Authentication credentials.
*   `tokenId` (str): The ID of the bearer token to delete.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

**Example:**
```python
status_code = delete_bearer_token(auth, "token123")
if status_code:
    print(f"Deletion status: {status_code}")
else:
    print("Error deleting bearer token.")
```

## /devices

### `get_devices(auth)`

Retrieves a list of devices.

**Args:**

*   `auth`: Authentication credentials.

**Returns:**

*   `dict`: JSON response containing the list of devices, or `None` on error.

**Example:**
```python
devices = get_devices(auth)
if devices:
    print(devices)
else:
    print("Error retrieving devices.")
```

## /fabrics

### `get_fabrics(auth, fabricId=None, candidate=None, include_metadata=False)`

Retrieves a list of fabrics.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str, optional): Filter by one or more fabric IDs and/or names. Defaults to `None`.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `include_metadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the list of fabrics, or `None` on error.

**Example:**
```python
fabrics = get_fabrics(auth, fabricId="my-fabric", candidate="candidate1", include_metadata=True)
if fabrics:
    print(fabrics)
else:
    print("Error retrieving fabrics.")
```

### `create_fabric(auth, fabric_name, description, location, address, city, country, labels, topology=None)`

Creates a new fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabric_name` (str): The name of the fabric.  Must be unique and DNS compliant.
*   `description` (str): A description of the fabric.
*   `location` (str): A location identifier.
*   `address` (str): The street address.
*   `city` (str): The city.
*   `country` (str): The two-letter country code.
*   `labels` (list, optional): A list of labels for the fabric. Defaults to `[]`.
*   `topology` (str, optional): The fabric topology (MESH or SPINE_LEAF). Defaults to None.

**Returns:**

*   `dict`: JSON response containing the created fabric information, or `None` on error.

**Example:**
```python
fabric = create_fabric(auth, "my-new-fabric", "A test fabric", "My Location", "123 Main St", "Anytown", "US", ["label1", "label2"], topology="SPINE_LEAF")
if fabric:
    print(fabric)
else:
    print("Error creating fabric.")
```

## /fabrics/{fabricId}

### `get_fabric(auth, fabricId, candidate=None, include_metadata=False)`

Retrieves a specific fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `include_metadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the fabric information, or `None` on error.

**Example:**
```python
fabric = get_fabric(auth, "my-fabric", candidate="candidate1", include_metadata=True)
if fabric:
    print(fabric)
else:
    print("Error retrieving fabric.")
```

### `update_fabric(auth, fabricId, payload)`

Updates a specific fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `payload` (dict): A JSON payload containing the updated fabric properties. See schema for possible properties.

**Returns:**

*   `dict`: JSON response containing the updated fabric information, or `None` on error.

**Example:**

```python
payload = {
  "name": "updated-fabric-name",
  "description": "Updated fabric description",
  "location": "Updated Location",
  "address": "Updated Address",
  "city": "Updated City",
  "country": "US",
  "labels": ["label1", "label2"],
  "topology": "SPINE_LEAF"
}

fabric = update_fabric(auth, "my-fabric", payload)
if fabric:
    print(fabric)
else:
    print("Error updating fabric.")
```

### `delete_fabric(auth, fabricId)`

Deletes a specific fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric to delete.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

**Example:**
```python
status_code = delete_fabric(auth, "my-fabric")
if status_code:
    print(f"Deletion status: {status_code}")
else:
    print("Error deleting fabric.")
```

## /fabrics/{fabricId}/candidates

### `get_fabric_candidates(auth, fabricId, name=None, txnId=None, needInactive=None, needReviews=None, needEvents=None, startTime=None, endTime=None)`

Retrieves a list of candidate configurations for a specific fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str, optional): The candidate configuration name. Defaults to `None`.
*   `txnId` (int, optional): The transaction sequence number. Defaults to `None`.
*   `needInactive` (bool, optional): Include committed/reverted candidate configurations. Defaults to `None`.
*   `needReviews` (bool, optional): Include the list of reviews. Defaults to `None`.
*   `needEvents` (bool, optional): Include the list of activity events. Defaults to `None`.
*   `startTime` (str, optional): Start value of time range. Defaults to `None`.
*   `endTime` (str, optional): End value of the time range. Defaults to `None`.

**Returns:**

*   `dict`: JSON response containing the list of candidate configurations, or `None` on error.

**Example:**
```python
candidates = get_fabric_candidates(auth, "my-fabric", name="candidate1", needInactive=True)
if candidates:
    print(candidates)
else:
    print("Error retrieving fabric candidates.")
```

## /fabrics/{fabricId}/candidates/{name}

### `get_fabric_candidate(auth, fabricId, name, needInactive=None, needReviews=None, needEvents=None)`

Retrieves a specific candidate configuration for a fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str): The name of the candidate configuration.
*   `needInactive` (bool, optional): Include committed/reverted candidate configuration.  Defaults to `None`.
*   `needReviews` (bool, optional): Include the list of reviews. Defaults to `None`.
*   `needEvents` (bool, optional): Include the list of activity events. Defaults to `None`.

**Returns:**

*   `dict`: JSON response containing the candidate configuration, or `None` on error.

**Example:**
```python
candidate = get_fabric_candidate(auth, "my-fabric", "candidate1", needInactive=True)
if candidate:
    print(candidate)
else:
    print("Error retrieving fabric candidate.")
```

### `review_fabric_candidate(auth, fabricId, name, comments)`

Adds a comment (review) to a specific candidate configuration.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str): The name of the candidate configuration.
*   `comments` (str): The review comments to add.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
result = review_fabric_candidate(auth, "my-fabric", "candidate1", "This looks good!")
if result:
    print(result)
else:
    print("Error reviewing fabric candidate.")
```

### `commit_fabric_candidate(auth, fabric_name, name, comments)`

Commits a specific candidate configuration to the running configuration of a fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabric_name` (str): The ID or name of the fabric.
*   `name` (str): The name of the candidate configuration.
*   `comments` (str): The commit comments.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
result = commit_fabric_candidate(auth, "my-fabric", "candidate1", "Committing changes to production.")
if result:
    print(result)
else:
    print("Error committing fabric candidate.")
```

### `revert_fabric_candidate(auth, fabricId, name)`

Discards (reverts) a specific candidate configuration.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str): The name of the candidate configuration.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

**Example:**
```python
status_code = revert_fabric_candidate(auth, "my-fabric", "candidate1")
if status_code:
    print(f"Revert status: {status_code}")
else:
    print("Error reverting fabric candidate.")
```

## /fabrics/{fabricId}/connections

### `get_fabric_connections(auth, fabricId, candidate=None)`

Retrieves a list of connections within a fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
connections = get_fabric_connections(auth, "my-fabric", candidate="candidate1")
if connections:
    print(connections)
else:
    print("Error retrieving fabric connections.")
```

### `add_fabric_connections(auth, fabricId, connections)`

Adds one or more connections to a fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `connections` (list): A list of connections to add.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**

```python
connections = [
  {
    "local": {
      "portName": "Ethernet1_19",
      "nodeName": "node-leaf0"
    },
    "remote": {
      "portName": "Ethernet1_19",
      "nodeName": "node-spine0"
    }
  },
  {
    "local": {
      "portName": "Ethernet1_22",
      "nodeName": "node-leaf1"
    },
    "remote": {
      "portName": "Ethernet1_22",
      "nodeName": "node-spine0"
    }
  }
]

result = add_fabric_connections(auth, "my-fabric", connections)
if result:
    print(result)
else:
    print("Error adding fabric connections.")
```

### `set_fabric_connections(auth, fabricId, connections)`

Replaces all connections in a fabric with a new set of connections.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `connections` (list): A list of connections to set.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**

```python
connections = [
  {
    "local": {
      "portName": "Ethernet1_19",
      "nodeName": "node-leaf0"
    },
    "remote": {
      "portName": "Ethernet1_19",
      "nodeName": "node-spine0"
    }
  }
]

result = set_fabric_connections(auth, "my-fabric", connections)
if result:
    print(result)
else:
    print("Error setting fabric connections.")
```

### `delete_fabric_connections(auth, fabricId)`

Deletes all connections in the fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.

**Returns:**
    None
**Example:**
```python
delete_fabric_connections(auth, "my-fabric")
print("All fabric connections deleted")
```

## /fabrics/{fabricId}/connections/{connectionId}

### `get_fabric_connection(auth, fabricId, connectionId, candidate=None)`

Retrieves a specific connection by ID.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `connectionId` (str): The ID of the connection.
*   `candidate` (str, optional):  Candidate configuration name. Defaults to `None`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
connection = get_fabric_connection(auth, "my-fabric", "conn123", candidate="candidate1")
if connection:
    print(connection)
else:
    print("Error retrieving fabric connection.")
```

### `delete_fabric_connection(auth, fabricId, connectionId)`

Delete a specific connection.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `connectionId` (str): The ID of the connection.

**Returns:**
    None
**Example:**
```python
delete_fabric_connection(auth, "my-fabric", "conn123")
print("Fabric connection deleted")
```

## /fabrics/{fabricId}/nodes

### `get_fabric_nodes(auth, fabricId, candidate=None, includeMetadata=None)`

Retrieves a list of nodes within a fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
nodes = get_fabric_nodes(auth, "my-fabric", candidate="candidate1", includeMetadata=True)
if nodes:
    print(nodes)
else:
    print("Error retrieving fabric nodes.")
```

### `add_fabric_nodes(auth, fabric_name, nodes)`

Adds one or more nodes to a fabric.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodes` (list): A list of node objects to add.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**

```python
nodes = [
  {
   "name": "node-leaf0",
   "description": "example fabric node leaf zero",
   "enabled": True,
   "serialNumber": "RESTAA2000",
   "modelName": "HF6100-60L4D",
   "roles": [
    "LEAF"
   ],
   "labels": [
    "TAG_ONE_ZERO"
   ]
  },
  {
   "name": "node-leaf1",
   "description": "example fabric node leaf one",
   "enabled": True,
   "serialNumber": "RESTAA2001",
   "modelName": "HF6100-32D"
  },
 ]

result = add_fabric_nodes(auth, "my-fabric", nodes)
if result:
    print(result)
else:
    print("Error adding fabric nodes.")
```

## /fabrics/{fabricId}/nodes/{nodeId}

### `get_fabric_node(auth, fabricId, nodeId, candidate=None, includeMetadata=None)`

Retrieves a specific node by ID or name.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
node = get_fabric_node(auth, "my-fabric", "node123", candidate="candidate1", includeMetadata=True)
if node:
    print(node)
else:
    print("Error retrieving fabric node.")
```

### `update_fabric_node(auth, fabricId, nodeId, payload)`

Updates a specific node.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `payload` (dict): A JSON payload containing the updated node properties.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
payload = {"description": "Updated node description", "enabled": False}
result = update_fabric_node(auth, "my-fabric", "node123", payload)
if result:
    print(result)
else:
    print("Error updating fabric node.")
```

### `delete_fabric_node(auth, fabricId, nodeId)`

Deletes a specific node.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

**Example:**
```python
status_code = delete_fabric_node(auth, "my-fabric", "node123")
if status_code:
    print(f"Deletion status: {status_code}")
else:
    print("Error deleting fabric node.")
```
## /fabrics/{fabricId}/nodes/{nodeId}/devices/{deviceId}
### `bind_device(auth, fabricId, nodeId, deviceId)`

Binds a device to a specific node
 **Args:**
    *   `auth`: Authentication credentials.
    *   `fabricId` (str): The ID or name of the fabric.
    *   `nodeId` (str): The ID or name of the node.
    *   `deviceId` (str): The serial of the device.

**Returns:**
    * `dict`: JSON response or None on Error

**Example:**
```python
result = bind_device(auth, "my-fabric", "node123","H888777234")
if result:
    print(result)
else:
    print("Error binding device to node.")
```

## /fabrics/{fabricId}/nodes/{nodeId}/devices
### `unbind_device(auth, fabricId, nodeId)`

Unbinds a device from a specific node
**Args:**
    *   `auth`: Authentication credentials.
    *   `fabricId` (str): The ID or name of the fabric.
    *   `nodeId` (str): The ID or name of the node.

**Returns:**
    *  `Int`: Response Code or None on Error

**Example:**
```python
result = unbind_device(auth, "my-fabric", "node123")
if result:
    print(result)
else:
    print("Error unbinding device to node.")
```
## /fabrics/{fabricId}/nodes/{nodeId}/managementPorts
### `get_management_ports(auth, fabricId, nodeId, candidate=None, includeMetadata=None)`

Retrieves a list of management ports for a specific node.
**Args:**
    *   `auth`: Authentication credentials.
    *   `fabricId` (str): The ID or name of the fabric.
    *   `nodeId` (str): The ID or name of the node.
    *   `candidate` (str, optional): The candidate configuration name. Defaults to None.
    *   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to False.
**Returns:**
    * `dict`: JSON response containing the list of management ports, or None on error.
**Example:**
```python
management_ports = get_management_ports(auth, "my-fabric", "node123", candidate="candidate1", includeMetadata=True)
if management_ports:
    print(management_ports)
else:
    print("Error retrieving fabric management ports.")
```
### `add_management_ports(auth, fabricId, nodeId, ports)`

Creates or updates one or more ManagementPorts for a fabric node

**Args:**
    *   `auth`: Authentication credentials.
    *   `fabricId` (str): The ID or name of the fabric.
    *   `nodeId` (str): The node id or name from which a device is bound.
    *   `ports` (list): A list of one or more ports to update.
**Returns:**
    * `dict`: JSON response
**Example:**
```python
ports = [
                 {
                  "name": "eth0",
                  "ipv4Address": "10.1.1.250/31",
                  "ipv4Gateway": "10.1.1.251",
                  "ipv6Address": "2a02:1243:5687:0:9c09:2c7a:7c78:9ffc/64",
                  "ipv6Gateway": "2a02:1243:5687:0:8d91:ba6b:b24d:9b41",
                  "dnsAddresses": [
                   "8.8.8.8",
                   "8.8.4.4"
                  ],
                  "proxyAddress": "https://10.1.1.10:8080",
                  "proxyUsername": "admin",
                  "proxyPassword": "admin123",
                  "enabled": True,
                  "cloudUrls": [
                   "https://a.b.com"
                  ],
                  "setProxyPassword": True,
                  "noProxy": [
                   "10.0.0.0/8",
                   "68.0.0.0/8",
                   "72.0.0.0/8",
                   "172.0.0.0/8",
                   "172.0.0.0/8",
                   "173.0.0.0/8",
                   "cisco.com",
                   "localhost",
                   "127.0.0.1",
                   ".local"
                  ]
                 }
                ]

result = add_management_ports(auth, "my-fabric", "node123", ports)
if result:
    print(result)
else:
    print("Error add Management Ports.")
```

## /fabrics/{fabricId}/nodes/{nodeId}/managementPorts/{id}
### `get_management_port(auth, fabricId, nodeId, id, candidate=None, includeMetadata=None)`

Retrieves information on the management port specified

**Args:**
    *   `auth`: Authentication credentials.
    *   `fabricId` (str): The ID or name of the fabric.
    *   `nodeId` (str): The node id or name from which a device is bound.
    *   `id` (str): ID of the port

**Returns:**
    * `dict`: JSON response
**Example:**
```python
management_port = get_management_port(auth, "my-fabric", "node123","Mgmt123", candidate="candidate1", includeMetadata=True)
if management_port:
    print(management_port)
else:
    print("Error retrieving fabric management port.")
```
### `update_management_port(auth, fabricId, nodeId, id, payload)`

Updates the settings on a management port

**Args:**
    *   `auth`: Authentication credentials.
    *   `fabricId` (str): The ID or name of the fabric.
    *   `nodeId` (str): The node id or name from which a device is bound.
    *   `ports` (list): A list of one or more ports to update.

**Returns:**
    * `dict`: JSON response
**Example:**
```python
payload = {
                  "name": "eth0",
                  "ipv4Address": "10.1.1.250/31",
                  "ipv4Gateway": "10.1.1.251",
                  "ipv6Address": "2a02:1243:5687:0:9c09:2c7a:7c78:9ffc/64",
                  "ipv6Gateway": "2a02:1243:5687:0:8d91:ba6b:b24d:9b41",
                  "dnsAddresses": [
                   "8.8.8.8",
                   "8.8.4.4"
                  ],
                  "proxyAddress": "https://10.1.1.10:8080",
                  "proxyUsername": "admin",
                  "proxyPassword": "admin123",
                  "enabled": True,
                  "cloudUrls": [
                   "https://a.b.com"
                  ],
                  "setProxyPassword": True,
                  "noProxy": [
                   "10.0.0.0/8",
                   "68.0.0.0/8",
                   "72.0.0.0/8",
                   "172.0.0.0/8",
                   "172.0.0.0/8",
                   "173.0.0.0/8",
                   "cisco.com",
                   "localhost",
                   "127.0.0.1",
                   ".local"
                  ]
                 }

result = update_management_port(auth, "my-fabric", "node123", "Mgmt123", payload)
if result:
    print(result)
else:
    print("Error Update Management Ports.")
```

## /fabrics/{fabricId}/nodes/{nodeId}/ports

### `get_ports(auth, fabricId, nodeId, candidate=None, includeMetadata=None)`

Retrieves a list of ports for a specific node.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
ports = get_ports(auth, "my-fabric", "node123", candidate="candidate1", includeMetadata=True)
if ports:
    print(ports)
else:
    print("Error retrieving fabric ports.")
```

### `set_ports(auth, fabricId, nodeId, ports)`

Replaces all ports for a specific node.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `ports` (list): A list of port objects to set.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**

```python
ports = [
  {
   "name": "Ethernet1_5",
   "enabled": True,
   "roles": [
    "HOST_PORT"
   ]
  },
  {
   "name": "Ethernet1_6",
   "enabled": True,
   "roles": [
    "HOST_PORT"
   ]
  },
  {
   "name": "Ethernet1_7",
   "enabled": True,
   "roles": [
    "HOST_PORT"
   ]
  },
  {
   "name": "Ethernet1_8",
   "enabled": True,
   "roles": [
    "HOST_PORT"
   ]
  }
 ]

result = set_ports(auth, "my-fabric", "node123", ports)
if result:
    print(result)
else:
    print("Error setting fabric ports.")
```

## /fabrics/{fabricId}/nodes/{nodeId}/ports/{portId}

### `get_port(auth, fabricId, nodeId, portId, candidate=None, includeMetadata=None)`

Retrieves a specific port by its ID.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `portId` (str): The ID of the port.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
port = get_port(auth, "my-fabric", "node123", "eth1", candidate="candidate1", includeMetadata=True)
if port:
    print(port)
else:
    print("Error retrieving fabric port.")
```

### `update_port(auth, fabricId, nodeId, portId, payload)`

Updates a specific port.

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `portId` (str): The ID of the port.
*   `payload` (dict): A JSON payload containing the updated port properties.

**Returns:**

*   `dict`: JSON response, or `None` on error.

**Example:**
```python
payload = {"enabled": False, "description": "Test port"}
result = update_port(auth, "my-fabric", "node123", "eth1", payload)
if result:
    print(result)
else:
    print("Error updating fabric port.")
```

### `reset_port(auth, fabricId, nodeId, portId)`

Resets a specific port

**Args:**

*   `auth`: Authentication credentials.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node