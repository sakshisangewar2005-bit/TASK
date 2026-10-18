"""Console-based cab booking chatbot for Kiran Academy Task 02."""

import random

CAB_RATES = {
    "1": ("Auto", 12),
    "2": ("Sedan", 18),
    "3": ("SUV", 25),
}

ROUTES = {
    "1": {"source": "Pune Station", "destination": "Shivajinagar", "distance": 5},
    "2": {"source": "Swargate", "destination": "Kothrud", "distance": 8},
    "3": {"source": "Hinjawadi", "destination": "Wakad", "distance": 10},
}


def get_valid_choice(prompt, valid_choices):
    """Keep asking until the user enters one of the listed choices."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")


def book_ride():
    print("\nChoose a cab type:")
    for number, (cab_name, rate) in CAB_RATES.items():
        print(f"{number}. {cab_name} (Rs. {rate}/km)")

    cab_choice = get_valid_choice("Enter your choice (1-3): ", CAB_RATES)
    cab_name, rate_per_km = CAB_RATES[cab_choice]

    print("\nChoose a route:")
    for number, route in ROUTES.items():
        print(
            f"{number}. {route['source']} to {route['destination']} "
            f"({route['distance']} km)"
        )

    route_choice = get_valid_choice("Enter your choice (1-3): ", ROUTES)
    route = ROUTES[route_choice]
    fare = rate_per_km * route["distance"]

    print("\n--- Ride fare ---")
    print(f"Cab type: {cab_name}")
    print(f"Source: {route['source']}")
    print(f"Destination: {route['destination']}")
    print(f"Distance: {route['distance']} km")
    print(f"Rate: Rs. {rate_per_km}/km")
    print(f"Total fare: Rs. {fare}")

    print("\n1. Confirm & Share OTP")
    print("2. Cancel Ride")
    confirmation = get_valid_choice("Enter your choice (1-2): ", {"1", "2"})

    if confirmation == "2":
        print("Ride cancelled. No OTP was shared.")
        return

    otp = random.randint(1000, 9999)
    print(f"\nYour 4-digit OTP is: {otp}")
    print("Once the OTP is shared, this ride cannot be cancelled.")
    print("Booking confirmed. Thank you for booking with us!")


def main():
    while True:
        print("\n=== Cab Booking Chatbot ===")
        print("1. Book Ride")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            book_ride()
        elif choice == "2":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
