import random, os, art, blackjack_functions

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

game = True

while game:
    choice_game = input("Would you like to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower()
    if choice_game == "y":
        clear_terminal()
        print(art.logo)

        player_cards = []
        comp_cards = []

        player_cards += random.sample(cards, 2)
        player_score = sum(player_cards)

        comp_cards += random.sample(cards, 2)
        comp_score = sum(comp_cards)

        drawing = True
        blackjack = 0
        while drawing:
            if player_score == 21:
                player_score = blackjack
                blackjack_functions.print_score(player_cards, player_score, comp_cards[0])
                drawing = False
                break

            while player_score < 21:
                blackjack_functions.print_score(player_cards, player_score, comp_cards[0])
                draw_again = input("Type 'y' to get another card, type 'n' to pass: ")

                if draw_again == "y":
                    player_cards.append(random.choice(cards))
                    player_score = sum(player_cards)

                    if 11 in player_cards and player_score > 21:
                        player_cards[player_cards.index(11)] = 1
                        player_score = sum(player_cards)

                elif draw_again == "n":
                    drawing = False
                    break

            drawing = False

        if player_score == blackjack or player_score > 21:
            blackjack_functions.print_final_score(player_cards, player_score, comp_cards, comp_score)
            blackjack_functions.check_winner(player_score,comp_score)

        else:
            comp_bj = 0
            comp_score = sum(comp_cards)
            comp_drawing = True

            while comp_drawing:

                if comp_score == 21:
                    comp_score = comp_bj
                    comp_drawing = False

                else:
                    while comp_score < 17:
                        comp_cards.append(random.choice(cards))
                        comp_score = sum(comp_cards)

                        if 11 in comp_cards and comp_score > 21:
                            comp_cards[comp_cards.index(11)] = 1
                            comp_score = sum(comp_cards)

                comp_drawing = False
            blackjack_functions.print_final_score(player_cards, player_score, comp_cards, comp_score)
            blackjack_functions.check_winner(player_score, comp_score)

    else:
        clear_terminal()
        game = False