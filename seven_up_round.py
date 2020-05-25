import random
import seven_up_deck

# ********************************************************
# CLASS: Round
# ********************************************************
class Round():

    # ********************************************************
    # METHOD: __init__
    # ********************************************************
    def __init__(self, round_num, num_cards, users, dealer, trump):
        print 'ROUND[' + str(round_num) + ']: Num Cards = ' + str(num_cards) + ', Dealer = ' + users[dealer].name
        self.num_cards = num_cards
        self.users = users
        self.dealer = dealer
        self.deck = seven_up_deck.Deck()
        self.deck.shuffle()
        self.deal()
#        self.deck.print_deck()
        self.trump = trump
        self.trump_card = self.deck.pull_card()
        if self.trump:
            print 'TRUMP: ' + seven_up_deck.card_to_string(self.trump_card)
        else:
            print 'NO TRUMP'

    # ********************************************************
    # METHOD: deal
    # ********************************************************
    def deal(self):
        for index in range(0,self.num_cards):
            for id in self.users:
                card = self.deck.pull_card()
                self.users[id].add_card(card)

