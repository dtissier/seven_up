
import random

card_suites = {}
card_suites[0] = 'Hearts'
card_suites[1] = 'Clubs'
card_suites[2] = 'Spades'
card_suites[3] = 'Diamonds'

card_values = {}
card_values[0] = '2'
card_values[1] = '3'
card_values[2] = '4'
card_values[3] = '5'
card_values[4] = '6'
card_values[5] = '7'
card_values[6] = '8'
card_values[7] = '9'
card_values[8] = '10'
card_values[9] = 'Jack'
card_values[10] = 'Queen'
card_values[11] = 'King'
card_values[12] = 'Ace'

# ********************************************************
# METHOD: card_to_string
# ********************************************************
def card_to_string(card):
    global card_suites
    global card_values

    card_suite = card / 13
    card_index = card % 13
    return card_values[card_index] + ' of ' + card_suites[card_suite]

# ********************************************************
# CLASS: Deck
# ********************************************************
class Deck():

    # ********************************************************
    # METHOD: initialize
    # ********************************************************
    def initialize(self):
        self.cards = []

    # ********************************************************
    # METHOD: shuffle
    # ********************************************************
    def shuffle(self):
        ordered_cards = []
        for value in range(0, 52):
            ordered_cards.append(value)

        self.cards = []
        while len(ordered_cards) > 0:
        	index = random.randrange(0, len(ordered_cards))
        	value = ordered_cards[index]
        	self.cards.append(value)
        	ordered_cards.remove(value)
        # print str(self.cards)

    # ********************************************************
    # METHOD: pull_card
    # ********************************************************
    def pull_card(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card

    # ********************************************************
    # METHOD: print_deck
    # ********************************************************
    def print_deck(self):
        value = 10
        for value in self.cards:
            print card_to_string(value) + ',' ,

        
