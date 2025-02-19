from poker_constants import SUITS, CARDS, POSITIONS, ACTION_NAMES
import numpy as np
from HandRange import HandRange

card_ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
rank_index = {rank: i for i, rank in enumerate(card_ranks)}  # Fast lookup

def generate_deck():
    deck = []
    for suit in SUITS:
        for card in CARDS:
            deck.append(f"{card}{suit}")
    print(deck)
    return deck


"""
Generates all possible hand types from AA to 72o
"""


def generate_possible_hand_types():
    # want to generate all possible hands, off suit and suited
    for card in CARDS:
        print(card)
    return


def generate_poker_hands():
    hand_combinations = []

    for i, rank1 in enumerate(card_ranks):
        for rank2 in card_ranks[i:]:  # Avoid duplicates by only iterating forward
            if rank1 == rank2:
                hand_combinations.append(rank1 + rank2)  # Pairs
            else:
                hand_combinations.append(rank1 + rank2 + "s")  # Suited
                hand_combinations.append(rank1 + rank2 + "o")  # Offsuit

    return hand_combinations

def generate_poker_hand_matrix():
    size = len(card_ranks)
    matrix = np.empty((size, size), dtype=object)  # 13x13 array of strings

    for i, rank1 in enumerate(card_ranks):
        for j, rank2 in enumerate(card_ranks):
            if i == j:
                matrix[i, j] = rank1 + rank2  # Pair (AA, KK, QQ, etc.)
            elif i < j:
                matrix[i, j] = rank1 + rank2 + "s"  # Suited hands (AKs, AQs, etc.)
            else:
                matrix[i, j] = rank2 + rank1 + "o"  # Offsuit hands (AKo, AQo, etc.)

    return matrix

def get_hands_in_range(range_str: str, matrix):
    is_expanded_range: bool = range_str.endswith("+")
    is_suited: bool = "s" in range_str
    row_or_col: str = "row" if is_suited else "column"
    print(is_expanded_range, " is expanded range")
    print(is_suited, " is suited")
    print(row_or_col, " row or col")

    return

# output of this loop is true until the user wishes to exit the program
# def user_input_collector() -> bool:

def get_hero_position(user_input: int) -> str:
    return ""

def main():
    print("Hello poker")
    print('************ RANGE REAPER oooo scary ***************')
    print("What is your position:\n1.LJ 2.HJ 3.CO \n4.BTN 5.SB 6.BB")
    user_pos = int(input("-->: "))
    print("What is villan position:\n0.NA 1.LJ 2.HJ 3.CO \n4.BTN 5.SB 6.BB")
    villain_pos = int(input('-->: '))
    print("What is the action?\n1.RFI 2.RAISE 3.3BET 4.4BET\n5.4BET_ALLIN\n6.5BET 7.5BET_ALLIN")
    action = int(input("-->: "))
    if villain_pos == 0 or action == 1:
        villain_pos = "NA"
        action = "RFI"
    else:
        villain_pos = POSITIONS[villain_pos - 1]
        action = ACTION_NAMES[action-1]
    user_pos = POSITIONS[user_pos-1]
    print(user_pos, villain_pos, action)
    print("Enter your hand")
    user_hand = input("-->: ")
    print(f'{user_pos}-{villain_pos}-{action}-{user_hand}')
    file_path = ""
    if action == "RFI" or villain_pos == "NA":
        file_path = f'{user_pos}-{action}.json'
    else:
        file_path = f'{user_pos}-{villain_pos}-{action}.json'
    print(f'file path: {file_path}')


    hand_range = HandRange(user_pos)
    print(hand_range)
    # generate_possible_hand_types()

    # poker_hands = generate_poker_hands()
    # temp = []
    # for hand in poker_hands:
    #     print(hand)
    # poker_matrix = generate_poker_hand_matrix()
    # for x in poker_matrix:
    #     print(x)

    # selected_hands = parse_poker_range(poker_range, poker_matrix)
    # print("selected hands")
    # print(selected_hands)

if __name__ == "__main__":
    main()
