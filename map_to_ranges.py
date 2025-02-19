# Contains the direct file paths from the current working directory to the hand ranges
import pathlib
import os

ACTION_NAMES = ["RFI", "RAISE", "3BET", "4BET", "4BET_ALLIN", "5BET_ALLIN"]

POSITIONS = ["LJ", "HJ", "CO", "BTN", "SB", "BB"]

current_dir = os.path.dirname(__file__)
range_dir = "CASH_6MAX_100"
BB_RANGES = pathlib.Path(
    f"{current_dir}/{range_dir}/{POSITIONS[0]}/{ACTION_NAMES[0]}/{POSITIONS[0]}_{ACTION_NAMES[0]}.html"
)


# f = open(BB_RANGES, "r")
# print(f.read())

"""
Folders are structured as follows
Position 
    Action
        Ranges
Range files use the following naming structure
POSITION_VS_VILLAN_ACTION.html
where Villan is the other player involved in the hand. 
Action should be the same as the action folder name and 
position should be the same as the position folder name
"""
files = []
for position in POSITIONS:
    for action in ACTION_NAMES:
        temp_path = ""
        if action == "RFI":
            temp_path = f"{current_dir}/{range_dir}/{position}/{action}/{position}_{action}.html"
            folder_exists = pathlib.Path(temp_path).exists()
            if folder_exists:
                temp_obj = {
                    "position": position,
                    "action": action,
                    "villan": "NA",
                    "file": temp_path,
                }
                files.append(temp_obj)
        else:
            for p in POSITIONS:
                temp_path = f"{current_dir}/{range_dir}/{position}/{action}/{position}_VS_{p}_{action}.html"
                folder_exists = pathlib.Path(temp_path).exists()
                if folder_exists:
                    temp_obj = {
                        "position": position,
                        "action": action,
                        "villan": p,
                        "file": temp_path,
                    }
                    files.append(temp_obj)
for x in files:
    print(x)
