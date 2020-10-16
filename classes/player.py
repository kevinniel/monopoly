from config.settings import START_MONEY

class Player:

    def __init__(self, name):
        self.money = START_MONEY
        self.name = name
        self.position = 0
        self.number_double = 0
        self.cards = []

    def print_state(self, board):
        print(
            f"joueur : {self.name} \n" \
            f"argent : {self.money} \n" \
            f"case :  {board.cells[self.position].name} \n"
        )

    def move_count(self, board):
        self.position += board.dices.total
        if self.position > 39:
            self.position -= 40
        print(
            f"le joueur a avancé de {board.dices.total} cases et se trouve \n"
            f"maintenant sur la case : {board.cells[self.position].name} \n"
        )
