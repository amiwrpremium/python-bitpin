"""
# Exceptions.

Exceptions for the bitpin package.

# Description.
This module contains all the exceptions that are raised by the bitpin package.
"""

import json

from . import types as t


class APIException(Exception):
    """
    API Exception.

    Attributes:
        message (str): Message.
        result (t.Any): Result.
        status_code (int): Status code.
        response (t.Union[requests.Response, aiohttp.ClientResponse]): Response.
        request (t.Union[requests.PreparedRequest, aiohttp.ClientRequest]): Request.
        url (str): URL.
    """

    def __init__(self, response: t.HttpResponses, status_code: int, text: str):
        """
        Constructor.

        Args:
            response (t.Union[requests.Response, aiohttp.ClientResponse]): Response.
            status_code (int): Status code.
            text (str): Text.
        """

        try:
            json_res = json.loads(text)
        except ValueError:
            self.message = f"Invalid JSON error message from Bitpin: {response.text}"
            self.result = None
        else:
            self.message = json_res.get("detail", "Unknown error")
            self.result = json_res.get("result")

        self.status_code = status_code
        self.response = response
        self.request = getattr(response, "request", None)
        self.url = getattr(response, "url", None)

    def __str__(self) -> str:
        """
        String representation.

        Returns:
            str: String representation.
        """

        return f"APIError(code={self.status_code}): {self.message} | {self.result} | {self.url}"


class RequestException(Exception):
    """
    Request Exception.

    Attributes:
        message (str): Message.
    """

    def __init__(self, message: str):
        """
        Constructor.

        Args:
            message (str): Message.
        """

        self.message = message

    def __str__(self) -> str:
        """
        String representation.

        Returns:
            str: String representation.
        """

        return f"RequestException: {self.message}"
