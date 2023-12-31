"""
File with constants
"""

national_airports = [
    {
        "code": "MDE",
        "name": "Jose Maria Cordova International Airport",
        "city": "Medellin",
        "country": "Colombia",
    },
    {
        "code": "BOG",
        "name": "El Dorado International Airport",
        "city": "Bogota",
        "country": "Colombia",
    },
    {
        "code": "CTG",
        "name": "Rafael Nunez International Airport",
        "city": "Cartagena",
        "country": "Colombia",
    },
    # {
    #     "code": "PEI",
    #     "name": "Matecana International Airport",
    #     "city": "Pereira",
    #     "country": "Colombia",
    # },
    # {
    #     "code": "AXM",
    #     "name": "El Eden International Airport",
    #     "city": "Armenia",
    #     "country": "Colombia",
    # },
    {
        "code": "CLO",
        "name": "Alfonso Bonilla Aragon International Airport",
        "city": "Cali",
        "country": "Colombia",
    },
    {
        "code": "BAQ",
        "name": "Ernesto Cortissoz International Airport",
        "city": "Barranquilla",
        "country": "Colombia",
    },
    {
        "code": "ADZ",
        "name": "Gustavo Rojas Pinilla International Airport",
        "city": "San Andres",
        "country": "Colombia",
    },
    {
        "code": "LET",
        "name": "Alfredo Vasquez Cobo International Airport",
        "city": "Leticia",
        "country": "Colombia",
    },
    {
        "code": "BGA",
        "name": "Palonegro International Airport",
        "city": "Bucaramanga",
        "country": "Colombia",
    },
    # {
    #     "code": "CUC",
    #     "name": "Camilo Daza International Airport",
    #     "city": "Cucuta",
    #     "country": "Colombia",
    # },
    # {"code": "EYP", "name": "El Yopal Airport", "city": "Yopal", "country": "Colombia"},
    # {
    #     "code": "MZL",
    #     "name": "La Nubia Airport",
    #     "city": "Manizales",
    #     "country": "Colombia",
    # },
    {
        "code": "NVA",
        "name": "Benito Salas Airport",
        "city": "Neiva",
        "country": "Colombia",
    },
    {
        "code": "PPN",
        "name": "Guillermo Leon Valencia Airport",
        "city": "Popayan",
        "country": "Colombia",
    },
    {
        "code": "PSO",
        "name": "Antonio Narino Airport",
        "city": "Pasto",
        "country": "Colombia",
    },
    {
        "code": "RCH",
        "name": "Almirante Padilla Airport",
        "city": "Riohacha",
        "country": "Colombia",
    },
    {
        "code": "SMR",
        "name": "Simon Bolivar International Airport",
        "city": "Santa Marta",
        "country": "Colombia",
    },
    # {
    #     "code": "VVC",
    #     "name": "Vanguardia Airport",
    #     "city": "Villavicencio",
    #     "country": "Colombia",
    # },
]

international_airports = [
    {
        "code": "MDE",
        "name": "Jose Maria Cordova International Airport",
        "city": "Medellin",
        "country": "Colombia",
    },
    {
        "code": "PTY",
        "name": "Tocumen International Airport",
        "city": "Ciudad de Panama",
        "country": "Panama",
    },
    {
        "code": "CUN",
        "name": "Cancun International Airport",
        "city": "Cancun",
        "country": "Mexico",
    },
    # {
    #     "code": "MEX",
    #     "name": "Mexico City International Airport",
    #     "city": "Ciudad de Mexico",
    #     "country": "Mexico",
    # },
    # {
    #     "code": "SDQ",
    #     "name": "Santo domingo Airport",
    #     "city": "Santo domingo",
    #     "country": "Dominican Republic",
    # }
    {
        "code": "PUJ",
        "name": "Punta Cana Airport",
        "city": "Punta cana",
        "country": "Dominican Republic",
    },
    {
        "code": "HAV",
        "name": "Jose Marti International Airport",
        "city": "La habana",
        "country": "Cuba",
    },
    {
        "code": "AUA",
        "name": "Queen Beatrix International Airport",
        "city": "Oranjestad",
        "country": "Aruba",
    },
    {
        "code": "CUR",
        "name": "Hato International Airport",
        "city": "Willemstad",
        "country": "Curacao",
    },
    {
        "code": "SJO",
        "name": "Juan Santamaria International Airport",
        "city": "San Jose",
        "country": "Costa Rica",
    },
    # {
    #     "code": "UIO",
    #     "name": "Mariscal Sucre International Airport",
    #     "city": "Quito",
    #     "country": "Ecuador",
    # },
    # {
    #     "code": "MIA",
    #     "name": "Miami International Airport",
    #     "city": "Miami",
    #     "country": "United States",
    # },
    # {
    #     "code": "MCO",
    #     "name": "Orlando International Airport",
    #     "city": "Orlando",
    #     "country": "United States",
    # },
    {
        "code": "LIM",
        "name": "Jorge Chávez International Airport",
        "city": "Lima",
        "country": "Peru",
    },
    # {
    #     "code": "CUZ",
    #     "name": "Alejandro Velasco Astete International Airport",
    #     "city": "Cusco",
    #     "country": "Peru",
    # },
    # {
    #     "code": "ASU",
    #     "name": "Silvio Pettirossi International Airport",
    #     "city": "asuncion",
    #     "country": "Paraguay",
    # },
    # {
    #     "code": "MVD",
    #     "name": "Carrasco International Airport",
    #     "city": "montevideo",
    #     "country": "Uruguay",
    # },
    # {
    #     "code": "SCL",
    #     "name": "Arturo Merino Benítez International Airport",
    #     "city": "santiago de chile",
    #     "country": "Chile",
    # },
    # {
    #     "code": "LPB",
    #     "name": "Aeropuerto Internacional El Alto",
    #     "city": "la paz",
    #     "country": "Bolivia",
    # },
    # {
    #     "code": "GIG",
    #     "name": "Aeropuerto Internacional de Galeão",
    #     "city": "rio de janerio",
    #     "country": "Brazil",
    # },
    # {
    #     "code": "EZE",
    #     "name": "Aeropuerto Internacional Ministro Pistarini",
    #     "city": "buenos aires",
    #     "country": "Argentina",
    # },
    # {
    #     "code": "MAD",
    #     "name": "Madrid Barajas Airport",
    #     "city": "madrid",
    #     "country": "Spain",
    # },
    # {
    #     "code": "LON",
    #     "name": "London International Airport",
    #     "city": "londres",
    #     "country": "England",
    # },
]
