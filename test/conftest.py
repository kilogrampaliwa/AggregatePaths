import pytest
import json
from unittest.mock import mock_open, patch
import os

@pytest.fixture
def lines():
    return ["line1\n", "line2 banned\n", "line3 wanted\n"]

@pytest.fixture
def temp_output_file():
    test_output = "test_output.txt"
    yield test_output
    if os.path.exists(test_output):
        os.remove(test_output)

@pytest.fixture
def mock_config():
    config = {
        "wanted": ["wanted"],
        "banned": ["banned"],
        "delete": ["line3"]
    }
    config_json = json.dumps(config)

    with patch('builtins.open', mock_open(read_data=config_json)):
        yield config
