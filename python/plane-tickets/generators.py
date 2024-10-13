"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number: int):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = "ABCDE"
    counter = 0
    while counter < number:
        yield seats[counter % 4]
        counter += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_letters = generate_seat_letters(number)
    curr_row = 1
    seat_number = 0

    while seat_number < number:
        if curr_row == 13:
            curr_row += 1
            continue

        for _ in range(4):
            if seat_number < number:
                yield f"{curr_row}{next(seat_letters)}"
                seat_number += 1
        curr_row += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield f"{seat}{flight_id}".ljust(12, "0")
