import pytest


def test_m4():
    assert False


@pytest.mark.logg
def test_m5():
    assert 100 == 100


def test_m6():
    assert "vladis" == "VLADIS"


@pytest.mark.logg
def test_login_gmail():
    assert "admin" == "admin"
