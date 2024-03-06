# ---------------------------------------------------------------------------- #
#                              JSON Parsing Module                             #
# ---------------------------------------------------------------------------- #

# ---------------------------------- Imports --------------------------------- #
import json
import utils.interpac.get # FOR DEV ONLY
# -------------------------------- Module Code ------------------------------- #
class JasonMan:
    """
    A utility class for handling JSON data.

    Methods:
    - jparse(jsond): Parses a JSON string and returns the corresponding Python object.
    - jREQ(reqResult): Parses the JSON response from a requests.Response object and returns the corresponding Python object.
    """
    def __init__(self):
        pass

    def jparse(self, jsond):
        """
        Parses a JSON string and returns the corresponding Python object.

        Args:
        - jsond: A string containing JSON data.

        Returns:
        The parsed Python object.

        Example:
        ```
        json_data = '{"name": "John", "age": 30}'
        parsed_data = jparse(json_data)
        print(parsed_data)  # {'name': 'John', 'age': 30}
        ```
        """
        return json.loads(jsond)

    def jREQ(self, reqResult: utils.interpac.get.requests.Response):
        """
        Parses the JSON response from a requests.Response object and returns the corresponding Python object.

        Args:
        - reqResult: A requests.Response object.

        Returns:
        The parsed Python object.

        Example:
        ```
        response = requests.get('https://api.example.com/data')
        parsed_data = jREQ(response)
        print(parsed_data)  # {'name': 'John', 'age': 30}
        ```
        """
        return reqResult.json()