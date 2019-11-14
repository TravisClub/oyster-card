import pytest

from oyster.card import Card
from oyster.trip import Trip


@pytest.fixture
def some_empty_card():
    """Returns a card instance with 0 balance"""
    return Card()


@pytest.fixture()
def some_fare():
    """Returns an amount"""
    yield 2.25


@pytest.fixture()
def some_amount():
    """Returns an amount"""
    yield 20


@pytest.fixture()
def some_empty_trip():
    """Returns an amount"""
    yield Trip('tube')
