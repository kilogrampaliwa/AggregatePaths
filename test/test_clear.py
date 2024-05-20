import pytest
from src.clear import cleared

def test_clear(lines, mock_config):
    processed = cleared(lines)
    # Adjust expectations based on the mocked configuration
    expected_lines = ["line1", "line2 banned", "line3 wanted"]
    assert processed.lines == expected_lines
    assert processed.one_line == "line1line2 bannedline3 wanted"
