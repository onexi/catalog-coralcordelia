# -----------------------------------------------
#  6. Word Frequency Analysis:
# 
#  Objective: Perform a word frequency count 
#  on the course titles.
# 
#  Tools/Resources: You can use a “map reduce” 
#  style word counting approach.
# -----------------------------------------------

import json


def store_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('Data saved to: ', file)

with open("cleaned_bodies.json", "r", encoding='utf-8') as infile:
    bodies = json.load(infile)
    word_freqs = {}
    for i in bodies:
        for j in i[2].split():
            word_freqs[j.lower().replace(',', '')] = word_freqs.get(j.lower().replace(',', ''), 0) + 1
    sorted_word_freqs = {i: {"rank": ind+1, "frequency": word_freqs[i]} for ind, i in 
                         enumerate(sorted(word_freqs, key=lambda x: word_freqs[x], reverse=True)) # we sort the list
                         if i.upper() != i.lower()}    # we ignore "words" without letters and common words
    store_json(sorted_word_freqs, "word_frequencies_in_titles.json")
    
