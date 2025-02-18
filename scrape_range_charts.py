from bs4 import BeautifulSoup, ResultSet#,  Tag
import re
import os
import pathlib
import random
from poker_constants import ACTION_NAMES, POSITIONS
# fold_regex = re.compile("^Fold=")
# call_regex = re.compile("^Call=")
# raise_regex = re.compile("^Raise \d*")
# three_bet_regex = re.compile("^3-bet \d*")
# four_bet_raise_regex = re.compile("4-bet \d*")
# four_bet_all_in_regex = re.compile("4-bet All-in=*")
# five_bet_raise_regex = re.compile("5-bet \d*")
# five_bet_all_in_regex = re.compile("5-bet All-in=*")
# comments_regex = re.compile("<!--|-->")
# source = "CASH_6MAX_100_LJ_RFI.html"
# script_dir = os.path.dirname(os.path.abspath

# html_file = open(file_path, "r", encoding="utf-8")
# soup = BeautifulSoup(comments_regex.sub("", html_file.read()), "lxml")
# chart_columns: ResultSet = soup.find("div", {"class": "chart_full_data"}).find_all("div", {"class": "row"})
# print(len(chart_columns))
# print(type(chart_columns))
# col_one: Tag = chart_columns[0]
# print(col_one.attrs)
# hand_combo = col_one.attrs['data-handid']
# print(hand_combo)

class ScrapeRangeCharts:

    def __init__(self, name: str):
        self.name = name
        self.fold_regex = re.compile("^Fold=")
        self.call_regex = re.compile("^Call=")
        self.raise_regex = re.compile("^Raise \d*")
        self.three_bet_regex = re.compile("^3-bet \d*")
        self.four_bet_raise_regex = re.compile("4-bet \d*")
        self.four_bet_all_in_regex = re.compile("4-bet All-in=*")
        self.five_bet_raise_regex = re.compile("5-bet \d*")
        self.five_bet_all_in_regex = re.compile("5-bet All-in=*")
        self.comments_regex = re.compile("<!--|-->")
        self.file_info = []

    def get_all_file_paths(self, range_dir = "CASH_6MAX_100") -> list: 
        current_dir = os.path.dirname(__file__)
        file_info = []
        for hero in POSITIONS:
            for action in ACTION_NAMES:
                temp_path = ""
                if action == "RFI":
                    temp_path = f'{current_dir}/{range_dir}/{hero}/{action}/{hero}_{action}.html'
                    folder_exists = pathlib.Path(temp_path).exists()
                    if folder_exists:
                        temp_obj = {
                            "position": hero,
                            "action": action,
                            "villan": "NA",
                            "file_path": temp_path
                        }
                    file_info.append(temp_obj)
                else:
                    for villan in POSITIONS:
                        temp_path = f'{current_dir}/{range_dir}/{hero}/{action}/{hero}_VS_{villan}_{action}.html'
                        folder_exists = pathlib.Path(temp_path).exists()
                        if folder_exists:
                            temp_obj = {
                                "position": hero,
                                "action": action,
                                "villan": villan,
                                "file_path": temp_path
                            }
                            file_info.append(temp_obj)
        self.file_info = file_info
        return file_info

    def parse_file_for_chart_cols(self, file_path: str) -> ResultSet:
        html_file = open(file_path, "r", encoding="utf-8")
        soup = BeautifulSoup(self.comments_regex.sub("", html_file.read()), "lxml")
        chart_cols: ResultSet = soup.find("div", {"class": "chart_full_data"}).find_all("div", {"class": "row"})
        return chart_cols

    def get_range_values(self, range_cols: ResultSet):
        hands = {}
        for row in range_cols:
            hand = row.attrs['data-handid']
            temp = {}
            can_call = row.find("div", {"class": self.call_regex})
            can_raise = row.find("div", {"class": self.raise_regex})
            can_fold = row.find("div", {"class": self.fold_regex})
            can_3bet = row.find("div", {"class": self.three_bet_regex})
            can_4bet = row.find("div", {"class": self.four_bet_raise_regex})
            can_4bet_allin = row.find("div", {"class": self.four_bet_all_in_regex})
            can_5bet = row.find("div", {"class": self.five_bet_raise_regex})
            can_5bet_allin = row.find("div", {"class": self.five_bet_all_in_regex})

            if can_raise is not None:
                raise_info = can_raise.attrs['class'][1].split("=")
                value = raise_info[0]
                freq = raise_info[1]
                temp['raise'] = {
                    "value": value,
                    "freq": freq
                }
            else: 
                temp['raise'] = {
                    "value": "0",
                    "freq": "0"
                }
            if can_fold is not None:
                fold_info = can_fold.attrs['class'][0].split("=")[1]
                temp['fold'] = {"freq": fold_info}
            else:
                temp['fold'] = {"freq": "0"}
            if can_call is not None:
                call_info = can_call.attrs['class'][0].split("=")[1]
                temp['call'] =  {
                    "freq": call_info
                }
            else: 
                temp['call'] = {
                    "freq": "0"
                }
            if can_3bet is not None:
                three_bet_info = can_3bet.attrs['class'][1].split("=")
                value = three_bet_info[0]
                freq = three_bet_info[1]
                temp['3bet'] = {
                    "freq":  freq,
                    "value": value
                }
            else: 
                temp['3bet'] = {
                    "freq": "0"
                }
            if can_4bet is not None:
                four_bet_info = can_4bet.attrs['class'][1].split("=")
                value = four_bet_info[0]
                freq = four_bet_info[1]
                temp['4bet'] = {
                    "freq":  freq,
                    "value": value
                }
            else: 
                temp['4bet'] = {
                    "freq": "0"
                }
            if can_4bet_allin is not None:
                four_bet_allin_info = can_4bet_allin.attrs['class'][1].split("=")[1]
                temp['4bet_allin'] = {
                    "freq": four_bet_allin_info
                }
            else:
                temp['4bet_allin'] = {
                    "freq": "0"
                }
            if can_5bet is not None:
                five_bet_info = can_5bet.attrs['class'][1].split("=")
                value = five_bet_info[0]
                freq = five_bet_info[1] 
                temp['5bet'] = {
                    "freq": freq,
                    "value": value
                }
            else:
                temp['5bet'] = {
                    "freq": "0"
                }
            if can_5bet_allin is not None:
                five_bet_allin_info = can_5bet_allin.attrs['class'][1].split("=")[1]
                temp['5bet_allin'] = {
                    "freq": five_bet_allin_info
                }
            else:
                temp['5bet_allin'] = {
                    "freq": "0"
                }

            
            hands[hand] = temp
        return hands


