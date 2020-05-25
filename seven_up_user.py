import seven_up_deck

# ********************************************************
# CLASS: User
# ********************************************************
class User():

    # ********************************************************
    # METHOD: initialize
    # ********************************************************
    def initialize(self, name):
        self.name = name
        self.cards = []

    # ********************************************************
    # METHOD: add_card
    # ********************************************************
    def add_card(self, card):
        self.cards.append(card)

    # ********************************************************
    # METHOD: print_user
    # ********************************************************
    def print_user(self):
        print('NAME: ' + str(self.name)) + ' -' ,
    	for card in sorted(self.cards, reverse=True):
            print seven_up_deck.card_to_string(card) + ',' ,
        print ''
        
