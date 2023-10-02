"""
File to open all the URLs of the flights from Medellin to the cities
"""

import webbrowser

base_url = "https://www.espanol.skyscanner.com/transporte/vuelos"
initial_date = "240506"
final_date = "240514"
airports = {
    #  "Jose Maria Cordova International Airport - Colombia"
    "source": "MDE",
    "targets": [
        # "Ciudad de Panama International Airport - Panama"
        "PTY",
        # "Cancun International Airport - Mexico"
        "CUN",
        # "Ciudad de Mexico International Airport - Mexico"
        "MEX",
        # "Punta Cana International Airport - Dominican Republic"
        "PUJ",
        # "Santo Domingo Airport - Dominican Republic"
        "SDQ",
        # "Jose Marti International Airport - Cuba"
        "HAV",
        # "Queen Beatrix International Airport - Aruba"
        "AUA",
        # "Hato International Airport - Curacao"
        "CUR",
        # "Juan Santamaria International Airport - Costa Rica"
        "SJO",
        # "Quito International Airport - Ecuador"
        "UIO",
        # "Miami International Airport - United States"
        "MIA",
        # "Orlando International Airport - United States"
        "MCO",
        # "Lima International Airport - Peru"
        "LIM",
        # "Cusco International Airport - Peru"
        "CUZ",
        # "Asuncion International Airport - Paraguay"
        "ASU",
        # "Montevideo International Airport - Uruguay"
        "MVD",
        # "Santiago de Chile International Airport - Chile"
        "SCL",
        # "La paz International Airport - Bolivia"
        "LPB",
        # "Rio de Janeiro International Airport - Brazil"
        "GIG",
        # "Buenos Aires International Airport - Argentina"
        "EZE",
        # "Madrid International Airport - Spain"
        "MAD",
        # "Londres International Airport - England"
        "LON",
    ],
}


# Open each URL in a new tab
for target in airports["targets"]:
    url = f"{base_url}/{airports['source']}/{target}/{initial_date}/{final_date}"

    webbrowser.open_new_tab(url)

    print(
        f"\nCrear un itinerario detallado del viaje teniendo en cuenta la siguiente información:"
        f"\n-Dos personas"
        f"\n-Aeropuerto de origen: {airports['source']}"
        f"\n-Aeropuerto de destino: {target}"
        f"\n-Fecha de ida: {initial_date}"
        f"\n-Fecha de regreso: {final_date}"
        "\n-Incluir horas de cada actividad"
        "\n-Excluir visitas a centros comerciales y tiempo libre"
        "\n-Indicar los costos aproximados en USD de cada actividad y el costo total al final"
        "\n-Incluir los costos de transporte entre cada lugar y el costo del desayuno, almuerzo y cena"
        "\n-Incluir pueblos, ciudades muy cercanas y mercados locales"
        "\n-Incluir los lugares más turísticos"
    )
