"""# Utility functions for bitpin module."""

import asyncio


def get_loop() -> asyncio.AbstractEventLoop:
    """
    Get event loop.

    Returns:
        asyncio.AbstractEventLoop
    """

    try:
        loop = asyncio.get_event_loop()
        return loop
    except RuntimeError as e:
        if str(e).startswith("There is no current event loop in thread"):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop

        raise e
