from typing import Dict, Optional

from promptflow._constants import ConnectionType
from promptflow.connections import CustomConnection
from promptflow.core import tool

# Unify client as the connection is a temporary solution before the final approach is chosen (CustomConnection?)


class UnifyConnection(CustomConnection):
    TYPE = ConnectionType.CUSTOM.value

    def __init__(
        self,
        secrets: Dict[str, str],
        configs: Dict[str, str] = None,
        **kwargs,
    ):
        _Connection_kwargs: Dict[str, str] = {
            "name": "UnifyConnection",
            "module": "unify.clients",
            "type": "Custom",
        }
        kwargs = {**kwargs, **_Connection_kwargs}
        super().__init__(secrets=secrets, configs=configs, **kwargs)


@tool
def single_sign_on(config: Optional[dict], secrets: Optional[dict]) -> UnifyConnection:
    ...
