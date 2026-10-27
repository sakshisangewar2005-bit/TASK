"""Booking class: stores one confirmed booking."""


class Booking:
    def __init__(self, booking_id, flight, passenger, tickets,
                 subtotal, discount, final_amount):
        self.__booking_id = booking_id
        self.__flight = flight
        self.__passenger = passenger
        self.__tickets = tickets
        self.__subtotal = subtotal
        self.__discount = discount
        self.__final_amount = final_amount

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def flight(self):
        return self.__flight

    @property
    def passenger(self):
        return self.__passenger

    @property
    def tickets(self):
        return self.__tickets

    @property
    def subtotal(self):
        return self.__subtotal

    @property
    def discount(self):
        return self.__discount

    @property
    def final_amount(self):
        return self.__final_amount

    def display_summary(self):
        f, p = self.__flight, self.__passenger
        print(f"Booking ID: {self.__booking_id}")
        print(f"Flight: {f.code} | {f.source} to {f.destination} ({f.airline})")
        print(f"Passenger: {p.name} (Age {p.age})")
        print(f"Passenger type: {p.get_passenger_type()}")
        print(f"Tickets: {self.__tickets}")
        print(f"Base fare per ticket: Rs. {f.base_fare:,.0f}")
        print(f"Subtotal: Rs. {self.__subtotal:,.0f}")
        print(f"{p.get_passenger_type()} discount ({p.get_discount_percentage()}%): "
              f"Rs. {self.__discount:,.0f}")
        print(f"Final amount: Rs. {self.__final_amount:,.0f}")
