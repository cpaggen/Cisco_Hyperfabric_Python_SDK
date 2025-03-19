```markdown
# HyperFabric SDK Documentation

This document provides a guide to using the HyperFabric SDK.  The SDK allows you to interact with the HyperFabric API to manage fabrics, nodes, connections, and more.

## Authentication

All API requests require authentication using a bearer token. Simply export that token as environment variable AUTH_TOKEN.
Import `auth_config` in your client code.
## API Functions

### Bearer Tokens

#### `get_bearer_tokens(auth, include_metadata=False)`

Retrieves a list of bearer tokens.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `include_metadata` (bool, optional): Include metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the list of bearer tokens, or `None` on error.

#### `create_bearer_token(auth, name, description, scope, notBefore, notAfter)`

Creates a new bearer token.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `name` (str): The user-provided name for the token.
*   `description` (str): A description for the token.
*   `scope` (str): The permission scope of the token.
*   `notBefore` (str): Sets the time at which the token can be used (ISO 8601 format, e.g., "2024-01-01T00:00:00Z").
*   `notAfter` (str): Sets the time after which the token cannot be used (ISO 8601 format, e.g., "2024-12-31T23:59:59Z").

**Returns:**

*   `dict`: JSON response of the new created token, or `None` on error.

#### `get_bearer_token(auth, tokenId, include_metadata=False)`

Retrieves a specific bearer token by its ID.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `tokenId` (str): The ID of the bearer token.
*   `include_metadata` (bool, optional): Include metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the bearer token, or `None` on error.

#### `delete_bearer_token(auth, tokenId)`

Deletes a specific bearer token by its ID.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `tokenId` (str): The ID of the bearer token to delete.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

### Devices

#### `get_devices(auth)`

Retrieves a list of devices.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.

**Returns:**

*   `dict`: JSON response containing the list of devices, or `None` on error.

### Fabrics

#### `get_fabrics(auth, fabricId=None, candidate=None, include_metadata=False)`

Retrieves a list of fabrics.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str, optional): Filter by one or more fabric IDs or names. Defaults to `None`.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `include_metadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the list of fabrics, or `None` on error.

#### `create_fabric(auth, fabric_name, description, location, address, city, country, labels, topology=None)`

Creates a new fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabric_name` (str): The name of the fabric. Must be unique and DNS compliant.
*   `description` (str): A description of the fabric.
*   `location` (str): A location identifier.
*   `address` (str): The street address.
*   `city` (str): The city.
*   `country` (str): The two-letter country code.
*   `labels` (list, optional): A list of labels for the fabric. Defaults to `[]`.
*   `topology` (str, optional): The fabric topology (MESH or SPINE_LEAF). Defaults to `None`.

**Returns:**

*   `dict`: JSON response containing the created fabric information, or `None` on error.

#### `get_fabric(auth, fabricId, candidate=None, include_metadata=False)`

Retrieves a specific fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `include_metadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the fabric information, or `None` on error.

#### `update_fabric(auth, fabricId, payload)`

Updates a specific fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `payload` (dict): A JSON payload containing the updated fabric properties.  See the API documentation for allowed properties.

**Example Payload:**

```json
{
  "name": "updated-fabric-name",
  "description": "Updated fabric description",
  "location": "Updated Location",
  "address": "Updated Address",
  "city": "Updated City",
  "country": "US",
  "labels": ["label1", "label2"],
  "topology": "SPINE_LEAF"
}
```

**Returns:**

*   `dict`: JSON response containing the updated fabric information, or `None` on error.

#### `delete_fabric(auth, fabricId)`

Deletes a specific fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric to delete.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

### Fabric Candidates

#### `get_fabric_candidates(auth, fabricId, name=None, txnId=None, needInactive=None, needReviews=None, needEvents=None, startTime=None, endTime=None)`

Retrieves a list of candidate configurations for a specific fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str, optional): The candidate configuration name. Defaults to `None`.
*   `txnId` (int, optional): The transaction sequence number. Defaults to `None`.
*   `needInactive` (bool, optional): Include committed/reverted candidate configurations. Defaults to `None`.
*   `needReviews` (bool, optional): Include the list of reviews. Defaults to `None`.
*   `needEvents` (bool, optional): Include the list of activity events. Defaults to `None`.
*   `startTime` (str, optional): Start value of time range (ISO 8601 format, e.g., "2023-01-01T00:00:00Z"). Defaults to `None`.
*   `endTime` (str, optional): End value of the time range (ISO 8601 format, e.g., "2023-12-31T23:59:59Z"). Defaults to `None`.

