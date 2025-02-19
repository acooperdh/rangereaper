from scrape_range_charts import ScrapeRangeCharts
import json
import os

temp = ScrapeRangeCharts('test')

file_path = '/home/drew/Projects/rangereaper/CASH_6MAX_100/BB/RAISE/BB_VS_SB_RAISE.html'

charts_cols = temp.parse_file_for_chart_cols(file_path)

range_values = temp.get_range_values(charts_cols)

print(range_values)