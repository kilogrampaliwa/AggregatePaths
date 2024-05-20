import pytest
import os
from run import main

@pytest.fixture
def mock_open(monkeypatch, temp_output_file):
    def _mock_open(filename, mode='r'):
        if filename == "output.txt" and mode == 'r':
            return iter(["line1\n", "line2 banned\n", "line3 wanted\n"])
        elif filename == "output.txt" and mode == 'w':
            return open(temp_output_file, mode)
        else:
            raise FileNotFoundError
    monkeypatch.setattr("builtins.open", _mock_open)

def test_run(mock_open, temp_output_file):
    main()
    
    with open(temp_output_file, 'r') as f:
        output = f.readlines()
    
    assert output == ["line1line3 wanted\n", "\n", "line1", "line3 wanted"]
