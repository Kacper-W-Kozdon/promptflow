from promptflow.core import tool
from promptflow.connections import CustomConnection
from typing import Union, Optional, Sequence
from unify import Unify


@tool
def optimize_llm(connection: Unify, config: dict, input_text: Union[str, Sequence]) -> Union[dict, str]:
    """
    Selects the optimal model for a step of a flow.

    :param connection: CustomConnection to use
    :param config: requirements for the optimization
    """
    endpoint = config.get("endpoint", None)
    model = config.get("model", None)
    provider = config.get("provider", None)
    if endpoint:
        connection.set_endpoint(endpoint)
    if not endpoint and all([model, provider]):
        connection.set_model(model)
        connection.set_provider(provider)

    return "Hello " + input_text