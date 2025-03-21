<!-- markdownlint-disable -->

<a href="../hyperfabric_SDK.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `hyperfabric_SDK.py`




**Global Variables**
---------------
- **BASE_URL**

---

<a href="../hyperfabric_SDK.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_bearer_tokens`

```python
get_bearer_tokens(auth, include_metadata=False)
```

Retrieves a list of bearer tokens. 

**Args:**
 
 - <b>`include_metadata`</b> (bool, optional):  Include metadata in the response. Defaults to False. 

**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the list of bearer tokens, or None on error. 


---

<a href="../hyperfabric_SDK.py#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_bearer_token`

```python
create_bearer_token(auth, name, description, scope, notBefore, notAfter)
```

Creates a new bearer token. 

**Args:**
 
 - <b>`name`</b> (str):  The user provided name for the token. 
 - <b>`description`</b> (str):  A description for the token. 
 - <b>`scope`</b> (str):   The permission scope of the token. 
 - <b>`notBefore`</b> (str):  Sets the time at which the token can be used. 
 - <b>`notAfter`</b> (str):  Sets the time after which the token cannot be used. 

**Returns:**
 
 - <b>`dict`</b>:  JSON response of the new created token or None on error 


---

<a href="../hyperfabric_SDK.py#L153"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_bearer_token`

```python
get_bearer_token(auth, tokenId, include_metadata=False)
```

Retrieves a specific bearer token by its ID. 

**Args:**
 
 - <b>`tokenId`</b> (str):  The ID of the bearer token. 
 - <b>`include_metadata`</b> (bool, optional):  Include metadata in the response. Defaults to False. 

**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the bearer token, or None on error. 


---

<a href="../hyperfabric_SDK.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_bearer_token`

```python
delete_bearer_token(auth, tokenId)
```

Deletes a specific bearer token by its ID. 

**Args:**
 
 - <b>`tokenId`</b> (str):  The ID of the bearer token to delete. 

**Returns:**
 
 - <b>`int`</b>:  HTTP status code, or None on error. 


---

<a href="../hyperfabric_SDK.py#L178"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_devices`

```python
get_devices(auth)
```

Retrieves a list of devices. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the list of devices, or None on error. 


---

<a href="../hyperfabric_SDK.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabrics`

```python
get_fabrics(auth, fabricId=None, candidate=None, include_metadata=False)
```

Retrieves a list of fabrics. 

**Args:**
 
 - <b>`fabricId`</b> (str, optional):  Filter by one or more fabric ids and or names. Defaults to None. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`include_metadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 

**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the list of fabrics, or None on error. 


---

<a href="../hyperfabric_SDK.py#L210"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_fabric`

```python
create_fabric(
    auth,
    fabric_name,
    description,
    location,
    address,
    city,
    country,
    labels,
    topology=None
)
```

Creates a new fabric. 

**Args:**
 
 - <b>`fabric_name`</b> (str):  The name of the fabric.  Must be unique and DNS compliant. 
 - <b>`description`</b> (str):  A description of the fabric. 
 - <b>`location`</b> (str):  A location identifier. 
 - <b>`address`</b> (str):  The street address. 
 - <b>`city`</b> (str):  The city. 
 - <b>`country`</b> (str):  The two-letter country code. 
 - <b>`labels`</b> (list, optional):  A list of labels for the fabric. Defaults to []. 
 - <b>`topology`</b> (str, optional):  The fabric topology (MESH or SPINE_LEAF). Defaults to None. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the created fabric information, or None on error. 


---

<a href="../hyperfabric_SDK.py#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric`

```python
get_fabric(auth, fabricId, candidate=None, include_metadata=False)
```

Retrieves a specific fabric. 

**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`include_metadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 

**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the fabric information, or None on error. 


---

<a href="../hyperfabric_SDK.py#L265"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_fabric`

```python
update_fabric(auth, fabricId, payload)
```

