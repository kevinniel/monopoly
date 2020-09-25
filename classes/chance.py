class Chance:

    def __init__(self, id, params):
        self.id = id
        self.text = params["text"]
        self.win_money = params["win_money"]
        self.loose_money = params["loose_money"]
        self.move_to = params["move_to"]
        self.pay_per_house = params["pay_per_house"]
        self.pay_per_hotel = params["pay_per_hotel"]
        self.win_through_start = params["win_through_start"]
        self.move = params["move"]
