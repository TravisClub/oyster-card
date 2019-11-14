class Trip:
    """
    Class that models a Oyster card with its main functions

    Parameters
    ----------
    type : str
        type of trip
    orig_station : str
        name of origin station
    dest_station : str
        name of destination station

    Attributes
    ----------
    anywhere_in_zone_1 : float
        fare for trips inside zone 1
    anyone_zone_outside_zone_1 : float
        fare for trips outside zone 1 but inside same zone
    any_two_zones_including_zone_1 : float
        fare for trips where one station is inside zone 1
    any_two_zones_excluding_zone_1 : float
        fare for trips outside zone 1 and inbetween different zones
    more_than_two_zones : float
        fare for trips further than two zones
    """
    anywhere_in_zone_1 = 2.50
    anyone_zone_outside_zone_1 = 2.00
    any_two_zones_including_zone_1 = 3.00
    any_two_zones_excluding_zone_1 = 2.25
    more_than_two_zones = 3.20

    def __init__(self, type=None, orig_station=None, dest_station=None):
        self.type = type
        self.orig_station = orig_station
        self.dest_station = dest_station

    def calculate_trip_fare(self, zone_origin=None, zone_destination=None):
        """Calculates trip fare based on zones.

        Parameters
        ----------
        zone_origin : set
            Origin station zone(s)
        zone_destination : set
            Destination station zone(s)

        Returns
        -------
        fare
            The cheapest fare for the trip
        """
        if len(zone_origin) > 1 or len(zone_destination) > 1:
            return self.calculate_trip_fare(*self.calculate_cheapest_zone_fare(zone_origin, zone_destination))
        elif zone_origin == zone_destination:
            return self.anywhere_in_zone_1 if max(zone_destination) == 1 else self.anyone_zone_outside_zone_1
        else:
            if max(zone_origin) == 1 or max(zone_destination) == 1:
                if abs(max(zone_origin) - max(zone_destination)) >= 2:
                    return self.more_than_two_zones
                return self.any_two_zones_including_zone_1
            else:
                return self.any_two_zones_excluding_zone_1

    @staticmethod
    def calculate_cheapest_zone_fare(set_zone_origin, set_zone_destination):
        """Calculates cheapest fare between stations when there is one station with more than one zone

        Parameters
        ----------
        set_zone_origin : set
            Origin station zone(s)
        set_zone_destination : set
            Destination station zone(s)

        Returns
        -------
        zones
            The two zones with the cheapest fare to travel between them
        """
        if len(set_zone_origin.intersection(set_zone_destination)) == 1:
            return set_zone_origin.intersection(set_zone_destination), set_zone_origin.intersection(
                set_zone_destination)
        elif len(set_zone_origin.intersection(set_zone_destination)) > 1:
            return {max(set_zone_origin.intersection(set_zone_destination))}, {max(set_zone_origin.intersection(
                set_zone_destination))}
        else:
            if min(max(set_zone_origin, set_zone_destination, key=len)) > max(min(set_zone_origin, set_zone_destination,
                                                                                  key=len)):
                return min(set_zone_origin, set_zone_destination, key=len), {min(
                    max(set_zone_origin, set_zone_destination, key=len))}
            return {max(max(set_zone_origin, set_zone_destination, key=len))}, min(set_zone_origin,
                                                                                   set_zone_destination, key=len)
