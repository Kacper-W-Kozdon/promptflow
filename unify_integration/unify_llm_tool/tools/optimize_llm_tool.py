from typing import Sequence, Union

from unify import Unify

from promptflow.core import tool


@tool
def optimize_llm(connection: Unify, config: dict, input_text: Union[str, Sequence]) -> Union[dict, str]:
    """
    Selects the optimal model for a step of a flow.

    :param connection: CustomConnection to use
    :param config: requirements for the optimization
    """
    quality = config.get("quality", "1")
    cost = config.get("cost", "4.65e-03")
    time_to_first_token = config.get("time_to_first_token", "2.08e-05")
    inter_token_latency = config.get("inter_token_latency", "2.07e-03")
    router = f"router@q:{quality}|c:{cost}|t:{time_to_first_token}|i:{inter_token_latency}"
    endpoint = config.get("endpoint", None)
    model = config.get("model", None)
    provider = config.get("provider", None)
    if isinstance(endpoint, list):
        ...
    if isinstance(model, list):
        models = ",".join(model)
        router_listed = router.split("@").insert(1, f"@model:{models}|")
        router = "".join(router_listed)
    if isinstance(provider, list):
        ...

    if endpoint:
        connection.set_endpoint(endpoint)
    if not endpoint and all([model, provider]):
        connection.set_model(model)
        connection.set_provider(provider)

    return "Hello " + input_text
