import random

cards = {
    "2": 4,
    "3": 4,
    "4": 4,
    "5": 4,
    "6": 4,
    "7": 4,
    "8": 4,
    "9": 4,
    "10": 4,
    "J": 4,
    "Q": 4,
    "K": 4,
    "A": 4
}

cards_value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11  # Ace can be 1 or 11, initially set to 11
}

def deposit():
    while True:
        amount = input("Enter amount to deposit: $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Enter an amount greater than zero.")
        else:
            print("Enter a valid number.")

def get_bet(balance):
    while True:
        amount = input(f"Enter the amount to bet (Available balance: ${balance}): $ ")
        if amount.isdigit():
            amount = int(amount)
            if 0 < amount <= balance:
                return amount
            else:
                print("Enter a value greater than 0 and less than or equal to your available balance.")
        else:
            print("Enter a valid number.")

def distribute_cards(deck, num_cards):
    return deck[:num_cards], deck[num_cards:]

def calculate_hand_value(hand):
    total_value = sum(cards_value[card] for card in hand)
    num_aces = hand.count("A")
    while total_value > 21 and num_aces:
        total_value -= 10  # Change Ace value from 11 to 1
        num_aces -= 1
    return total_value

def print_cards(hand, player, hide_first_card=False):
    if player:
        print("PLAYER:")
    else:
        print("DEALER:")
    if hide_first_card:
        print("X")
        print("\n".join(hand[1:]))
    else:
        print("\n".join(hand))

def main():
    balance = deposit()

    while True:
        print(f"Available balance: ${balance}")
        bet = get_bet(balance)
        balance -= bet

        deck = [card for card in cards for _ in range(cards[card])]
        random.shuffle(deck)

        player_hand, deck = distribute_cards(deck, 2)
        dealer_hand, deck = distribute_cards(deck, 2)

        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        print_cards(player_hand, player=True)
        print_cards(dealer_hand, player=False, hide_first_card=True)

        if player_value == 21:
            print("Player has Blackjack!")
            balance += bet * 2.5  # Blackjack pays 3:2
        else:
            while player_value < 21:
                action = input("Do you want to hit or stand? ").strip().lower()
                if action == "hit":
                    new_card, deck = distribute_cards(deck, 1)
                    player_hand.extend(new_card)
                    player_value = calculate_hand_value(player_hand)
                    print_cards(player_hand, player=True)
                    if player_value > 21:
                        print("Player busts!")
                        break
                elif action == "stand":
                    break
                else:
                    print("Invalid action. Please enter 'hit' or 'stand'.")

            while dealer_value < 17:
                new_card, deck = distribute_cards(deck, 1)
                dealer_hand.extend(new_card)
                dealer_value = calculate_hand_value(dealer_hand)

            print("Final hands:")
            print_cards(player_hand, player=True)
            print_cards(dealer_hand, player=False)

            if player_value > 21:
                print("Player busts! Dealer wins!")
            elif dealer_value > 21:
                print("Dealer busts! Player wins!")
                balance += bet * 2
            elif player_value > dealer_value:
                print("Player wins!")
                balance += bet * 2
            elif player_value < dealer_value:
                print("Dealer wins!")
            else:
                print("It's a tie! Player gets back their bet.")
                balance += bet

        print(f"Updated balance: ${balance}")
        if balance <= 0:
            print("Insufficient balance to continue playing.")
            break

        play_again = input("Do you want to play again? (yes/no) ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
