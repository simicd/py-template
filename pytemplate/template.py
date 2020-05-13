"""Template
===============
This is the template module description
"""

import logging
logger = logging.getLogger(__name__)

def template_function(name: str) -> str:
    """This is a simple template function

    Comments and detailed explanations with several lines
    should be added here.

    Args:
        name: Name which will be printed.

    Returns:
        string
    """

    logger.info("Running function...")
    print(__name__)

    return f"Hello {name}"
