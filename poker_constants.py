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

HAND_RANGE_CHART_CLASS_NAMES = ["Raise", "Fold"]

ACTION_NAMES = ["RFI", "RAISE", "3BET", "4BET", "4BET_ALLIN", "5BET", "5BET_ALLIN"]

POSITIONS = ["LJ", "HJ", "CO", "BTN", "SB", "BB"]

POSITION_SCENARIOS = {
    "LJ": {
        "RFI",
        "HJ-3BET",
        "HJ-5BET_ALLIN",
        "CO-3BET",
        "CO-5BET_ALLIN",
        "BTN-3BET",
        "BTN-5BET_ALLIN",
        "SB-3BET",
        "SB-5BET_ALLIN",
        "BB-3BET",
        "BB-5BET_ALLIN",
    },
    "HJ": {
        "RFI",
        "LJ-4BET",
        "LJ-4BET_ALLIN",
        "LJ-RAISE",
        "CO-3BET",
        "CO-5BET_ALLIN",
        "BTN-3BET",
        "BTN-5BET_ALLIN",
        "BB-3BET",
        "BB-5BET_ALLIN",
        "SB-3BET",
        "SB-5BET_ALLIN",
    },
    "CO": {
        "RFI",
        "LJ-RAISE",
        "LJ-4BET",
        "LJ-4BET_ALLIN",
        "HJ-RAISE",
        "HJ-4BET",
        "HJ-4BET_ALLIN",
        "BTN-3BET",
        "BTN-5BET_ALLIN",
        "SB-3BET",
        "SB-5BET_ALLIN",
        "BB-3BET",
        "BB-5BET_ALLIN",
    },
    "BTN": {
        "RFI",
        "LJ-RAISE",
        "LJ-4BET",
        "LJ-4BET_ALLIN",
        "HJ-RAISE",
        "HJ-4BET",
        "HJ-4BET_ALLIN",
        "CO-RAISE",
        "CO-4BET",
        "CO-4BET_ALLIN",
        "SB-3BET",
        "SB-5BET_ALLIN",
        "BB-3BET",
        "BB-5BET_ALLIN",
    },
    "SB": {
        "RFI",
        "LJ-RAISE",
        "LJ-4BET",
        "LJ-4BET_ALLIN",
        "HJ-RAISE",
        "HJ-4BET",
        "HJ-4BET_ALLIN",
        "CO-RAISE",
        "CO-4BET",
        "CO-4BET_ALLIN",
        "BTN-RAISE",
        "BTN-4BET",
        "BTN-4BET_ALLIN",
        "BB-3BET",
        "BB-5BET_ALLIN",
    },
    "BB": {
        "RAISE": {
            "LJ",
            "HJ",
            "CO",
            "BTN",
            "SB"
        },
        "4BET": {
            "LJ",
            "HJ",
            "CO",
            "BTN",
            "SB"
        },
        "4BET_ALLIN": {
            "LJ",
            "HJ",
            "CO",
            "BTN",
            "SB"
        },
    },
}
