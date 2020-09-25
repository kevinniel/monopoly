from config.settings import HOUSES, HOTELS, BANK_MONEY

class Bank:

    def __init__(self):
        self.houses = HOUSES
        self.hotels = HOTELS
        self.money = BANK_MONEY
        # self.cards = []