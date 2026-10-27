"""FlightBookingSystem: controls flights, bookings and the menu."""
from flight import Flight
from passenger import RegularPassenger, StudentPassenger
from booking import Booking


class FlightBookingSystem:
    def __init__(self):
        self.__flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Kiran Air", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PN303", "SkyJet", "Pune", "Hyderabad", 10, 3000),
        ]
        self.__bookings = []
        self.__next_id = 1001

    # ---------- flights ----------
    def display_flights(self):
        print(f"\n{'Code':<8}{'Airline':<14}{'From':<12}{'To':<12}{'Seats':<8}Base Fare")
        print("-" * 64)
        for flight in self.__flights:
            flight.display()

    def find_flight(self, code):
        for flight in self.__flights:
            if flight.code.upper() == code.strip().upper():
                return flight
        return None

    # ---------- validation ----------
    def validate_booking_details(self, code, name, age_text, type_text, tickets_text):
        """Return (flight, passenger, tickets) or raise ValueError with a message."""
        flight = self.find_flight(code)
        if flight is None:
            raise ValueError("Invalid flight code.")
        if not name.strip():
            raise ValueError("Passenger name cannot be blank.")
        try:
            age = int(age_text)
        except ValueError:
            raise ValueError("Age must be a whole number.")
        if age <= 0:
            raise ValueError("Age must be greater than 0.")

        ptype = type_text.strip().lower()
        if ptype == "regular":
            passenger = RegularPassenger(name.strip(), age)
        elif ptype == "student":
            passenger = StudentPassenger(name.strip(), age)
        else:
            raise ValueError("Passenger type must be Regular or Student.")

        try:
            tickets = int(tickets_text)
        except ValueError:
            raise ValueError("Number of tickets must be a whole number.")
        if tickets <= 0:
            raise ValueError("Number of tickets must be greater than 0.")
        return flight, passenger, tickets

    # ---------- fare ----------
    def calculate_fare(self, flight, passenger, tickets):
        subtotal = flight.base_fare * tickets
        discount = passenger.calculate_discount(subtotal)  # polymorphic call
        return subtotal, discount, subtotal - discount

    # ---------- booking ----------
    def confirm_booking(self, flight, passenger, tickets):
        subtotal, discount, final = self.calculate_fare(flight, passenger, tickets)
        if not flight.reserve_seats(tickets):
            raise ValueError("Not enough seats available.")
        booking = Booking(f"BK{self.__next_id}", flight, passenger,
                          tickets, subtotal, discount, final)
        self.__next_id += 1
        self.__bookings.append(booking)
        return booking

    def book_flight(self):
        code = input("Enter flight code: ")
        name = input("Enter passenger name: ")
        age = input("Enter age: ")
        ptype = input("Passenger type (Regular/Student): ")
        tickets = input("Enter number of tickets: ")
        try:
            flight, passenger, count = self.validate_booking_details(
                code, name, age, ptype, tickets)
            booking = self.confirm_booking(flight, passenger, count)
        except ValueError as error:
            print(f"\nBooking failed: {error}")
            print("No booking was created. Available seats remain unchanged.")
            return
        print("\nBooking confirmed!")
        booking.display_summary()

    def view_booking(self):
        if not self.__bookings:
            print("\nNo booking found. Please book a flight first (option 2).")
            return
        print("\n--- Most Recent Booking ---")
        self.__bookings[-1].display_summary()

    # ---------- menu ----------
    def run(self):
        print("Welcome to Kiran Air Booking")
        while True:
            print("\n1. View Flights\n2. Book Flight\n3. View Booking\n4. Exit")
            choice = input("Enter choice: ").strip()
            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3 or 4.")
