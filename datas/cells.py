# coding: utf-8

CELLS = {
    1 : {
        "name" : "Case Depart",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 200,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    2 : {
        "name" : "Boulevard de Belleville",
        "buying_price" : 60,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 2,
            1 : 10,
            2 : 30,
            3 : 90,
            4 : 160,
            5 : 250,
        },
        "mortgage" : 30,
        "house_price" : 50,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    3 : {
        "name" : "Caisse de communauté",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    4 : {
        "name" : "Rue Lecourbe",
        "buying_price" : 60,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 4,
            1 : 20,
            2 : 60,
            3 : 180,
            4 : 320,
            5 : 450,
        },
        "mortgage" : 30,
        "house_price" : 50,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    5 : {
        "name" : "Impôts sur le revenu",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 200,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    6 : {
        "name" : "Gare Montparnasse",
        "buying_price" : 200,
        "station_prices" : {
            1 : 25,
            2 : 50,
            3 : 100,
            4 : 200
        },
        "cie_price" : None,
        "rent" : None,
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    7 : {
        "name" : "Rue de Vaugirard",
        "buying_price" : 100,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 6,
            1 : 30,
            2 : 90,
            3 : 270,
            4 : 400,
            5 : 550,
        },
        "mortgage" : 50,
        "house_price" : 50,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    8 : {
        "name" : "Chance",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : True,
        "draw_community" : False,
        "go_to_jail" : False
    },
    9 : {
        "name" : "Rue de Courcelles",
        "buying_price" : 100,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 6,
            1 : 30,
            2 : 90,
            3 : 270,
            4 : 400,
            5 : 550,
        },
        "mortgage" : 50,
        "house_price" : 50,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    10 : {
        "name" : "Avenue de la Republique",
        "buying_price" : 120,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 8,
            1 : 40,
            2 : 100,
            3 : 300,
            4 : 450,
            5 : 600,
        },
        "mortgage" : 60,
        "house_price" : 50,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    11 : {
        "name" : "Simple Visite",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    12 : {
        "name" : "Boulevard de la Vilette",
        "buying_price" : 140,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 10,
            1 : 50,
            2 : 150,
            3 : 450,
            4 : 625,
            5 : 750,
        },
        "mortgage" : 70,
        "house_price" : 100,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    13 : {
        "name" : "Compagnie de distribution d'electricite",
        "buying_price" : 150,
        "station_prices" : None,
        "cie_price" : {
            0 : 4,
            1 : 10
        },
        "rent" : None,
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    14 : {
        "name" : "Avenue de Neuilly",
        "buying_price" : 140,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 10,
            1 : 50,
            2 : 150,
            3 : 450,
            4 : 625,
            5 : 750,
        },
        "mortgage" : 70,
        "house_price" : 100,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    15 : {
        "name" : "Rue de Paradis",
        "buying_price" : 160,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 12,
            1 : 60,
            2 : 180,
            3 : 500,
            4 : 700,
            5 : 900,
        },
        "mortgage" : 80,
        "house_price" : 100,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    16 : {
        "name" : "Gare de Lyon",
        "buying_price" : 200,
        "station_prices" : {
            1 : 25,
            2 : 50,
            3 : 100,
            4 : 200
        },
        "cie_price" : None,
        "rent" : None,
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    17 : {
        "name" : "Avenue Mozart",
        "buying_price" : 180,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 14,
            1 : 70,
            2 : 200,
            3 : 550,
            4 : 700,
            5 : 900,
        },
        "mortgage" : 90,
        "house_price" : 100,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    18 : {
        "name" : "Caisse de Communaute",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : True,
        "go_to_jail" : False
    },
    19 : {
        "name" : "Boulevard Saint Michel",
        "buying_price" : 180,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 14,
            1 : 70,
            2 : 200,
            3 : 550,
            4 : 700,
            5 : 900,
        },
        "mortgage" : 90,
        "house_price" : 100,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    20 : {
        "name" : "Place Pigalle",
        "buying_price" : 200,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 16,
            1 : 80,
            2 : 220,
            3 : 600,
            4 : 800,
            5 : 1000,
        },
        "mortgage" : 100,
        "house_price" : 100,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    21 : {
        "name" : "Parc Gratuit",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    22 : {
        "name" : "Avenue Matignon",
        "buying_price" : 220,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 18,
            1 : 90,
            2 : 250,
            3 : 700,
            4 : 875,
            5 : 1050,
        },
        "mortgage" : 110,
        "house_price" : 150,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    23 : {
        "name" : "Chance",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : True,
        "draw_community" : False,
        "go_to_jail" : False
    },
    24 : {
        "name" : "Boulevard Malherbes",
        "buying_price" : 220,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 18,
            1 : 90,
            2 : 250,
            3 : 700,
            4 : 875,
            5 : 1050,
        },
        "mortgage" : 110,
        "house_price" : 150,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    25 : {
        "name" : "Avenue Henri-Martin",
        "buying_price" : 240,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 20,
            1 : 100,
            2 : 300,
            3 : 750,
            4 : 925,
            5 : 1100,
        },
        "mortgage" : 120,
        "house_price" : 150,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    26 : {
        "name" : "Gare du Nord",
        "buying_price" : 200,
        "station_prices" : {
            1 : 25,
            2 : 50,
            3 : 100,
            4 : 200
        },
        "cie_price" : None,
        "rent" : None,
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    27 : {
        "name" : "Faubourg Saint-Honore",
        "buying_price" : 260,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 22,
            1 : 110,
            2 : 330,
            3 : 800,
            4 : 975,
            5 : 1150,
        },
        "mortgage" : 130,
        "house_price" : 150,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    28 : {
        "name" : "Place de la Bourse",
        "buying_price" : 260,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 22,
            1 : 110,
            2 : 330,
            3 : 800,
            4 : 975,
            5 : 1150,
        },
        "mortgage" : 130,
        "house_price" : 150,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    29 : {
        "name" : "Compagnie des eaux",
        "buying_price" : 150,
        "station_prices" : None,
        "cie_price" : {
            0 : 4,
            1 : 10
        },
        "rent" : None,
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    30 : {
        "name" : "Rue la Fayette",
        "buying_price" : 280,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 24,
            1 : 120,
            2 : 360,
            3 : 850,
            4 : 1025,
            5 : 1200,
        },
        "mortgage" : 140,
        "house_price" : 150,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    31 : {
        "name" : "Allez en Prison",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 200,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : True
    },
    32 : {
        "name" : "Avenue de Breteuil",
        "buying_price" : 300,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 26,
            1 : 130,
            2 : 390,
            3 : 900,
            4 : 1100,
            5 : 1275,
        },
        "mortgage" : 150,
        "house_price" : 200,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    33 : {
        "name" : "Avenue Foch",
        "buying_price" : 300,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 26,
            1 : 130,
            2 : 390,
            3 : 900,
            4 : 1100,
            5 : 1275,
        },
        "mortgage" : 150,
        "house_price" : 200,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    34 : {
        "name" : "Caisse de communauté",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    35 : {
        "name" : "Boulevard des Capucines",
        "buying_price" : 320,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 28,
            1 : 150,
            2 : 450,
            3 : 1000,
            4 : 1200,
            5 : 1400,
        },
        "mortgage" : 160,
        "house_price" : 200,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    36 : {
        "name" : "Gare Saint-Lazarre",
        "buying_price" : 200,
        "station_prices" : {
            1 : 25,
            2 : 50,
            3 : 100,
            4 : 200
        },
        "cie_price" : None,
        "rent" : None,
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    37 : {
        "name" : "Chance",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : True,
        "draw_community" : False,
        "go_to_jail" : False
    },
    38 : {
        "name" : "Avenue des Champs Elysees",
        "buying_price" : 350,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 35,
            1 : 175,
            2 : 500,
            3 : 1100,
            4 : 1300,
            5 : 1500,
        },
        "mortgage" : 175,
        "house_price" : 200,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    39 : {
        "name" : "Taxe de luxe",
        "buying_price" : 0,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
        },
        "mortgage" : 0,
        "house_price" : 0,
        "money_win" : 0,
        "money_loose" : 100,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : False,
        "can_buy" : False,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    },
    40 : {
        "name" : "Rue de la paix",
        "buying_price" : 400,
        "station_prices" : None,
        "cie_price" : None,
        "rent" : {
            0 : 50,
            1 : 200,
            2 : 600,
            3 : 1400,
            4 : 1700,
            5 : 2000,
        },
        "mortgage" : 200,
        "house_price" : 200,
        "money_win" : 0,
        "money_loose" : 0,
        "is_mortgage" : False,
        "has_house" : 0,
        "has_hotel" : 0,
        "can_build" : True,
        "can_buy" : True,
        "draw_chance" : False,
        "draw_community" : False,
        "go_to_jail" : False
    }    
}

CELL_GROUPS = {
    101 : "Prison", # 11
    102 : "Les gares", # 6 + 16 + 26 + 36
    103 : "Les Cies", # 13 + 29
    104 : "Brun", # 2 + 4
    105 : "Bleu clair", # 7 + 9 + 10
    106 : "Violet", # 12 + 14 + 15
    107 : "Orange", # 17 + 19 + 20
    108 : "Rouge", # 22 + 24 + 25
    109 : "Jaune", # 27 + 28 + 30
    110 : "Vert", # 32 + 33 + 35
    111 : "Bleu fonce" # 38 + 40
}