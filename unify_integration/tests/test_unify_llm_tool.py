import pytest
import unittest

from promptflow.connections import CustomConnection
from unify_integration.unify_llm_tool.tools.optimize_llm_tool import optimize_llm
from unify import Unify
from dotenv import load_dotenv
import os

load_dotenv()
unify_api_key = os.getenv("UNIFY_KEY")

@pytest.fixture
def my_custom_connection() -> Unify:
    my_custom_connection = Unify(
        api_key=unify_api_key
    )
    return my_custom_connection


class TestTool:
    def test_optimize_llm(self, my_custom_connection, config):
        result = optimize_llm(my_custom_connection, config, input_text="Microsoft")
        assert result == "Hello Microsoft"


# Run the unit tests
if __name__ == "__main__":
    unittest.main()