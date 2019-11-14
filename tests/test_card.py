from unittest import mock
import pytest


def test_top_up_adds_amount_to_current_balance(some_empty_card, some_amount):
    some_empty_card.top_up(some_amount)
    assert some_empty_card.balance == some_amount


def test_subtract_amount_deducts_amount_from_cards_current_balance(some_empty_card, some_amount, some_fare):
    some_empty_card.top_up(some_amount)
    some_empty_card.subtract_amount(some_fare)
    assert some_empty_card.balance == some_amount - some_fare


def test_view_balance_shows_card_current_balance(some_empty_card, some_amount):
    some_empty_card.top_up(some_amount)
    assert some_empty_card.view_balance() == 'The balance left in your card is: £{}'.format('%.2f' % some_amount)


def test_swipe_in_subtracts_tuve_max_fare_when_tube(some_empty_card, some_amount):
    some_empty_card.top_up(some_amount)
    some_empty_card.swipe_in('tube')
    assert some_empty_card.balance == some_amount - some_empty_card.tube_max_fare


def test_swipe_in_subtracts_bus_max_fare_when_bus(some_empty_card, some_amount):
    some_empty_card.top_up(some_amount)
    some_empty_card.swipe_in('bus')
    assert some_empty_card.balance == some_amount - some_empty_card.bus_max_fare


def test_swipe_in_sets_current_trip_type(some_empty_card, some_amount):
    some_empty_card.top_up(some_amount)
    some_empty_card.swipe_in('bus')
    assert some_empty_card.trip.type == 'bus'


def test_swipe_in_sets_current_trip_origin_station(some_empty_card, some_amount):
    some_empty_card.top_up(some_amount)
    some_empty_card.swipe_in('tube', 'fake station')
    assert some_empty_card.trip.orig_station == 'fake station'


# def test_swipe_in_raises_not_enough_balance_exception_when_balance_less_than_max_tube_fare(some_empty_card):
#     with pytest.raises(NotEnoughBalance) as ne:
#         some_empty_card.swipe_in('tube', 'fake station')


# def test_swipe_out_sets_current_trip_origin_station(some_empty_card, some_amount):
#     mock_trip = Trip()
#     mock_trip.calculate_trip_fare = MagicMock()
#     some_empty_card.top_up(some_amount)
#     some_empty_card.swipe_in('tube', 'fake station')
#     assert some_empty_card.trip.orig_station == 'fake station'

def test_increase_tube_or_bus_max_fare_price_replaces_old_fare_with_new_fare_bus(some_empty_card):
    some_empty_card.increase_tube_or_bus_max_fare_price('bus', 2.00)
    assert some_empty_card.bus_max_fare == 2.00


def test_increase_tube_or_bus_max_fare_price_replaces_old_fare_with_new_fare_tube(some_empty_card):
    some_empty_card.increase_tube_or_bus_max_fare_price('tube', 5.00)
    assert some_empty_card.tube_max_fare == 5.00
