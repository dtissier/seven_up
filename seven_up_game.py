import random
import seven_up_round

# ********************************************************
# CLASS: Game
# ********************************************************
class Game():

    # ********************************************************
    # METHOD: __init__
    # ********************************************************
    def __init__(self, num_cards, users):
        self.num_cards = num_cards
        self.cur_num_cards = num_cards
        self.users = users
        self.dealer = self.get_random_dealer()
        self.round_num = 0
        self.rounds = {}
        self.start()

    # ********************************************************
    # METHOD: get_random_dealer
    # ********************************************************
    def get_random_dealer(self):
        dealer = random.choice(list(self.users.keys()))
        return dealer

    # ********************************************************
    # METHOD: get_random_dealer
    # ********************************************************
    def start(self):
        self.rounds[self.round_num] = seven_up_round.Round(self.round_num, self.cur_num_cards, self.users, self.dealer, True)

