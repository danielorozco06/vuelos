"""
Help with the planning of a trip
"""

import constants

base_url = "https://www.espanol.skyscanner.com/transporte/vuelos"
initial_date = "240506"
final_date = "240514"


airport_mode = ""
airports = []

while airport_mode != "nac" and airport_mode != "nonac":
    airport_mode = input("\nIngresar modo de aeropuerto (nac/nonac): ")
    if airport_mode == "nac":
        print("\n>>>Aeropuertos nacionales")
        airports = constants.national_airports
    elif airport_mode == "nonac":
        print("\n>>>Aeropuertos internacionales")
        airports = constants.international_airports
    else:
        print("!!!Modo de aeropuerto no valido!!!")

airport_codes = [airport["code"] for airport in airports]

# Print all airports
for airport in airports:
    print(
        f'{airport["code"]} : {airport["name"]} - {airport["city"]} - {airport["country"]}'
    )


source_airport = ""
target_airports = []

# Loop for source airport
while True:
    # Ask user for source airport
    source_airport = input("\nIngresar codigo aeropuerto origen: ")

    # Remove spaces and convert to uppercase
    source_airport = source_airport.strip().upper()

    # Check if source airport is valid
    if source_airport in airport_codes:
        break
    else:
        print("!!!Airport code not valid!!!")

# Loop for target airports
while True:
    # Ask user for target airports
    target_airports = input(
        "\nIngresar codigos aeropuertos destino (separados por coma): "
    ).split(",")

    # Remove spaces and convert to uppercase
    target_airports = [airport.strip().upper() for airport in target_airports]

    # Check if target airports are valid
    if all(airport.strip() in airport_codes for airport in target_airports):
        # Get all objects in airports list that match with target airports
        target_airports = [
            airport for airport in airports if airport["code"] in target_airports
        ]
        break
    else:
        print("!!!Airport codes not valids!!!")

# Open each URL in a new tab
for target_airport in target_airports:
    print(f"\n####### Desde {source_airport} hasta {target_airport['code']} #######")

    print("\n>>> Vuelos")
    url_flights = f"{base_url}/{source_airport}/{target_airport['code']}/{initial_date}/{final_date}"
    print(url_flights)

    print("\n>>> Hotel")
    url_hotel = (
        f"https://www.airbnb.com.co/s/{target_airport['code']}/homes?"
        "&checkin=2024-04-05"
        "&checkout=2024-04-15"
        "&adults=2"
    )
    print(url_hotel)

    print("\n>>> Itinerario (https://chat.openai.com)")
    print(
        f"Crear un itinerario detallado del viaje teniendo en cuenta la siguiente información:"
        f"\n-Dos personas"
        f"\n-Aeropuerto de origen: {source_airport}"
        f"\n-Aeropuerto de destino: {target_airport['code']}"
        f"\n-Fecha de ida: {initial_date}"
        f"\n-Fecha de regreso: {final_date}"
        "\n-Incluir horas de cada actividad"
        "\n-Excluir visitas a centros comerciales, tiempo libre y tiempo de relax"
        "\n-Indicar los costos aproximados en USD de cada actividad y el costo total al final"
        "\n-Incluir los costos de transporte entre cada lugar y el costo del desayuno, almuerzo y cena"
        "\n-Incluir pueblos, ciudades muy cercanas y mercados locales"
        "\n-Incluir los lugares más turísticos"
    )
