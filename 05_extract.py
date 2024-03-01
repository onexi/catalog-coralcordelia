# -----------------------------------------------
#  5. Data Extraction:
# 
#  Objective: Extract course titles from 
#  the data you cleaned.
# -----------------------------------------------

import json

def store_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('Data saved to: ', file)

with open("cleaned_bodies.json", "r", encoding='utf-8') as infile:
    bodies = json.load(infile)
    titles = [f"{i[0]} {i[1]}: {i[2]}" for i in bodies] # stores the titles of the courses into a file
    store_json(titles, 'titles.json')
