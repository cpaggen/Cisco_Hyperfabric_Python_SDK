import os

def get_api_headers(auth_token=None):
    """
    Assembles API headers using the authorization token.

    Args:
        auth_token (str, optional): The authorization token. If None, it attempts to
            retrieve it from the AUTH_TOKEN environment variable. Defaults to None.

    Returns:
        dict: A dictionary containing the API headers, including the Authorization header.

    Raises:
        ValueError: If the AUTH_TOKEN environment variable is not set and no auth_token is provided.
    """

    if auth_token is None:
        try:
            auth_token = os.environ['AUTH_TOKEN']
        except KeyError:
            raise ValueError("AUTH_TOKEN environment variable not set, and no auth_token provided.")

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    return headers

