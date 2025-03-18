# Cisco Hyperfabric API Python SDK (Beta)

This Python SDK provides a convenient and reasonably simple way to interact with the Cisco Hyperfabric API. It is automatically generated and should serve as a helpful starting point for Python developers. Please be aware that:

*   **SDK Completeness:** This SDK was generated automatically. Some endpoints or features might be incomplete or may have not been tested as you would expect.
*   **Support:** No formal support is available for this SDK. Use it at your own risk.

**Use this SDK with caution and thoroughly test your integrations.**

## Features

*   Automatically generated from the Hyperfabric OpenAPI specification
*   Provides Python functions for each API endpoint and HTTP verb
*   Includes error handling
*   Provides example code for each function, demonstrating payload structure and parameter usage

## Getting Started

1.  **Authentication:**

    *   Obtain a Bearer Token from the Hyperfabric web UI
    *   Export the token as an environment variable called AUTH_TOKEN (```export AUTH_TOKEN=<token>```)
    *   Import auth_config in your client code; this builds the HTTP authentication header

3.  **Usage:**

    *   Import the generated Python SDK or specific functions from the SDK into your project
    *   Refer to the docstrings within each function for detailed usage instructions, including parameter types and example payloads
    *   Inspect the test_SDK.py example provided for your convenience (launch with ```python test_SDK.py SDK-Test```)

## Example Usage

```python
from hyperfabric_SDK import get_fabrics, create_fabric
import auth_config

# Get a list of fabrics
fabrics = get_fabrics()
if fabrics:
    print("Fabrics:", fabrics)

# Create a new fabric (Remember to replace with your actual token)
fabric_id = create_fabric(fabric_name="my-new-fabric", description="A test fabric", location="HQ", address="Test Address", city="Test City", country="US", labels=["test", "example"])
if fabric_id:
  print(f"Successfully created fabric with ID: {fabric_id}")
else:
  print("Fabric Creation Failed")
