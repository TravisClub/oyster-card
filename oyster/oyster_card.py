import os
import json

from oyster.card import Card


path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
file_name = dir_path[:-6] + 'docs/stations.json'


def read_stations_file(file_name):
    """Reads and loads list of stations

    Returns
    -------
    stations_dict
        Dictionary that contains all stations
    """
    try:
        with open(file_name, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError as fnf_error:
        print("I/O error: {}".format(fnf_error))
        raise FileNotFoundError


def station_zone(station_name):
    """Returns the zone(s) for the given station.

    Parameters
    ----------
    station_name : str
        Name of station

    Returns
    -------
    zone
        A set with the zone or zones for given station
    """
    stations_list_loaded = read_stations_file(file_name)
    for station in stations_list_loaded['stations']:
        if station['name'] == station_name:
            return set(station['zone'])


card_1 = Card()
card_1.top_up(30)
card_1.swipe_in('tube', 'Holborn')
card_1.swipe_out(station_zone(card_1.trip.orig_station), station_zone('Earl’s Court'))
card_1.swipe_in('bus')
card_1.swipe_in('tube', 'Earl’s Court')
card_1.swipe_out(station_zone(card_1.trip.orig_station), station_zone('Hammersmith'))
print(card_1.view_balance())