Updates a specific fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`payload`</b> (dict):  A JSON payload containing the updated fabric properties. The keys depend upon #/components/schemas/configFabric: 
 - <b>`* name (str, optional)`</b>:   The user-defined name of the fabric 
 - <b>`* description (str, optional)`</b>:  The description of the fabric. 
 - <b>`* location (str, optional)`</b>:  The location of the fabric. 
 - <b>`* address (str, optional)`</b>:  The street address. 
 - <b>`* city (str, optional)`</b>:  The city. 
 - <b>`* country (str, optional)`</b>:  The two-letter country code. 
 - <b>`* labels (list, optional)`</b>:  A list of labels for the fabric. 



**Example:**
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
 
 - <b>`dict`</b>:  JSON response containing the updated fabric information, or None on error. 


---

<a href="../hyperfabric_SDK.py#L299"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_fabric`

```python
delete_fabric(auth, fabricId)
```

Deletes a specific fabric. 

**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric to delete. 

**Returns:**
 
 - <b>`int`</b>:  HTTP status code, or None on error. 


---

<a href="../hyperfabric_SDK.py#L311"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_candidates`

```python
get_fabric_candidates(
    auth,
    fabricId,
    name=None,
    txnId=None,
    needInactive=None,
    needReviews=None,
    needEvents=None,
    startTime=None,
    endTime=None
)
```

Retrieves a list of candidate configurations for a specific fabric. 

**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`name`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`txnId`</b> (int, optional):  The transaction sequence number. Defaults to None. 
 - <b>`needInactive`</b> (bool, optional):  Include committed/reverted candidate configurations. Defaults to None. 
 - <b>`needReviews`</b> (bool, optional):  Include the list of reviews. Defaults to None. 
 - <b>`needEvents`</b> (bool, optional):  Include the list of activity events. Defaults to None. 
 - <b>`startTime`</b> (str, optional):  Start value of time range. Defaults to None. 
 - <b>`endTime`</b> (str, optional):  End value of the time range. Defaults to None. 

**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the list of candidate configurations, or None on error. 


---

<a href="../hyperfabric_SDK.py#L345"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_candidate`

```python
get_fabric_candidate(
    auth,
    fabricId,
    name,
    needInactive=None,
    needReviews=None,
    needEvents=None
)
```

Retrieves a specific candidate configuration for a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`name`</b> (str):  The name of the candidate configuration. 
 - <b>`needInactive`</b> (bool, optional):  Include committed/reverted candidate configuration.  Defaults to None. 
 - <b>`needReviews`</b> (bool, optional):  Include the list of reviews. Defaults to None. 
 - <b>`needEvents`</b> (bool, optional):  Include the list of activity events. Defaults to None. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the candidate configuration, or None on error. 


---

<a href="../hyperfabric_SDK.py#L370"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `review_fabric_candidate`

```python
review_fabric_candidate(auth, fabricId, name, comments)
```

Adds a comment (review) to a specific candidate configuration. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`name`</b> (str):  The name of the candidate configuration. 
 - <b>`comments`</b> (str):  The review comments to add. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L386"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `commit_fabric_candidate`

```python
commit_fabric_candidate(auth, fabric_name, name, comments)
```

Commits a specific candidate configuration to the running configuration of a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`name`</b> (str):  The name of the candidate configuration. 
 - <b>`comments`</b> (str):  The commit comments. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L403"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `revert_fabric_candidate`

```python
revert_fabric_candidate(auth, fabricId, name)
```

Discards (reverts) a specific candidate configuration. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`name`</b> (str):  The name of the candidate configuration. 



**Returns:**
 
 - <b>`int`</b>:  HTTP status code, or None on error. 


---

<a href="../hyperfabric_SDK.py#L418"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_connections`

```python
get_fabric_connections(auth, fabricId, candidate=None)
```

Retrieves a list of connections within a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L435"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_fabric_connections`

```python
add_fabric_connections(auth, fabricId, connections)
```

Adds one or more connections to a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`connections`</b> (list):  A list of connections to add. 

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
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L474"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `set_fabric_connections`

```python
set_fabric_connections(auth, fabricId, connections)
```

Replaces all connections in a fabric with a new set of connections. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`connections`</b> (list):  A list of connections to set. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L489"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_fabric_connections`

```python
delete_fabric_connections(auth, fabricId)
```

Deletes all connections in the fabric. 

**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 


---

