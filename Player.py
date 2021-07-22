# This class controls the Player behavior
class Player:
    def __init__(self, number):
        self.number = number
        self.cards = {'c': [], 'd': [], 't': [], 'p': []}

    def set_new_card(self, card, type):
        if card in self.cards[type]:
            return False
        self.cards[type].append(card)
        return True

    def get_cards_value(self):
        total = 0
        special_cards = []
        for type in self.cards:
            for card in type:
                if isinstance(card, int):
                    total += card
                else:
                    special_cards.append(card)
        while len(special_cards) > 0:
            card = special_cards[0]
            if card == 'k':
                total += 12
            elif card == 'q':
                total += 11
            elif card == 'j':
                total += 10
            elif card == 'a':
                if total + 11 > 21 or len(special_cards) > 1:
                    total += 1
                total += 11
            special_cards.pop(0)