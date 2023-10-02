"""
Help with the planning of a trip
"""

base_url = "https://www.espanol.skyscanner.com/transporte/vuelos"
initial_date = "240506"
final_date = "240514"

airport_national_codes = [
    "MDE: Jose Maria Cordova International Airport - Medellin - Colombia",
    "BOG: El Dorado International Airport - Bogota - Colombia",
    "CTG: Rafael Nunez International Airport - Cartagena - Colombia",
    "PEI: Matecana International Airport - Pereira - Colombia",
    "AXM: El Eden International Airport - Armenia - Colombia",
    "CLO: Alfonso Bonilla Aragon International Airport - Cali - Colombia",
    "BAQ: Ernesto Cortissoz International Airport - Barranquilla - Colombia",
    "ADZ: Gustavo Rojas Pinilla International Airport - San Andres - Colombia",
    "LET: Alfredo Vasquez Cobo International Airport - Leticia - Colombia",
    "BGA: Palonegro International Airport - Bucaramanga - Colombia",
    "CUC: Camilo Daza International Airport - Cucuta - Colombia",
    "EYP: El Yopal Airport - Yopal - Colombia",
    "MTR: Los Garzones Airport - Monteria - Colombia",
    "MZL: La Nubia Airport - Manizales - Colombia",
    "NVA: Benito Salas Airport - Neiva - Colombia",
    "PPN: Guillermo Leon Valencia Airport - Popayan - Colombia",
    "PSO: Antonio Narino Airport - Pasto - Colombia",
    "RCH: Almirante Padilla Airport - Riohacha - Colombia",
    "SMR: Simon Bolivar International Airport - Santa Marta - Colombia",
    "VUP: Alfonso Lopez Pumarejo Airport - Valledupar - Colombia",
    "VVC: Vanguardia Airport - Villavicencio - Colombia",
]

airport_international_codes = [
    "MDE: Jose Maria Cordova International Airport - Medellin - Colombia",
    "PTY: Ciudad de Panama International Airport - Panama",
    "CUN: Cancun International Airport - Mexico",
    "MEX: Ciudad de Mexico International Airport - Mexico",
    "PUJ: Punta Cana International Airport - Dominican Republic",
    "SDQ: Santo Domingo Airport - Dominican Republic",
    "HAV: Jose Marti International Airport - Cuba",
    "AUA: Queen Beatrix International Airport - Aruba",
    "CUR: Hato International Airport - Curacao",
    "SJO: Juan Santamaria International Airport - Costa Rica",
    "UIO: Quito International Airport - Ecuador",
    "MIA: Miami International Airport - United States",
    "MCO: Orlando International Airport - United States",
    "LIM: Lima International Airport - Peru",
    "CUZ: Cusco International Airport - Peru",
    "ASU: Asuncion International Airport - Paraguay",
    "MVD: Montevideo International Airport - Uruguay",
    "SCL: Santiago de Chile International Airport - Chile",
    "LPB: La paz International Airport - Bolivia",
    "GIG: Rio de Janeiro International Airport - Brazil",
    "EZE: Buenos Aires International Airport - Argentina",
    "MAD: Madrid International Airport - Spain",
    "LON: Londres International Airport - England",
]

airport_mode = ""
airports = []

while airport_mode != "nac" and airport_mode != "nonac":
    airport_mode = input("\nIngresar modo de aeropuerto (nac/nonac): ")
    if airport_mode == "nac":
        print("\n>>>Aeropuertos nacionales")
        airports = airport_national_codes
    elif airport_mode == "nonac":
        print("\n>>>Aeropuertos internacionales")
        airports = airport_international_codes
    else:
        print("!!!Modo de aeropuerto no valido!!!")

airport_codes = [airport.split(":")[0] for airport in airports]

# Print all airports
for airport in airports:
    print(airport)

source_airport = ""
target_airports = []

# Loop for source airport
while True:
    # Ask user for source airport
    source_airport = input("\nIngresar codigo aeropuerto origen: ")
    source_airport = source_airport.upper()

    # Check if source airport is valid
    if source_airport in airport_codes:
        break
    else:
        print("!!!Airport code not valid!!!")

# Loop for target airports
while True:
    # Ask user for target airports
    target_airports = input(
        "\nIngresar codigo aeropuerto destino (separados por coma): "
    ).split(",")
    target_airports = [airport.strip().upper() for airport in target_airports]

    # Check if target airports are valid
    if all(airport.strip() in airport_codes for airport in target_airports):
        break
    else:
        print("!!!Airport codes not valids!!!")

# Open each URL in a new tab
for target_airport in target_airports:
    print("\n##################################################################")
    print(f"Desde {source_airport} hasta {target_airport}")

    print("\n>>>Vuelos")
    url = f"{base_url}/{source_airport}/{target_airport}/{initial_date}/{final_date}"
    print(url)

    print("\n>>>Hotel")

    print("\n>>>Itinerario")
    print(
        f"\nCrear un itinerario detallado del viaje teniendo en cuenta la siguiente información:"
        f"\n-Dos personas"
        f"\n-Aeropuerto de origen: {source_airport}"
        f"\n-Aeropuerto de destino: {target_airport}"
        f"\n-Fecha de ida: {initial_date}"
        f"\n-Fecha de regreso: {final_date}"
        "\n-Incluir horas de cada actividad"
        "\n-Excluir visitas a centros comerciales, tiempo libre y tiempo de relax"
        "\n-Indicar los costos aproximados en USD de cada actividad y el costo total al final"
        "\n-Incluir los costos de transporte entre cada lugar y el costo del desayuno, almuerzo y cena"
        "\n-Incluir pueblos, ciudades muy cercanas y mercados locales"
        "\n-Incluir los lugares más turísticos"
    )
