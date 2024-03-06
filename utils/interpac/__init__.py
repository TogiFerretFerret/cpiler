import utils.interpac.get
import utils.interpac.post

class InternetInterface:
    """
    A class representing an internet interface.

    Methods:
    - get(url: str): Sends a GET request to the specified URL.
    """

    def __init__(self):
        pass

    def get(self, url: str):
        """
        Sends a GET request to the specified URL.

        Args:
            url (str): The URL to send the GET request to.

        Returns:
            The response from the GET request.
        """
        return utils.interpac.get.Getter().getrequest(url=url)

class InterMan(InternetInterface):
    """
    The InterMan class is responsible for managing internet interactions.
    It provides methods for sending HTTP GET requests.

    Attributes:
        None

    Methods:
        sendGet(url: str) -> Any: Sends an HTTP GET request to the specified URL and returns the response.

    """

    def __init__(self):
        pass

    def sendGet(self, url: str):
        """
        Sends an HTTP GET request to the specified URL and returns the response.

        Args:
            url (str): The URL to send the GET request to.

        Returns:
            Any: The response from the GET request.

        """
        return super().get(url=url)