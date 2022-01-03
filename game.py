# Bringing in essential paramters
import os
import random 
import time 

# Welcome 
name = input("Welcome to the Casino, please enter your name: ")
welcome ="Nice to meet you, " + name + ". FYI, the dealer will present one of their cards, that card being the first card. Let's play some Backjack!"
print(welcome)
lets_start = input("Please enter 'Let's go!' to start the first round: ")
print(lets_start)


#setting up Card class for card values
class Card: 
    def __init__(self, suit, value, card_value): 
        self.suit = suit 
        self.value = value 
        self.card_value = card_value

def clear(): 
    os.system("clear") 

#Adding cards to player and Dealer 
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10]*4

def play(deck):
    player_cards = [] 
    dealer_cards = []

    while len(player_cards) < 2: 
        player_card = random.choice(deck)
        player_cards.append(player_card) 
    print("You currently have a sum of {a}.".format(a= player_cards[0] + player_cards[1]))
    
    while len(dealer_cards) <2: 
        dealer_card = random.choice(deck) 
        dealer_cards.append(dealer_card) 
    print("The Dealer is currently showing {a}.".format(a = dealer_cards[0]))
    dealer_sum = 0 

    for card in dealer_cards: 
        dealer_sum += card 
    return dealer_sum 

    if dealer_sum < 17: 
        dealer_hit = "The Dealer will hit after the first round." 
        print(dealer_hit)
    else: 
        dealer_stay = "The Dealer will stay after the first round."
        print(dealer_stay)

	
if __name__ == "__main__":
    play(deck)