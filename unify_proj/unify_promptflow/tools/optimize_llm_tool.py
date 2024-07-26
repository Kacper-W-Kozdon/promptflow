from promptflow.core import tool
from promptflow.connections import CustomConnection
from typing import Union, Optional


@tool
def optimize_llm(connection: CustomConnection, config: dict) -> Union[dict, str]:
"""
Selects the optimal model for a step of a flow.

:param connection: CustomConnection to use
:param config: requirements for the optimization
"""
    return "Hello " + input_text