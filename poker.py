from poker_constants import SUITS, CARDS, POSITIONS, ACTION_NAMES, POSITION_SCENARIOS 
import numpy as np
from HandRange import HandRange
import random

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
def format_file_name(hand_info, is_rfi) -> str:
    print("format_file_name parameters")
    print("hand_info", hand_info)
    print("is_rfi ", is_rfi)
    if is_rfi:
        return f"{hand_info[0].capitalize()}{hand_info[1].capitalize()}"
    return (
        f"{hand_info[0].capitalize()}{hand_info[1].capitalize()}{hand_info[2].lower()}"
    )

def possible_villain_pos(hero_pos: str, villain_pos: str) -> list:
    print(POSITION_SCENARIOS[hero_pos][villain_pos])
    return POSITION_SCENARIOS[hero_pos][villain_pos]

def main():
    print("Hello poker")
    continue_running = True
    print("************ RANGE REAPER oooo scary ***************")
    while continue_running:
        print("What is your position:\n1.LJ 2.HJ 3.CO \n4.BTN 5.SB 6.BB")
        user_pos = int(input("-->: "))
        if user_pos == 10:
            return
        print("What is villan position:\n0.NA 1.LJ 2.HJ 3.CO \n4.BTN 5.SB 6.BB")
        villain_pos = int(input("-->: "))

        user_pos = POSITIONS[user_pos-1]
        if villain_pos == 0 or villain_pos == user_pos:
            villain_pos = "RFI"
            action = "RFI"
        else:
            villain_pos = POSITIONS[villain_pos-1]
            if villain_pos == 10:
                return

        # working on optimzing the input flow so the action options that are shown are based on the hero and villain so you 
        # can't pick an action that is not possible for the current positions
        formatted_villain_pos = villain_pos
        possible_actions = possible_villain_pos(user_pos, formatted_villain_pos)
        print(possible_actions, "possible actions")
        print("What is the action?\n1.RFI 2.RAISE 3.3BET 4.4BET\n5.4BET_ALLIN\n6.5BET 7.5BET_ALLIN")
        action = int(input("-->: "))
        if action == 10:  
            return
        if villain_pos == 0 or action == 1:
            villain_pos = "NA"
            action = "RFI"
        print(user_pos, villain_pos, action)
        print("Enter your hand")
        user_hand = input("-->: ")
        user_hand_list = []
        for letter in user_hand:
            user_hand_list.append(letter)
        
        user_hand_list = format_file_name(user_hand_list, len(user_hand_list) == 2)
        print(user_hand_list)
        formatted_villain_pos = villain_pos
        if villain_pos == "NA":
            formatted_villain_pos = "RFI"
        villain_pos_scenarios = possible_villain_pos(user_pos, formatted_villain_pos, action)
        print(villain_pos_scenarios, "villain pos")
        print(f"{user_pos}-{villain_pos}-{action}-{user_hand}")
        file_path = ""
        if action == "RFI" or villain_pos == "NA":
            file_path = f"{user_pos}-{action}.json"
        else:
            file_path = f"{user_pos}-{villain_pos}-{action}.json"
        print(f"file path: {file_path}")

        hand_range = HandRange(user_pos)
        range_json = hand_range.load_ranges_from_json(
            hand_range.get_range_file_path(user_pos, villain_pos, action)
        )
        for temp in range_json[user_hand_list]:
            print(temp)
            print(range_json[user_hand_list][temp])

if __name__ == "__main__":
    main()
