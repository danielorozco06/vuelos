import webbrowser

base_url = "https://www.espanol.skyscanner.com/transporte/vuelos"
initial_date = "240501"
final_date = "240508"
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

# Generate the endpoints dynamically
urls = [
    f"{base_url}/{airports['source']}/{target}/{initial_date}/{final_date}"
    for target in airports["targets"]
]

# Open each URL in a new tab
for url in urls:
    print(url)
    webbrowser.open_new_tab(url)
