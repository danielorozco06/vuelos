"""
Help with the planning of a trip
"""

import constants
from datetime import datetime
from typing import Union


def is_valid_date(date: str) -> bool:
    """
    Check if date is valid
    """
    try:
        # Try to convert the string into a datetime object
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        # If it raises a ValueError, the string is not a valid date
        return False


def convert_date_format(date: str) -> str:
    """
    Convert date from 'YYYY-MM-DD' to 'YYMMDD'
    """
    try:
        # Convert the string into a datetime object
        dt = datetime.strptime(date, "%Y-%m-%d")

        # Format the datetime object into the desired format
        return dt.strftime("%y%m%d")
    except ValueError:
        # If it raises a ValueError, the string is not a valid date
        return "Invalid date"


def get_date_input(prompt: str) -> str:
    """
    Prompts the user for a date input until a valid date is entered.
    """
    while True:
        date = input(prompt)
        if is_valid_date(date):
            return date
        print("Invalid date. Please try again.")


def get_airport_mode() -> str:
    """
    A function to get the airport mode from user input.
    """
    while True:
        airport_mode = input("\nIngresar modo de aeropuerto (nac/nonac): ")
        if airport_mode in ["nac", "nonac"]:
            return airport_mode
        print("!!!Modo de aeropuerto no valido!!!")


def validate_airport_codes(
    airport_codes: list[str], multiple: bool = False
) -> Union[str, list[str]]:
    """
    Validates user input airport codes against a provided list of valid codes.
    """
    while True:
        input_prompt = (
            "\nIngresar codigo aeropuerto origen: "
            if not multiple
            else "\nIngresar codigos aeropuertos destino (separados por coma): "
        )
        input_codes = [code.strip().upper() for code in input(input_prompt).split(",")]

        if all(code in airport_codes for code in input_codes):
            return input_codes if multiple else input_codes[0]

        print("!!!Airport code(s) not valid!!!")


def get_airports(airport_mode: str) -> list[dict[str, str]]:
    """
    Function to get the airports based on the airport mode.
    """
    return (
        constants.national_airports
        if airport_mode == "nac"
        else constants.international_airports
    )


def print_airports(airports: list[dict[str, str]]) -> None:
    """
    Prints the details of each airport in the provided list.
    """
    for airport in airports:
        print(
            f'{airport["code"]} : {airport["name"]} - {airport["city"]} - {airport["country"]}'
        )


def process_flights(
    source_airport_code: str,
    target_airport_code: str,
    initial_date: str,
    final_date: str,
) -> None:
    """
    Processes flight information and prints the URL for flight search.
    """
    print("\n>>> Vuelos")
    base_url = "https://www.espanol.skyscanner.com/transporte/vuelos"
    url_flights = (
        f"{base_url}/"
        f"{source_airport_code}/"
        f"{target_airport_code}/"
        f"{convert_date_format(initial_date)}/"
        f"{convert_date_format(final_date)}"
    )
    print(url_flights)


def process_hotel(
    target_airport_code: str,
    airports: list[dict[str, str]],
    initial_date: str,
    final_date: str,
) -> None:
    """
    This function generates and prints the URL for hotel search on Airbnb based on given \
    airport code, date range and city.
    """
    print("\n>>> Hotel")
    target_city = next(
        (
            airport["city"]
            for airport in airports
            if airport["code"] == target_airport_code
        ),
        None,
    )

    url_hotel = (
        f"https://www.airbnb.com.co/s/{target_city}/homes?"
        f"&checkin={initial_date}"
        f"&checkout={final_date}"
        "&adults=2"
    )
    print(url_hotel)


def process_itinerary(
    source_airport_code: str,
    target_airport_code: str,
    initial_date: str,
    final_date: str,
) -> None:
    """
    This function generates a detailed travel itinerary based on the provided parameters.
    """
    print("\n>>> Itinerario (https://chat.openai.com)")
    print(
        f"Crear un itinerario detallado del viaje teniendo en cuenta la siguiente información:"
        f"\n-Dos personas"
        f"\n-Aeropuerto de origen: {source_airport_code}"
        f"\n-Aeropuerto de destino: {target_airport_code}"
        f"\n-Fecha de ida: {initial_date}"
        f"\n-Fecha de regreso: {final_date}"
        "\n-Incluir horas de cada actividad"
        "\n-Excluir visitas a centros comerciales, tiempo libre y tiempo de relax"
        "\n-Indicar los costos aproximados en USD de cada actividad y el costo total al final"
        "\n-Incluir los costos de transporte entre cada lugar y el costo del desayuno, almuerzo y cena"
        "\n-Incluir pueblos, ciudades muy cercanas y mercados locales"
        "\n-Incluir los lugares más turísticos"
    )


def main() -> None:
    """
    Main function
    """
    init_date = get_date_input("\nIngresar fecha de ida (yyyy-mm-dd): ")
    final_date = get_date_input("\nIngresar fecha de regreso (yyyy-mm-dd): ")

    airport_mode = get_airport_mode()
    airports = get_airports(airport_mode)

    print_airports(airports)

    airport_codes = [airport["code"] for airport in airports]
    source_airport_code = validate_airport_codes(airport_codes)
    target_airports_codes = validate_airport_codes(airport_codes, multiple=True)

    for target_airport_code in target_airports_codes:
        print(f"\n### Desde {source_airport_code} hasta {target_airport_code} ###")
        process_flights(source_airport_code, target_airport_code, init_date, final_date)
        process_hotel(target_airport_code, airports, init_date, final_date)
        process_itinerary(
            source_airport_code, target_airport_code, init_date, final_date
        )


if __name__ == "__main__":
    main()
