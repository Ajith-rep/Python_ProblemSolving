#Simple BlackJack Game
import random

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_total(hand):
    total = 0
    aces = hand.count('A')
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card != 'A':
            total += int(card)
    for _ in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total

def blackjack():
    print("\n--- Simple Blackjack ---")
    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]

    print("Your cards:", player)
    print("Dealer shows:", dealer[0])

    # Player turn
    while calculate_total(player) < 21:
        move = input("Hit or Stand? (h/s): ").lower()
        if move == 'h':
            player.append(deal_card())
            print("Your cards:", player)
        else:
            break

    player_total = calculate_total(player)
    dealer_total = calculate_total(dealer)

    print("\nYour total:", player_total)
    print("Dealer's cards:", dealer, "| total =", dealer_total)

    # Dealer draws if less than 17
    while dealer_total < 17:
        dealer.append(deal_card())
        dealer_total = calculate_total(dealer)
        print("Dealer draws:", dealer)

    # Results
    if player_total > 21:
        print("You busted! Dealer wins.")
    elif dealer_total > 21:
        print("Dealer busted! You win.")
    elif player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
blackjack()
