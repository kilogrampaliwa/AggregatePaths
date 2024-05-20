import pytest
import json
import os

@pytest.fixture
def lines():
    return ["line1\n", "line2 banned\n", "line3 wanted\n"]

@pytest.fixture
def configuration():
    config = {
        "wanted": ["wanted"],
        "banned": ["banned"],
        "delete": ["line3"]
    }
    with open("src/configuration.json", 'w') as file:
        json.dump(config, file)
    return config

@pytest.fixture
def temp_output_file():
    test_output = "test_output.txt"
    yield test_output
    os.remove(test_output)