**Returns:**

*   `dict`: JSON response containing the list of candidate configurations, or `None` on error.

#### `get_fabric_candidate(auth, fabricId, name, needInactive=None, needReviews=None, needEvents=None)`

Retrieves a specific candidate configuration for a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str): The name of the candidate configuration.
*   `needInactive` (bool, optional): Include committed/reverted candidate configuration. Defaults to `None`.
*   `needReviews` (bool, optional): Include the list of reviews. Defaults to `None`.
*   `needEvents` (bool, optional): Include the list of activity events. Defaults to `None`.

**Returns:**

*   `dict`: JSON response containing the candidate configuration, or `None` on error.

#### `review_fabric_candidate(auth, fabricId, name, comments)`

Adds a comment (review) to a specific candidate configuration.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str): The name of the candidate configuration.
*   `comments` (str): The review comments to add.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `commit_fabric_candidate(auth, fabricId, name, comments)`

Commits a specific candidate configuration to the running configuration of a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str): The name of the candidate configuration.
*   `comments` (str): The commit comments.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `revert_fabric_candidate(auth, fabricId, name)`

Discards (reverts) a specific candidate configuration.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `name` (str): The name of the candidate configuration.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

### Fabric Connections

#### `get_fabric_connections(auth, fabricId, candidate=None)`

Retrieves a list of connections within a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `add_fabric_connections(auth, fabricId, connections)`

Adds one or more connections to a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `connections` (list): A list of connections to add. Each connection object must have a `local` and `remote` property with `portName` and `nodeName`.

**Example:**

```json
[
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
```

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `set_fabric_connections(auth, fabricId, connections)`

Replaces all connections in a fabric with a new set of connections.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `connections` (list): A list of connections to set. Each connection object must have a `local` and `remote` property with `portName` and `nodeName`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `delete_fabric_connections(auth, fabricId)`

Deletes all connections in the fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.

#### `get_fabric_connection(auth, fabricId, connectionId, candidate=None)`

Retrieves a specific connection by ID.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `connectionId` (str): The ID of the connection.
*   `candidate` (str, optional): Candidate configuration name. Defaults to `None`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `delete_fabric_connection(auth, fabricId, connectionId)`

Deletes a specific connection.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `connectionId` (str): The ID of the connection.

### Fabric Nodes

#### `get_fabric_nodes(auth, fabricId, candidate=None, includeMetadata=None)`

Retrieves a list of nodes within a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `add_fabric_nodes(auth, fabricId, nodes)`

