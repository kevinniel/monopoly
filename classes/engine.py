from classes.board import Board
from classes.player import Player

class Engine:

    def __init__(self):
        # instanciate board
        self.board = Board()
        self.players = []
        self.player_count = 0
        self.playing = 0
        self.launch_game()
    
    def launch_game(self):
        # create players
        self._create_players()

        # start game
        self.start_round()

    def start_round(self):
        # affichage de l'état du joueur
        self.players[self.playing].print_state(self.board)
        # lancement des dés
        self.board.dices.launch_dices()
        # déplacement du joueur
        self.players[self.playing].move_count(self.board)
        # TODO => ACTIONS
        # tour suivant
        self._next_player()

    def _next_player(self):
        if self.board.dices.is_double:
            # si le dernier coup est un double le même joueur rejoue
            self.start_round()
        else:
            # sinon on passe au joueur suivant
            self.playing += 1
            if self.playing == len(self.players):
                self.playing = 0
            self.start_round()

    def _create_players(self):
        self._add_player()
        while self.player_count < 4:
            add_another_player = input("souhaitez vous ajouter un autre joueur ? (o/n) ")
            if add_another_player == "o":
                self._add_player()
            else:
                self.player_count = 4

    def _add_player(self):
        name = input("saisissez le nom du joueur : ")
        self.players.append(Player(name))
        self.player_count += 1