# Cab Booking Chatbot (Python)

A beginner-friendly, console-based solution for Kiran Academy Task 02.

## Requirements

- Python 3
- No external packages are required

## Run

Open a terminal in this folder and run:

```bash
python chatbot.py
```

On some systems, use `python3 chatbot.py` instead.

## Features

- Repeats the main menu until the user selects Exit.
- Includes the three predefined routes and fixed distances from the task.
- Calculates fares using Auto (Rs. 12/km), Sedan (Rs. 18/km), or SUV (Rs. 25/km).
- Validates menu, cab, route, and confirmation choices.
- Allows cancellation before OTP sharing; cancelled rides receive no OTP.
- Generates and displays a 4-digit OTP only after confirmation, then clearly states that cancellation is locked.

## Example calculation

For Sedan on Hinjawadi to Wakad: 10 km x Rs. 18/km = Rs. 180.
