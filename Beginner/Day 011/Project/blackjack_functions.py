def check_winner(p_score, c_score):
    if p_score == 0:
        print("You win with Blackjack! 🤩")
    elif c_score == 0:
        print("You lose. Opponent has Blackjack! 😱")
    elif p_score > 21:
        print("You went over. You lose. 😭")
    elif c_score > 21:
        print("Opponent went over! You win! 😁")
    elif p_score > c_score:
        print("You win! 😁")
    elif c_score > p_score:
        print("You lose. 😭")
    elif p_score == c_score:
        print("It's a draw! 🥱")

def print_score(p_cards, p_score, c_cards):
    if p_score == 0:
        p_score = "BlackJack"
    if 1 in p_cards:
        p_cards[p_cards.index(1)] = 11
    print(f"Your cards: {p_cards}, current score: {p_score}")
    print(f"Computer's first card: {c_cards}")

def print_final_score(p_cards, p_score, c_cards, c_score):
    if p_score == 0:
        p_score = "BlackJack"
    if c_score == 0:
        c_score = "BlackJack"
    if 1 in p_cards:
        p_cards[p_cards.index(1)] = 11
    if 1 in c_cards:
        c_cards[c_cards.index(1)] = 11
    print(f"Your final cards are: {p_cards}. Final score: {p_score}")
    print(f"Computers final cards are: {c_cards}. Final score: {c_score}")