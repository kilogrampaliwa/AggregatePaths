import pytest
from src.aggregator.aggregator import aggre

@pytest.mark.parametrize("banned, expected", [
    ([], ["line1", "line2 banned", "line3 wanted"]),
    (["banned"], ["line1", "line3 wanted"]),
])
def test_aggregator_banned(lines, banned, expected):
    agg = aggre(lines, banned=banned)
    assert agg.lines == expected

@pytest.mark.parametrize("wanted, expected", [
    ([], ["line1", "line2 banned", "line3 wanted"]),
    (["wanted"], ["line3 wanted"]),
])
def test_aggregator_wanted(lines, wanted, expected):
    agg = aggre(lines, wanted=wanted)
    assert agg.lines == expected

@pytest.mark.parametrize("delete, expected", [
    ([], ["line1", "line2 banned", "line3 wanted"]),
    (["line3"], ["line1", "line2 banned", " wanted"]),
])
def test_aggregator_delete(lines, delete, expected):
    agg = aggre(lines, delete=delete)
    assert agg.lines == expected