'''
For each hand we want to look for all of the possible actions and record 
what the recommended sizing is, as well as the % of time that it should be done. 

i.e. Raise 2.5bb=0.6739 is Raise, 2.5bb, 0.6739 
'''
# hands = {}
# for row in chart_columns:
#     hand = row.attrs['data-handid']
#     temp = {}
#     can_call = row.find("div", {"class": call_regex})
#     can_raise = row.find("div", {"class": raise_regex})
#     can_fold = row.find("div", {"class": fold_regex})
#     can_3bet = row.find("div", {"class": three_bet_regex})
#     can_4bet = row.find("div", {"class": four_bet_raise_regex})
#     can_4bet_allin = row.find("div", {"class": four_bet_all_in_regex})
#     can_5bet = row.find("div", {"class": five_bet_raise_regex})
#     can_5bet_allin = row.find("div", {"class": five_bet_all_in_regex})

#     if can_raise is not None:
#         raise_info = can_raise.attrs['class'][1].split("=")
#         value = raise_info[0]
#         freq = raise_info[1]
#         temp['raise'] = {
#             "value": value,
#             "freq": freq
#         }
#     else: 
#         temp['raise'] = {
#             "value": "0",
#             "freq": "0"
#         }
#     if can_fold is not None:
#         fold_info = can_fold.attrs['class'][0].split("=")[1]
#         temp['fold'] = {"freq": fold_info}
#     else:
#         temp['fold'] = {"freq": "0"}
#     if can_call is not None:
#         call_info = can_call.attrs['class'].split["="][1]
#         temp['call'] =  {
#             "freq": call_info
#         }
#     else: 
#         temp['call'] = {
#             "freq": "0"
#         }
#     if can_4bet is not None:
#         four_bet_info = can_4bet.attrs['class'].split("=")
#         value = four_bet_info[0][1]
#         freq = four_bet_info[1]
#         temp['4bet'] = {
#             "freq":  freq,
#             "value": value
#         }
#     else: 
#         temp['4bet'] = {
#             "freq": "0"
#         }
#     if can_4bet_allin is not None:
#         four_bet_allin_info = can_4bet_allin.attrs['class'].split("=")[1]
#         temp['4bet_allin'] = {
#             "freq": four_bet_allin_info
#         }
#     else:
#         temp['4bet_allin'] = {
#             "freq": "0"
#         }
#     if can_5bet is not None:
#         five_bet_info = can_5bet.attrs['class'].split("=")
#         value = five_bet_info[0].split(" ")[1]
#         freq = five_bet_info[1] 
#         temp['5bet'] = {
#             "freq": freq,
#             "value": value
#         }
#     else:
#         temp['5bet'] = {
#             "freq": "0"
#         }
#     if can_5bet_allin is not None:
#         four_bet_allin_info = can_5bet_allin.attrs['class'].split("=")[1]
#         temp['5bet_allin'] = {
#             "freq": four_bet_allin_info
#         }
#     else:
#         temp['5bet_allin'] = {
#             "freq": "0"
#         }

    
#     hands[hand] = temp
# print(hands)
# print(hands['54s'])
# print(random.randint(0, 1000)/1000)
# print(col_one.find("div", {"class": raise_regex}).attrs['class'])
# col_1 = BeautifulSoup(chart_columns[0], "html")
# print(col_1)
