

def test_calculate_trip_fare_returns_anywhere_in_zone_1_fare_when_two_one_zones_indicated(some_empty_trip):
    zone_fake_1 = set([1])
    zone_fake_2 = set([1])
    assert some_empty_trip.calculate_trip_fare(zone_fake_1, zone_fake_2) == 2.50


def test_calculate_trip_fare_returns_anyone_zone_outside_zone_1_fare_when_two_zones_outside_zone_1_indicated(
        some_empty_trip):
    zone_fake_1 = set([4])
    zone_fake_2 = set([4])
    assert some_empty_trip.calculate_trip_fare(zone_fake_1, zone_fake_2) == 2.00


def test_calculate_trip_fare_returns_any_two_zones_including_zone_1_fare_when_any_two_zones_including_zone_1_indicated(
        some_empty_trip):
    zone_fake_1 = set([1])
    zone_fake_2 = set([2])
    assert some_empty_trip.calculate_trip_fare(zone_fake_1, zone_fake_2) == 3.00


def test_calculate_trip_fare_returns_any_two_zones_excluding_zone_1_fare_when_any_two_zones_excluding_zone_1_indicated(
        some_empty_trip):
    zone_fake_1 = set([4])
    zone_fake_2 = set([5])
    assert some_empty_trip.calculate_trip_fare(zone_fake_1, zone_fake_2) == 2.25


def test_calculate_trip_fare_returns_more_than_two_zones_fare_when_more_than_two_zones_indicated(some_empty_trip):
    zone_fake_1 = set([1])
    zone_fake_2 = set([3])
    assert some_empty_trip.calculate_trip_fare(zone_fake_1, zone_fake_2) == 3.20


def test_calculate_cheapest_zone_fare_returns_same_zone_when_both_stations_share_a_zone(some_empty_trip):
    zone_fake_1 = set([1])
    zone_fake_2 = set([1, 2])
    assert some_empty_trip.calculate_cheapest_zone_fare(zone_fake_1, zone_fake_2) == ({1}, {1})


def test_calculate_cheapest_zone_fare_returns_bigger_zone_when_both_stations_share_more_than_one_zone(some_empty_trip):
    zone_fake_1 = set([2, 3])
    zone_fake_2 = set([3, 2])
    assert some_empty_trip.calculate_cheapest_zone_fare(zone_fake_1, zone_fake_2) == ({3}, {3})


def test_calculate_cheapest_zone_fare_returns_smallest_zone_from_station_with_more_than_one_zone_when_station_with_one_zone_is_smaller_than_the_smallest_of_station_with_more_than_one_zone(
        some_empty_trip):
    zone_fake_1 = set([1])
    zone_fake_2 = set([2, 3])
    assert some_empty_trip.calculate_cheapest_zone_fare(zone_fake_1, zone_fake_2) == ({1}, {2})


def test_calculate_cheapest_zone_fare_returns_smallest_zone_from_station_with_more_than_one_zone_when_station_with_one_zone_is_bigger_than_the_biggest_of_station_with_more_than_one_zone(
        some_empty_trip):
    zone_fake_1 = set([4])
    zone_fake_2 = set([2, 3])
    assert some_empty_trip.calculate_cheapest_zone_fare(zone_fake_1, zone_fake_2) == ({3}, {4})
