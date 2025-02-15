from rangereaper.poker_constants import *
import random
import numpy as np

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
    row_or_col: bool = "row" if is_suited else "column"
    print(is_expanded_range, " is expanded range")
    print(is_suited, " is suited")
    print(row_or_col, " row or col")

    return



def parse_poker_range(range_str, matrix):
    selected_hands = set()

    for term in range_str.split(","):
        term = term.strip()

        if "+" in term:  # Handles "A5o+", "K8s+"
            base, plus = term[:-1], term[-1]
            rank1, rank2 = base[0], base[1]
            suit_type = "" if len(base) == 2 else base[2]  # "s", "o", or ""

            r1_idx = rank_index[rank1]
            r2_idx = rank_index[rank2]

            # Include the pair (AA, KK, etc.)
            selected_hands.add(matrix[r1_idx, r1_idx])

            # Expand the range from rank2 upwards
            for i in range(r2_idx, len(card_ranks)):
                expanded_hand = rank1 + card_ranks[i] + suit_type
                selected_hands.add(matrix[r1_idx, i])

        elif len(term) == 2:  # Handles pairs like "QQ"
            r_idx = rank_index[term[0]]
            selected_hands.add(matrix[r_idx, r_idx])

        else:  # Handles specific hands like "K8s"
            r1_idx, r2_idx = rank_index[term[0]], rank_index[term[1]]
            selected_hands.add(matrix[r1_idx, r2_idx])

    return selected_hands

def main():
    print("Hello poker")
    deck = generate_deck()
    poker_range = "A5o+, K8+, QTo+"
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
    lojack_rfi = "A3s+,A10o+,K8s+,KJo+,Q9s+,QJo+,J9s+,T9s+,66+"
    for x in lojack_rfi.split(","):
        print(x)
        get_hands_in_range(x, "")

if __name__ == "__main__":
    main()
