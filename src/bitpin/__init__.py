"""# Bitpin Python Library."""

import deprecated

from .clients.async_client import AsyncClient
from .clients.client import Client

__all__ = ["AsyncClient", "Client", "deprecated"]


# Meta
__version__ = "0.0.11"
__author__ = "amiwrpremium"
__email__ = "amiwrpremium@gmail.com"
__license__ = "MIT"
