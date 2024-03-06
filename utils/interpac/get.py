# ---------------------------------------------------------------------------- #
#                              Get Request Library                             #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Imports --------------------------------- #
import requests

# ----------------------------------- Code ----------------------------------- #
class Getter:
    """
    A class that handles HTTP GET requests.
    """

    def __init__(self):
        pass

    def getrequest(self, url: str, params=None, **kwargs):
        """
        Sends a GET request to the specified URL.

        Args:
            url (str): The URL to send the request to.
            params (dict, optional): The query parameters to include in the request. Defaults to None.
            **kwargs: Additional keyword arguments to pass to the requests.get() function.

        Returns:
            requests.Response: The response object returned by the GET request.
        """
        return requests.get(url=url, params=params, **kwargs)