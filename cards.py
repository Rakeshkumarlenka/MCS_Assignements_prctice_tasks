from random import shuffle

class Cards:
    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suites = ['♥', '♠', '♣', '♦']
        self.deck = [j + i for j in ranks for i in suites]
        self.deal = []

    def shuffle(self):
        shuffle(self.deck)

    def deal_out(self,num_cards, num_players):
        deal = [[x for x in range(num_cards)] for y in range(num_players)]
        for i in range(num_cards):
            for k in range(num_players):
                deal[k][i]=self.deck.pop()
        self.deal = deal


#declare number of players and cards to be dealt
num_players = int(input("Please enter a number of players: "))
num_cards = int(input("Please enter a number of cards to be dealt: "))


#create new game with new deck
first_game = Cards()
print('\nDeck:\n')
print(first_game.deck)

#shuffle cards
first_game.shuffle()
print('\nShuffled Deck:\n')
print(first_game.deck)

#deal cards
first_game.deal_out(num_cards, num_players)

#Print the dealt cards
print('\nDealt cards:\n')
print(first_game.deal)

