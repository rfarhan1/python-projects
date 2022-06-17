import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(x):
    randomInt = random.randint(0, len(x) - 1)
    card_list = x[randomInt]
    return card_list


def calculated_score(card_list):  # if a list in constant, it can be used inside the function
    score = sum(card_list)
    if score == 21:
        return 0
    else:
        ace = False
        for i in range(0, len(card_list)):
            if card_list[i] == 11:
                ace = True
        while ace:
            for i in range(0, len(card_list)):
                if card_list[i] == 11:
                    card_list[i] = 1
                    score = 0
                    for card in card_list:
                        score += card
                    break
            return score
        return score


def compare(score1, score2):
    result = "Error"
    if score1 > 21:
        result = "lose"
    elif score2 > 21:
        result = "win"
    elif score1 == score2:
        result = "draw"
    elif score1 == 0:
        result = "win"
    elif score2 == 0:
        result = "lose"
    elif score2 > score1:
        result = "lose"
    elif score2 < score1:
        result = "win"
    return result


start = input("Do you want to play a game of Blackjack? 'Y' or 'N':  ").lower()

if start == 'y':
    print(art.logo)

    players_card = []
    computer_card = []
    for i in range(0, 2):
        players_card.append(deal_card(cards))
        computer_card.append(deal_card(cards))
    # deal: both gets two cards

    players_score = calculated_score(players_card)
    computer_score = calculated_score(computer_card)
    print(f"Your card: {players_card} Your score: {players_score}\nDealer's first card: {computer_card[0]}")

    game_over = False

    if players_score == 0:
        print(f"Your card: {players_card}  Your scored Blackjack\nDealer's first card: {computer_card[0]}\nYou win")
        game_over = True
    elif players_score > 21 or computer_score == 0:
        print(
            f"Your card: {players_card}  Your score: {players_score}\nDealer's first card: {computer_card[0]}  Blackjack for dealer\nYou lose.")
        game_over = True

    players_deal = True
    while not game_over and players_deal:
        to_continue = input("Type 'y' to take another card, otherwise type 'n': ").lower()
        if to_continue == 'n':
            players_deal = False
        elif to_continue == 'y':
            players_card.append(deal_card(cards))
            players_score = calculated_score(players_card)
            if players_score == 0:
                print(
                    f"Your card: {players_card}  Your scored Blackjack\nDealer's first card: {computer_card[0]}\nYou win")
                game_over = True
            elif players_score > 21:
                print(
                    f"Your card: {players_card}  Your score: {players_score}\nDealer's first card: {computer_card[0]}\nYou lose.")
                game_over = True
            else:
                print(f"Your card: {players_card} Your score: {players_score}\nDealer's first card: {computer_card[0]}")

    dealers_play = False
    if computer_score < 17 and game_over == False:
        dealers_play = True

    while dealers_play and not game_over:
        computer_card.append(deal_card(cards))
        computer_score = calculated_score(computer_card)
        if computer_score == 0:
            print(
                f"Your card: {players_card}  Your score: {players_score}\nDealer's card: {computer_card}  Dealer's score: {computer_score}\nYou lose.")
            game_over = True

        elif computer_score > 21:
            print(
                f"Your card: {players_card}  Your score: {players_score}\nDealer's card: {computer_card}  Dealer's score: {computer_score}\nYou win")
            game_over = True
            break
        elif computer_score >= 17:
            dealers_play = False

        final_result = compare(players_score, computer_score)

    if game_over == False:
        print(
            f"Your card: {players_card}  Your score: {players_score}\nDealer card: {computer_card}  Dealer's score: {computer_score}\nYou {final_result}")


else:
    print("You've lost")

