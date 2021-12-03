import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A']
suits = ['♥', '♠', '♣', '♦']
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')
player1 = []
player2 = []


num_cards = int(input("Please enter a number of cards to be dealt: "))
print("-----------------------------------------------")
while len(player1) <num_cards:
    card = random.choice(deck)
    deck.remove(card)
    player1.append(card)
    card2 = random.choice(deck)
    deck.remove(card2)
    player2.append(card2)



def cal_sum(hand):
    sum1 = 0
    for i in hand:
        ch = i[0]
        if ch =='A':
            sum1 +=14
        elif ch == 'K':
            sum1 +=13
        elif ch =='Q':
            sum1 +=12
        elif ch =='J':
            sum1 +=11
        elif (ch =='1'):
            sum1 += 10
        else:
            sum1 +=int(ch)
    return(sum1)

def WINNER_AND_LOSER(player1,player2):
    sum1 = cal_sum(player1)
    sum2 = cal_sum(player2)
    if(sum1 > sum2):
        print("Player1 IS WINNER!!!")
    elif (sum1 == sum2):
        print("DRAW")
    else:
        print("player2 IS WINNER!!!")

print("-----------------------------------------------")
print("Player1 has the folowing cards :")
print(player1)
print("-----------------------------------------------")
print("total value of cards payer1 have :",cal_sum(player1))
print("-----------------------------------------------")
print("Player2 has the folowing cards :")
print(player2)
print("-----------------------------------------------")
print("total value of cards payer2 have :",cal_sum(player2))
print("-----------------------------------------------")
WINNER_AND_LOSER(player1, player2)
print("-----------------------------------------------")