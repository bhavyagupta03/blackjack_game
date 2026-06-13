# project blackjack

import random

K = 10
J = 10
Q = 10

cards = [2, 3, 4, 5, 6, 7, 8, 9, K, Q, J, 11]

blackjack_logo = ''' /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
| $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/
| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/       | $$| $$  \ $$| $$  \__/| $$ /$$/
| $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/        | $$| $$$$$$$$| $$      | $$$$$/
| $$__  $$| $$      | $$__  $$| $$      | $$  $$   /$$  | $$| $$__  $$| $$      | $$  $$
| $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$ | $$  | $$| $$  | $$| $$    $$| $$\  $$
| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$
|_______/ |________/|__/  |__/ \______/ |__/  \__/ \______/ |__/  |__/ \______/ |__/  \__/'''


# deals cards
def deal_card():
    return random.choice(cards)


def calculate_score(cards):
    # Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Handle multiple aces correctly
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "DRAW"
    elif dealer_score == 0:
        return "LOST, DEALER HAS BLACKJACK"
    elif user_score == 0:
        return "WON, YOU HAVE A BLACKJACK"
    elif user_score > 21:
        return "YOU LOST"
    elif dealer_score > 21:
        return "YOU WIN"
    elif user_score > dealer_score:
        return "YOU WIN"
    else:
        return "YOU LOSE"


def play_game():
    print(blackjack_logo)

    dealer_cards = []
    user_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to hit and 'n' to pass: ").lower()

            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    dealer_score = calculate_score(dealer_cards)

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print("\n-------------------------")
    print(f"YOUR FINAL HAND: {user_cards}, FINAL SCORE: {user_score}")
    print(f"DEALER FINAL HAND: {dealer_cards}, DEALER SCORE: {dealer_score}")
    print(compare(user_score, dealer_score))
    print("-------------------------")


while input("Do you want to play a game of blackjack? ('y'/'n'): ").lower() == "y":
    play_game()