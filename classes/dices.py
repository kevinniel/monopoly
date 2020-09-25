# coding: utf-8

import random

class Dices:

    def __init__(self):
        self.first = None
        self.second = None
        self.is_double = False
    
    def launch_dices(self):
        self._set_values()
        self._is_double()
        return self
    
    def _set_values(self):
        self.first = random.randint(1, 6)
        self.second = random.randint(1,6)

    def _is_double(self):
        self.is_doble = False
        if self.first == self.second:
            self.is_double = True