<a href="../hyperfabric_SDK.py#L499"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_connection`

```python
get_fabric_connection(auth, fabricId, connectionId, candidate=None)
```

Retrieves a specific connection by ID. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`connectionId`</b> (str):  The ID of the connection. 
 - <b>`candidate`</b> (str, optional):   Candidate configuration name. Defaults to None. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L517"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_fabric_connection`

```python
delete_fabric_connection(auth, fabricId, connectionId)
```

Delete a specific connection. 

**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`connectionId`</b> (str):  The ID of the connection. 


---

<a href="../hyperfabric_SDK.py#L528"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_nodes`

```python
get_fabric_nodes(auth, fabricId, candidate=None, includeMetadata=None)
```

Retrieves a list of nodes within a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L548"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_fabric_nodes`

```python
add_fabric_nodes(auth, fabric_name, nodes)
```

Adds one or more nodes to a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodes`</b> (list):  A list of node objects to add. 

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
           },
          ]
        ``` 

**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L588"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_node`

```python
get_fabric_node(auth, fabricId, nodeId, candidate=None, includeMetadata=None)
```

Retrieves a specific node by ID or name. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L609"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_fabric_node`

```python
update_fabric_node(auth, fabricId, nodeId, payload)
```

Updates a specific node. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 
 - <b>`payload`</b> (dict):  A JSON payload containing the updated node properties. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L624"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_fabric_node`

```python
delete_fabric_node(auth, fabricId, nodeId)
```

Deletes a specific node. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 



**Returns:**
 
 - <b>`int`</b>:  HTTP status code, or None on error. 


---

<a href="../hyperfabric_SDK.py#L638"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bind_device`

```python
bind_device(auth, fabricId, nodeId, deviceId)
```

Binds a device to a specific node 

**Args:**
 
  - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
  - <b>`nodeId`</b> (str):  The ID or name of the node. 
  - <b>`deviceId`</b> (str):  The serial of the device. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response or None on Error 


---

<a href="../hyperfabric_SDK.py#L652"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `unbind_device`

```python
unbind_device(auth, fabricId, nodeId)
```

Unbinds a device from a specific node 

**Args:**
 
  - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
  - <b>`nodeId`</b> (str):  The ID or name of the node. 



**Returns:**
 
 - <b>`Int`</b>:  Response Code or None on Error 


---

<a href="../hyperfabric_SDK.py#L666"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_management_ports`

```python
get_management_ports(
    auth,
    fabricId,
    nodeId,
    candidate=None,
    includeMetadata=None
)
```

Retrieves a list of management ports for a specific node. 

**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 

**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the list of management ports, or None on error. 


---

