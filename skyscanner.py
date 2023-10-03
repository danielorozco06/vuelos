"""
Help with the planning of a trip
"""

import os
import constants
import ast
from datetime import datetime
from typing import Union
from dotenv import load_dotenv

load_dotenv()


def get_airports(airport_mode: str) -> list[dict[str, str]]:
    """
    Function to get the airports based on the airport mode.
    """
    return (
        constants.national_airports
        if airport_mode == "NACIONAL"
        else constants.international_airports
    )


def validate_date(date: str) -> None:
    """
    Check if date is valid
    """
    try:
        # Try to convert the string into a datetime object
        datetime.strptime(date, "%Y-%m-%d")
        return
    except ValueError:
        raise ValueError(f"Invalid date {date}. Execution stopped.")


def validate_airport_mode(airport_mode: str) -> None:
    """
    Validate airport mode
    """
    airport_mode = airport_mode.upper()
    if airport_mode in ["NACIONAL", "INTERNACIONAL"]:
        return
    else:
        raise ValueError(f"Invalid airport mode {airport_mode}. Execution stopped.")


def validate_airport_codes(airport_codes: list[str], input_codes: list[str]) -> None:
    """
    Validates user input airport codes against a provided list of valid codes.
    """
    input_codes = [code.strip().upper() for code in input_codes]

    if all(code in airport_codes for code in input_codes):
        return
    else:
        raise ValueError("Invalid airport code(s). Execution stopped.")


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


def get_url_flight(
    source_airport_code: str,
    target_airport_code: str,
    initial_date: str,
    final_date: str,
) -> str:
    """
    Create URL for flight search.
    """
    base_url = "https://www.espanol.skyscanner.com/transporte/vuelos"
    return (
        f"{base_url}/"
        f"{source_airport_code}/"
        f"{target_airport_code}/"
        f"{convert_date_format(initial_date)}/"
        f"{convert_date_format(final_date)}"
    )


def get_city(airport_code: str, airports: list[dict[str, str]]) -> str:
    """
    This function returns the city of the airport.
    """
    return next(
        (airport["city"] for airport in airports if airport["code"] == airport_code),
        None,
    )


def get_url_hotel(
    target_airport_code: str,
    airports: list[dict[str, str]],
    initial_date: str,
    final_date: str,
) -> str:
    """
    Generate the URL for hotel search on Airbnb
    """
    target_city = get_city(target_airport_code, airports)
    encoded_target_city = target_city.replace(" ", "%20")

    return (
        f"https://www.airbnb.com.co/s/{encoded_target_city}/homes?"
        f"&checkin={initial_date}"
        f"&checkout={final_date}"
        "&adults=2"
    )


def create_itinerary(
    source_airport_code: str,
    target_airport_code: str,
    init_date: str,
    final_date: str,
) -> str:
    """
    This function generates a detailed travel itinerary based on the provided parameters.
    """
    return (
        f"Crear un itinerario detallado del viaje teniendo en cuenta la siguiente información:"
        f"\n-Dos personas"
        f"\n-Aeropuerto de origen: {source_airport_code}"
        f"\n-Aeropuerto de destino: {target_airport_code}"
        f"\n-Fecha de ida: {init_date}"
        f"\n-Fecha de regreso: {final_date}"
        "\n-Incluir horas de cada actividad"
        "\n-Excluir visitas a centros comerciales, tiempo libre y tiempo de relax"
        "\n-Indicar los costos aproximados en USD de cada actividad y el costo total al final"
        "\n-Incluir los costos de transporte entre cada lugar y el costo del desayuno, almuerzo y cena"
        "\n-Incluir pueblos, ciudades muy cercanas y mercados locales"
        "\n-Incluir los lugares más turísticos\n"
    )


def write_itinerary_to_file(
    source_airport_code: str,
    target_airport_code: str,
    init_date: str,
    final_date: str,
    url_flight: str,
    url_hotel: str,
    itinerary: str,
) -> None:
    """
    Writes the itinerary details to a file.
    """
    # Create output directory if not exists
    if not os.path.exists("output"):
        os.makedirs("output")

    # Format the filename
    filename = f"{init_date}_{final_date}.txt"

    # Open the file in append mode
    with open(os.path.join("output", filename), "a") as f:
        f.write(f"### De {source_airport_code} a {target_airport_code}")
        f.write(f"\n>>> Vuelos\n{url_flight}\n")
        f.write(f"\n>>> Hotel\n{url_hotel}\n")
        f.write(f"\n>>> Itinerario (https://chat.openai.com)\n{itinerary}\n")


def main() -> None:
    """
    Main function
    """
    init_date = os.getenv("INIT_DATE")
    final_date = os.getenv("FINAL_DATE")
    airport_mode = os.getenv("AIRPORT_MODE")
    source_code = ast.literal_eval(os.getenv("SOURCE_AIRPORT_CODE"))
    target_codes = ast.literal_eval(os.getenv("TARGET_AIRPORT_CODES"))

    airports = get_airports(airport_mode)
    airport_codes = [airport["code"] for airport in airports]

    validate_date(init_date)
    validate_date(final_date)
    validate_airport_mode(airport_mode)
    validate_airport_codes(airport_codes, source_code)
    validate_airport_codes(airport_codes, target_codes)

    for target_code in target_codes:
        url_flight = get_url_flight(source_code[0], target_code, init_date, final_date)
        url_hotel = get_url_hotel(target_code, airports, init_date, final_date)
        itinerary = create_itinerary(source_code[0], target_code, init_date, final_date)
        write_itinerary_to_file(
            source_code[0],
            target_code,
            init_date,
            final_date,
            url_flight,
            url_hotel,
            itinerary,
        )


if __name__ == "__main__":
    main()
