import pytest


def test_upper():
    assert 'foo'.upper() == 'FOO'


def test_upper2():
    assert 'foo'.upper() == 'Foo'


@pytest.mark.parametrize("obj", ['1', '2', 'Foo'])
def test_isdigit(obj):
    assert obj.isdigit()