<a href="../hyperfabric_SDK.py#L686"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_management_ports`

```python
add_management_ports(auth, fabricId, nodeId, ports)
```

Creates or updates one or more ManagementPorts for a fabric node 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):   The node id or name from which a device is bound. 
 - <b>`ports`</b> (list):  A list of one or more ports to update.  Example payload: ```json
            [
              {

 - <b>`              "name"`</b>:  "eth0",

 - <b>`              "ipv4Address"`</b>:  "10.1.1.250/31",

 - <b>`              "ipv4Gateway"`</b>:  "10.1.1.251",

 - <b>`              "ipv6Address"`</b>:  "2a02:1243:5687:0:9c09:2c7a:7c78:9ffc/64",

 - <b>`              "ipv6Gateway"`</b>:  "2a02:1243:5687:0:8d91:ba6b:b24d:9b41",

 - <b>`              "dnsAddresses"`</b>:  [
                "8.8.8.8",
                "8.8.4.4"
              ],

 - <b>`              "proxyAddress"`</b>:  "https://10.1.1.10:8080",

 - <b>`              "proxyUsername"`</b>:  "admin",

 - <b>`              "proxyPassword"`</b>:  "admin123",

 - <b>`              "enabled"`</b>:  true,

 - <b>`              "cloudUrls"`</b>:  [

 - <b>`               "https`</b>: //a.b.com"
              ],

 - <b>`              "setProxyPassword"`</b>:  true,

 - <b>`              "noProxy"`</b>:  [
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
 
 - <b>`dict`</b>:  JSON response 


---

<a href="../hyperfabric_SDK.py#L740"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_management_port`

```python
get_management_port(
    auth,
    fabricId,
    nodeId,
    id,
    candidate=None,
    includeMetadata=None
)
```

Retrieves information on the management port specified 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):   The node id or name from which a device is bound. 
 - <b>`id`</b> (str):  ID of the port 



**Returns:**
 
 - <b>`dict`</b>:  JSON response 


---

<a href="../hyperfabric_SDK.py#L760"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_management_port`

```python
update_management_port(auth, fabricId, nodeId, id, payload)
```

Updates the settings on a management port 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):   The node id or name from which a device is bound. 
 - <b>`ports`</b> (list):  A list of one or more ports to update. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response 


---

<a href="../hyperfabric_SDK.py#L776"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_ports`

```python
get_ports(auth, fabricId, nodeId, candidate=None, includeMetadata=None)
```

Retrieves a list of ports for a specific node. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L797"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `set_ports`

```python
set_ports(auth, fabricId, nodeId, ports)
```

Replaces all ports for a specific node. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 
 - <b>`ports`</b> (list):  A list of port objects to set. 

Here is an example: ```json
      [
       {

 - <b>`       "name"`</b>:  "Ethernet1_5",

 - <b>`       "enabled"`</b>:  true,

 - <b>`       "roles"`</b>:  [
         "HOST_PORT"
       ]
      },
      {

 - <b>`       "name"`</b>:  "Ethernet1_6",

 - <b>`       "enabled"`</b>:  true,

 - <b>`       "roles"`</b>:  [
         "HOST_PORT"
       ]
      },
      {

 - <b>`       "name"`</b>:  "Ethernet1_7",

 - <b>`       "enabled"`</b>:  true,

 - <b>`       "roles"`</b>:  [
         "HOST_PORT"
       ]
      },
      {

 - <b>`       "name"`</b>:  "Ethernet1_8",

 - <b>`       "enabled"`</b>:  true,

 - <b>`       "roles"`</b>:  [
         "HOST_PORT"
       ]
      }
     ]
    ``` 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L848"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_port`

```python
get_port(auth, fabricId, nodeId, portId, candidate=None, includeMetadata=None)
```

Retrieves a specific port by its ID. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 
 - <b>`portId`</b> (str):  The ID of the port. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L870"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_port`

```python
update_port(auth, fabricId, nodeId, portId, payload)
```

Updates a specific port. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 
 - <b>`portId`</b> (str):  The ID of the port. 
 - <b>`payload`</b> (dict):  A JSON payload containing the updated port properties. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L886"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `reset_port`

```python
reset_port(auth, fabricId, nodeId, portId)
```

Resets a specific port 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`nodeId`</b> (str):  The ID or name of the node. 
 - <b>`portId`</b> (str):  The ID of the port. 


---

<a href="../hyperfabric_SDK.py#L898"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_vnis`

```python
get_fabric_vnis(auth, fabricId, candidate=None, includeMetadata=None)
```

Retrieves a list of VNIs within a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L918"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_fabric_vnis`

```python
add_fabric_vnis(auth, fabricId, vnis)
```

Adds one or more VNIs to a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vnis`</b> (list):  A list of VNI objects to add. Each VNI object must conform to the `#/components/schemas/modelsVni` schema. 

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
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L959"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_vni`

```python
get_fabric_vni(auth, fabricId, vniId, candidate=None, includeMetadata=None)
```

Retrieves a specific VNI by ID or name. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vniId`</b> (str):  The ID or name of the VNI. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object Metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L980"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_fabric_vni`

```python
update_fabric_vni(auth, fabricId, vniId, payload)
```

Updates a specific VNI. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vniId`</b> (str):  The ID or name of the VNI. 
 - <b>`payload`</b> (dict):  A JSON payload containing the updated VNI properties. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L995"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_fabric_vni`

```python
delete_fabric_vni(auth, fabricId, vniId)
```

Deletes a VNI given its ID 



**Args:**
 
  - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
  - <b>`vniId`</b> (str, optional):  The name for the device you are listing deleting a VNI device 


---

<a href="../hyperfabric_SDK.py#L1007"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_vni_members`

```python
get_fabric_vni_members(
    auth,
    fabricId,
    vniId,
    candidate=None,
    includeMetadata=None
)
```

Retrieves a list of vni members from a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vniId`</b> (str):  The ID or name of the vni. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1028"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_fabric_vni_members`

```python
add_fabric_vni_members(auth, fabricId, vniId, payload)
```

Adds one or more vni member to a fabric vni object 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vrfId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
 - <b>`payload`</b> (str, optional):  The Route Tag Defaults to None 


---

<a href="../hyperfabric_SDK.py#L1043"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_vni_member`

```python
get_fabric_vni_member(
    auth,
    fabricId,
    vniId,
    memberId,
    candidate=None,
    includeMetadata=None
)
```

Gets details for a vni member 

**Args:**
 
  - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
  - <b>`vniId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
  - <b>`memberId`</b> (str, optional):  The name for the device you are listing information for. Defaults to None 



**Returns:**
 
 - <b>`int`</b>:  JSON response on success or None on Fail 


---

<a href="../hyperfabric_SDK.py#L1062"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_fabric_vni_member`

```python
delete_fabric_vni_member(auth, fabricId, vniId, memberId)
```

Deletes a VNI member given its ID. 



**Args:**
 
  - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
  - <b>`vniId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
  - <b>`memberId`</b> (str, optional):  The name for the device you are listing deleting a VNI device 


---

<a href="../hyperfabric_SDK.py#L1075"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_vrfs`

```python
get_fabric_vrfs(auth, fabricId, candidate=None, includeMetadata=None)
```

Retrieves a list of VRFs within a fabric. 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1095"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_fabric_vrfs`

```python
add_fabric_vrfs(auth, fabricId, vrfs)
```

Creates or updates one or more Vrf with a specific name 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vnis`</b> (list):  Each VRF objects must conform to the `#/components/schemas/modelsVrf`. 

**Example:**
 ```json
       [
          {
           "name": "Vrf-exampleOne",
           "enabled": true
          },
          {
           "name": "Vrf-exampleTwo",
           "description": "Test Vrf for example-fabric",
           "labels": [
            "VRF_LABEL_ONE",
            "vrf_label_two",
            "vrf label three"
           ],
           "enabled": true
          },
          {
           "name": "Vrf-exampleThree",
           "enabled": true
          }
       ]
       ``` 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_vrf`

```python
get_fabric_vrf(auth, fabricId, vrfId, candidate=None, includeMetadata=None)
```

Gets details for a vrf 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vrfId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
 - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_fabric_vrf`

```python
update_fabric_vrf(auth, fabricId, vrfId, payload)
```

Updates a specific Vrf 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vrfId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
 - <b>`payload`</b> (str, optional):  The Route Payload Defaults to None 

```json
    {

 - <b>`    "name"`</b>:  "Vrf-examplevrf1",

 - <b>`    "annotations"`</b>:  [
      {

 - <b>`      "name"`</b>:  "position",

 - <b>`      "value"`</b>:  "1234"
     }
    ],

 - <b>`    "enabled"`</b>:  true,

 - <b>`    "isDefault"`</b>:  true
    }
    ``` 


---

<a href="../hyperfabric_SDK.py#L1181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_fabric_vrf`

```python
delete_fabric_vrf(auth, fabricId, vrfId)
```

Deletes a specific Vrf object. 

**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vrfId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 


---

<a href="../hyperfabric_SDK.py#L1192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_static_routes`

```python
get_fabric_static_routes(
    auth,
    fabricId,
    vrfId,
    candidate=None,
    includeMetadata=None
)
```

Gets a list of staticRoutes for a vrf 



**Args:**
 
  - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
  - <b>`vrfId`</b> (str):  The unique identifier of the VRF to which this static routes belong to. 
  - <b>`candidate`</b> (str, optional):  The candidate configuration name. Defaults to None. 
  - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_fabric_static_routes`

```python
add_fabric_static_routes(auth, fabricId, vrfId, staticRoutes)
```

 Creates or updates one or more static route for a fabric vrf object 



**Args:**
 
     - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
     - <b>`vrfId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
     - <b>`staticRoutes`</b> (str, optional):  Payload which creates or updates the static route. Defaults to None 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 

**staticRoutes** example payload: ```json
    [
    {

 - <b>`      "name"`</b>:  "Vrf-exampleOne-SR1",

 - <b>`      "enabled"`</b>:  true,

 - <b>`      "routes"`</b>:  [
         {

 - <b>`          "prefix"`</b>:  "10.10.10.0/24",

 - <b>`          "preference"`</b>:  10,

 - <b>`          "discard"`</b>:  true
        },
        {

 - <b>`          "prefix"`</b>:  "11.10.10.0/24",

 - <b>`          "preference"`</b>:  10,

 - <b>`          "discard"`</b>:  true
        }
      ]
    }
   ]

    ``` 


---

<a href="../hyperfabric_SDK.py#L1254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_fabric_static_route`

```python
get_fabric_static_route(
    auth,
    fabricId,
    vrfId,
    routeId,
    candidate=None,
    includeMetadata=None
)
```

Gets information for a single fabric static Route 



**Args:**
 
  - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
  - <b>`vrfId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
  - <b>`routeId`</b> (str, optional):  The name for the device you are listing information for. Defaults to None 



**Returns:**
 
 - <b>`int`</b>:  JSON response on success or None on Fail 


---

<a href="../hyperfabric_SDK.py#L1274"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_fabric_static_route`

```python
update_fabric_static_route(auth, fabricId, vrfId, routeId, payload)
```

Updates a specific static route for a given VRF object 



**Args:**
 
 - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
 - <b>`vrfId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
 - <b>`routeId`</b> (str, optional):  The name for the device you are listing information for. Defaults to None 
 - <b>`payload`</b> (str, optional):  The Route Payload Defaults to None 


---

<a href="../hyperfabric_SDK.py#L1287"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_fabric_static_route`

```python
delete_fabric_static_route(auth, fabricId, vrfId, routeId)
```

Deletes a static route for a vrf ID in a fabric 



**Args:**
 
  - <b>`fabricId`</b> (str):  The ID or name of the fabric. 
  - <b>`vrfId`</b> (str):  A list of user-defined labels that can be used for grouping and filtering VRFs. 
  - <b>`routeId`</b> (str, optional):  The name for the device you are listing information for. Defaults to None 


---

<a href="../hyperfabric_SDK.py#L1300"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_users`

```python
get_users(auth, emails=None, enabled=None, roles=None, includeMetadata=None)
```

Retrieves a list of users. 



**Args:**
 
 - <b>`emails`</b> (str, optional):  Filter by one or more email addresses. Defaults to None. 
 - <b>`enabled`</b> (bool, optional):  Only return users that are administratively enabled. Defaults to None. 
 - <b>`roles`</b> (str, optional):  Only return users with specific roles (ADMIN, READ_WRITE, READ_ONLY). Defaults to None. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1325"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_users`

```python
add_users(auth, users)
```

Adds one or more users to the organization. 

**Args:**
 
 - <b>`users`</b> (list):  A list of user objects to add. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1339"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_user`

```python
get_user(auth, id, includeMetadata=None)
```

Retrieves a specific user by ID or email. 

**Args:**
 
 - <b>`id`</b> (str):  The ID or email of the user. 
 - <b>`includeMetadata`</b> (bool, optional):  Include object metadata in the response. Defaults to False. 



**Returns:**
 
 - <b>`dict`</b>:  JSON response containing the user information, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1355"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `update_user`

```python
update_user(auth, id, payload)
```

Updates a specific user. 



**Args:**
 
 - <b>`id`</b> (str):  The ID or email of the user. 
 - <b>`payload`</b> (dict):  A JSON payload containing the updated user properties. Example Payload: ```json
    {

 - <b>`     "enabled"`</b>:  true,

 - <b>`     "labels"`</b>:  ["LAB_ONE", "LAB_TWO"],

 - <b>`     "role"`</b>:  "READ_ONLY"
    }
    ``` 



**Returns:**
 
 - <b>`dict`</b>:  JSON response, or None on error. 


---

<a href="../hyperfabric_SDK.py#L1377"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delete_user`

```python
delete_user(auth, id)
```

Deletes a specific user. 



**Args:**
 
 - <b>`id`</b> (str):  The ID or email of the user. 



**Returns:**
 
 - <b>`int`</b>:  HTTP status code, or None on error. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