Adds one or more nodes to a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodes` (list): A list of node objects to add.

**Example:**

```json
[
  {
   "name": "node-leaf0",
   "description": "example fabric node leaf zero",
   "enabled": true,
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
   "enabled": true,
   "serialNumber": "RESTAA2001",
   "modelName": "HF6100-32D"
  }
]
```

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `get_fabric_node(auth, fabricId, nodeId, candidate=None, includeMetadata=None)`

Retrieves a specific node by ID or name.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `update_fabric_node(auth, fabricId, nodeId, payload)`

Updates a specific node.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `payload` (dict): A JSON payload containing the updated node properties.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `delete_fabric_node(auth, fabricId, nodeId)`

Deletes a specific node.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

#### `bind_device(auth, fabricId, nodeId, deviceId)`

Binds a device to a specific node.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `deviceId` (str): The serial of the device.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `unbind_device(auth, fabricId, nodeId)`

Unbinds a device from a specific node.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.

**Returns:**

*   `int`: HTTP status code, or `None` on error.

### Fabric Node Management Ports

#### `get_management_ports(auth, fabricId, nodeId, candidate=None, includeMetadata=None)`

Retrieves a list of management ports for a specific node.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response containing the list of management ports, or `None` on error.

#### `add_management_ports(auth, fabricId, nodeId, ports)`

Creates or updates one or more ManagementPorts for a fabric node.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The node ID or name from which a device is bound.
*   `ports` (list): A list of one or more ports to update.

**Example:**

```json
[
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
  "enabled": true,
  "cloudUrls": [
   "https://a.b.com"
  ],
  "setProxyPassword": true,
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
```

**Returns:**

*   `dict`: JSON response.

#### `get_management_port(auth, fabricId, nodeId, id, candidate=None, includeMetadata=None)`

Retrieves information on the management port specified.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The node ID or name from which a device is bound.
*   `id` (str): ID of the port

**Returns:**

*   `dict`: JSON response.

#### `update_management_port(auth, fabricId, nodeId, id, payload)`

Updates the settings on a management port

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The node ID or name from which a device is bound.
*   `id` (str): The ID of the management port to update.
*   `payload` (dict): The JSON payload with updated port properties.

**Returns:**

*   `dict`: JSON response.

### Fabric Node Ports

#### `get_ports(auth, fabricId, nodeId, candidate=None, includeMetadata=None)`

Retrieves a list of ports for a specific node.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `set_ports(auth, fabricId, nodeId, ports)`

Replaces all ports for a specific node.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `ports` (list): A list of port objects to set.

**Example:**

```json
[
  {
   "name": "Ethernet1_5",
   "enabled": true,
   "roles": [
    "HOST_PORT"
   ]
  },
  {
   "name": "Ethernet1_6",
   "enabled": true,
   "roles": [
    "HOST_PORT"
   ]
  },
  {
   "name": "Ethernet1_7",
   "enabled": true,
   "roles": [
    "HOST_PORT"
   ]
  },
  {
   "name": "Ethernet1_8",
   "enabled": true,
   "roles": [
    "HOST_PORT"
   ]
  }
]
```

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `get_port(auth, fabricId, nodeId, portId, candidate=None, includeMetadata=None)`

Retrieves a specific port by its ID.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `portId` (str): The ID of the port.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `update_port(auth, fabricId, nodeId, portId, payload)`

Updates a specific port.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `portId` (str): The ID of the port.
*   `payload` (dict): A JSON payload containing the updated port properties.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `reset_port(auth, fabricId, nodeId, portId)`

Resets a specific port.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `nodeId` (str): The ID or name of the node.
*   `portId` (str): The ID of the port.

### Fabric VNIs

#### `get_fabric_vnis(auth, fabricId, candidate=None, includeMetadata=None)`

Retrieves a list of VNIs within a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `add_fabric_vnis(auth, fabricId, vnis)`

Adds one or more VNIs to a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `vnis` (list): A list of VNI objects to add.

**Example:**

```json
[
  {
    "name": "vni-example-1001",
    "description": "Example VNI",
    "vni": 1001,
    "vrfId": "1234-4567-7890-abcd",
    "svis": [
        {
            "enabled": true,
            "ipv4Addresses": ["10.1.1.1/24"],
            "ipv6Addresses": ["2001:db8::1/64"]
        }
    ],
    "labels": ["VLAN1001"]
  },
  {
    "name": "vni-example-1002",
    "description": "Example VNI 2, no SVI",
    "vni": 1002,
    "vrfId": "1234-4567-7890-abcd"
  }
]
```

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `get_fabric_vni(auth, fabricId, vniId, candidate=None, includeMetadata=None)`

Retrieves a specific VNI by ID or name.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `vniId` (str): The ID or name of the VNI.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `update_fabric_vni(auth, fabricId, vniId, payload)`

Updates a specific VNI.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `vniId` (str): The ID or name of the VNI.
*   `payload` (dict): A JSON payload containing the updated VNI properties.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `delete_fabric_vni(auth, fabricId, vniId)`

Deletes a VNI given its ID.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `vniId` (str): The ID of the VNI to delete.

#### `get_fabric_vni_members(auth, fabricId, vniId, candidate=None, includeMetadata=None)`

Retrieves a list of vni members from a fabric.

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `vniId` (str): The ID or name of the vni.
*   `candidate` (str, optional): The candidate configuration name. Defaults to `None`.
*   `includeMetadata` (bool, optional): Include object metadata in the response. Defaults to `False`.

**Returns:**

*   `dict`: JSON response, or `None` on error.

#### `add_fabric_vni_members(auth, fabricId, vniId, payload)`

Adds one or more vni member to a fabric vni object

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `vniId` (str): The ID or name of the vni.
*   `payload` (list): A list of members to add to the vni.

#### `get_fabric_vni_member(auth, fabricId, vniId, memberId, candidate=None, includeMetadata=None)`

Gets details for a vni member

**Args:**

*   `auth` (dict): A dictionary containing the `Authorization` header with the bearer token.
*   `fabricId` (str): The ID or name of the fabric.
*   `vniId` (str): The ID or name of the vni.
*   `memberId
