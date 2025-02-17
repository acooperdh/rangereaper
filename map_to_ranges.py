# Contains the direct file paths from the current working directory to the hand ranges
import pathlib
import os
def get_range_file_name(position):
    return

ACTION_NAMES = ["RFI", "RAISE", "3BET", "4BET", "4BET_ALLIN", "5BET_ALLIN"]

POSITIONS = ["LJ", "HJ", "CO", "BTN", "SB", "BB"]

current_dir = os.path.dirname(__file__)
range_dir = "CASH_6MAX_100"
BB_RANGES = pathlib.Path(f'{current_dir}/{range_dir}/{POSITIONS[0]}/{ACTION_NAMES[0]}/{POSITIONS[0]}_{ACTION_NAMES[0]}.html')
print(BB_RANGES)



# f = open(BB_RANGES, "r")
# print(f.read())

for position in POSITIONS:
    for action in ACTION_NAMES:
        print(f'{position}/{action}')
