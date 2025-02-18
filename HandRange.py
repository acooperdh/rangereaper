import json
import os
'''
A HandRange contains a players theoretical hand range & action frequency from a given position. 
HandRanges are expected to only be used for one position vs one action. For other situations generate a group of hand ranges
'''

class HandRange: 

    def __init__(self, hero_position: str):
        self.hero_position = hero_position
        self.range_dir = "ranges_json"

    
    def get_range_file_path(self, hero: str, villan: str, action: str) -> str:
        current_dir =  os.path.dirname(__file__)
        if villan == "NA" or action == "RFI":
            return f'{current_dir}/{self.ranges_dir}/{hero}-{action}.json'
        return f'{current_dir}/{self.ranges_dir}/{hero}-{villan}-{action}.json'


    def load_ranges_from_json(self, file_path: str) -> dict: 
        with open(file_path) as f:
            d = json.load(f)
            print(d)
            return d
        return 


