CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

SUITS = ["H", "D", "C", "S"]

HAND_TYPES = ["s", "o"]

SUIT_VALUES = {"H": "Hearts", "D": "Diamonds", "C": "Clubs", "S": "Spades"}

CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 0,
}

PLAYER_ACTIONS = [
    "FOLD",
    "CALL",
    "LIMP",
    "3BET",
    "4BET",
    "4BET ALL IN",
    "5BET",
    "5BET ALL IN",
    "JAM / ALL IN",
]

SIX_MAX_POSITIONS = ["SB", "BB", "LJ", "HJ", "CO", "BTN"]

SIX_MAX_PREFLOP_POSITIONS = ["LJ", "HJ", "CO", "BTN", "SB", "BB"]

HAND_RANGE_CHART_CLASS_NAMES = [
    "Raise",
    "Fold"
]