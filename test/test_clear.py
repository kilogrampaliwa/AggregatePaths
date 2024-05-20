import pytest
from src.clear import cleared

def test_clear(lines, configuration):
    processed = cleared(lines)
    assert processed.lines == ["line3 wanted"]
    assert processed.one_line == "line3 wanted"
