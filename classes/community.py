class Community:

    def __init__(self, id, params):
        self.id = id
        self.text = params["text"]
        self.win_money = params["win_money"]
        self.loose_money = params["loose_money"]
        self.players_pay_you = params["players_pay_you"]
        self.draw_chance = params["draw_chance"]

