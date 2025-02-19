from scrape_range_charts import ScrapeRangeCharts
from bs4 import ResultSet
import json

scraper = ScrapeRangeCharts("hello")

file_info = scraper.get_all_file_paths()

bb_vs_sb_4bet_allin_info: dict = file_info[-1]

print(bb_vs_sb_4bet_allin_info)

soup_obj: ResultSet = scraper.parse_file_for_chart_cols(
    bb_vs_sb_4bet_allin_info["file_path"]
)
print(type(soup_obj))
# for info in file_info:
#     print(info)

all_hands = {}

for info in file_info:
    range_cols = scraper.parse_file_for_chart_cols(info["file_path"])
    hand_info: dict = scraper.get_range_values(range_cols)
    if info["villan"] == "NA":
        json_file_name = f"{info['position']}-{info['action']}"
    else:
        json_file_name = f"{info['position']}-{info['villan']}-{info['action']}"
    # with open(f'{json_file_name}.json', "w") as fp:
    #     json.dump(hand_info, fp)

# with open("result.json", "w") as fp:
#     json.dump(all_hands, fp)
