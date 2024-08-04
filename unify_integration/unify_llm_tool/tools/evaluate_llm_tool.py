from unify import Unify

from promptflow.core import tool


# Unify client as the connection is a temporary solution before the final approach is chosen (CustomConnection?)
@tool
def evaluate_llms(connection: Unify, models: list, prompt_set: list) -> dict:
    unify_tool = UnifyTool(api_key=connection["api_key"])
    results = unify_tool.benchmark(prompt_set, models)
    return results
