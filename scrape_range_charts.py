from bs4 import BeautifulSoup, ResultSet, Tag
import re
import os
import random

fold_regex = re.compile("^Fold=")
call_regex = re.compile("^Call=")
raise_regex = re.compile("^Raise \d*")
three_bet_regex = re.compile("^3-bet \d*")
four_bet_raise_regex = re.compile("4-bet \d*")
four_bet_all_in_regex = re.compile("4-bet All-in=*")
five_bet_raise_regex = re.compile("5-bet \d*")
five_bet_all_in_regex = re.compile("5-bet All-in=*")
comments_regex = re.compile("<!--|-->")
source = "CASH_6MAX_100_LJ_RFI.html"
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, source)
html_file = open(file_path, "r", encoding="utf-8")
soup = BeautifulSoup(comments_regex.sub("", html_file.read()), "lxml")
chart_columns: ResultSet = soup.find("div", {"class": "chart_full_data"}).find_all("div", {"class": "row"})
print(len(chart_columns))
print(type(chart_columns))
col_one: Tag = chart_columns[0]
print(col_one.attrs)
hand_combo = col_one.attrs['data-handid']
print(hand_combo)
'''
For each hand we want to look for all of the possible actions and record 
what the recommended sizing is, as well as the % of time that it should be done. 

i.e. Raise 2.5bb=0.6739 is Raise, 2.5bb, 0.6739 
'''
hands = {}
for row in chart_columns:
    hand = row.attrs['data-handid']
    temp = {}
    can_call = row.find("div", {"class": call_regex})
    can_raise = row.find("div", {"class": raise_regex})
    can_fold = row.find("div", {"class": fold_regex})
    can_3bet = row.find("div", {"class": three_bet_regex})
    can_4bet = row.find("div", {"class": four_bet_raise_regex})
    can_4bet_allin = row.find("div", {"class": four_bet_all_in_regex})
    can_5bet = row.find("div", {"class": five_bet_raise_regex})
    can_5bet_allin = row.find("div", {"class": five_bet_all_in_regex})

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
        call_info = can_call.attrs['class'].split["="][1]
        temp['call'] =  {
            "freq": call_info
        }
    else: 
        temp['call'] = {
            "freq": "0"
        }
    if can_4bet is not None:
        four_bet_info = can_4bet.attrs['class'].split("=")
        value = four_bet_info[0].split(" ")[1]
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
        four_bet_allin_info = can_4bet_allin.attrs['class'].split("=")[1]
        temp['4bet_allin'] = {
            "freq": four_bet_allin_info
        }
    else:
        temp['4bet_allin'] = {
            "freq": "0"
        }
    if can_5bet is not None:
        five_bet_info = can_5bet.attrs['class'].split("=")
        value = five_bet_info[0].split(" ")[1]
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
        four_bet_allin_info = can_5bet_allin.attrs['class'].split("=")[1]
        temp['5bet_allin'] = {
            "freq": four_bet_allin_info
        }
    else:
        temp['5bet_allin'] = {
            "freq": "0"
        }

    
    hands[hand] = temp
print(hands)
print(hands['54s'])
print(random.randint(0, 1000)/1000)
# print(col_one.find("div", {"class": raise_regex}).attrs['class'])
# col_1 = BeautifulSoup(chart_columns[0], "html")
# print(col_1)
