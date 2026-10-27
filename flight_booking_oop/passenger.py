"""Passenger classes: abstraction, inheritance and polymorphism."""
from abc import ABC, abstractmethod


class Passenger(ABC):
    """Abstract base class: every passenger type must provide a discount."""

    def __init__(self, name, age):
        self.__name = name      # private fields (encapsulation)
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @abstractmethod
    def get_discount_percentage(self):
        """Discount percentage for this passenger type (e.g. 10 for 10%)."""

    @abstractmethod
    def get_passenger_type(self):
        """Readable passenger type name."""

    def calculate_discount(self, subtotal):
        """Same method works for every subclass (polymorphism)."""
        return subtotal * self.get_discount_percentage() / 100


class RegularPassenger(Passenger):
    def get_discount_percentage(self):
        return 0

    def get_passenger_type(self):
        return "Regular"


class StudentPassenger(Passenger):
    def get_discount_percentage(self):
        return 10

    def get_passenger_type(self):
        return "Student"
