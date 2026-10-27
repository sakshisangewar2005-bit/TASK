"""Flight class with encapsulated seat management."""


class Flight:
    def __init__(self, code, airline, source, destination, seats, base_fare):
        self.__code = code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = seats
        self.__base_fare = base_fare

    @property
    def code(self):
        return self.__code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def available_seats(self):
        return self.__available_seats

    @property
    def base_fare(self):
        return self.__base_fare

    def has_seats(self, count):
        return 0 < count <= self.__available_seats

    def reserve_seats(self, count):
        """Only place where seat count changes. Returns True on success."""
        if not self.has_seats(count):
            return False
        self.__available_seats -= count
        return True

    def display(self):
        print(f"{self.__code:<8}{self.__airline:<14}{self.__source:<12}"
              f"{self.__destination:<12}{self.__available_seats:<8}Rs. {self.__base_fare:,.0f}")
