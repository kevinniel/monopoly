# coding: utf-8

import random

from datas.cells import CELLS
from datas.community import COMMUNITY
from datas.chance import CHANCE

from classes.dices import Dices
from classes.community import Community
from classes.chance import Chance
from classes.bank import Bank

class Engine:

    def __init__(self):
        # print(CELLS)
        # print(COMMUNITY)
        # print(CHANCE)

        # create dices
        self.dices = Dices()

        # create community array to store community cards
        self.community = []
        self._init_communities()

        # create chance array to store chance cards
        self.chance = []
        self._init_chances()

        # create bank
        self.bank = Bank()

    def _init_communities(self):
        """ Method that init the community cards """
        # instanciation of objects
        self._instanciate_communities()
        # shuffle cards
        random.shuffle(self.community)

    def _instanciate_communities(self):
        """ Method that instanciate the community cards """
        for id, card in COMMUNITY.items():
            self.community.append(Community(id, card))

    def _init_chances(self):
        """ Method that init the chance cards """
        # instanciation of objects
        self._instanciate_chances()
        # shuffle cards
        random.shuffle(self.chance)

    def _instanciate_chances(self):
        for id, card in CHANCE.items():
            self.chance.append(Chance(id, card))