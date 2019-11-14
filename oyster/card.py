from oyster.trip import Trip


class NotEnoughBalance(Exception):
    pass


class Card:
    """
    Class that models a Oyster card with its main functions

    Parameters
    ----------
    balance : float
        current balance of the oyster card
    trip : Trip
        instance of class trip

    Attributes
    ----------
    tube_max_fare : float
        max fare for tube service
    bus_max_fare : float
        max fare for bus service
    """
    tube_max_fare = 3.20
    bus_max_fare = 1.80

    def __init__(self, balance=0):
        self.balance = balance
        self.trip = Trip()

    def top_up(self, amount):
        """Top up card with an amount or adds difference between max fare and trip fare to the balance.

        Parameters
        ----------
        amount : float
            The amount to top up
        """
        self.balance += amount

    def subtract_amount(self, amount):
        """Subtracts trip price from the balance.

        Parameters
        ----------
        amount : float
            The amount to subtract
        station_name : str
            Should the fuels refilled to cover the distance?
        """
        self.balance -= amount

    def view_balance(self):
        """Shows remaining balance to stdout.

        Returns
        -------
        self.balance
            Current balance in the card
        """
        return 'The balance left in your card is: £{}'.format('%.2f' % self.balance)

    def swipe_in(self, trip_type, station_name=None):
        """Subtracts max fare from the balance and sets trip type and origin station name.

        Parameters
        ----------
        trip_type : str
            Type of trip
        station_name : str
            Name of origin station

        Raises
        ------
        NotEnoughBalance
            Not Enough Balance
        """
        if trip_type == 'tube' and 0 <= self.balance < self.tube_max_fare:
            raise NotEnoughBalance(
                'Sorry but you do not have enough balance.\nCurrent balance: £{}\n Please top up your card.'.format(
                    self.balance))
        elif trip_type == 'bus' and 0 <= self.balance < self.bus_max_fare:
            raise NotEnoughBalance(
                'Sorry but you do not have enough balance.\nCurrent balance: £{}\n Please top up your card.'.format(
                    self.balance))
        self.subtract_amount(self.tube_max_fare) if trip_type == 'tube' else self.subtract_amount(self.bus_max_fare)
        self.trip.type = trip_type
        self.trip.orig_station = station_name

    def swipe_out(self, station_origin_zone, station_destination_zone):
        """Calculates proper fare and replace the charged max fare with it.

        Parameters
        ----------
        station_origin_zone : str
            Origin station zone
        station_destination_zone : str
            Destination station zone
        """
        fare = self.trip.calculate_trip_fare(station_origin_zone, station_destination_zone)
        self.top_up(self.tube_max_fare - fare)

    @classmethod
    def increase_tube_or_bus_max_fare_price(cls, service_type, price):
        """Updates tube or bus max fare price.

        Parameters
        ----------
        price : float
            Price of the new max fare
        service_type : str
            Type of service
        """
        if service_type == 'tube':
            cls.tube_max_fare = price
        else:
            cls.bus_max_fare = price
