# -----------------------------------------------
#  7. Data Visualization:
#  Objective: Visualize the word frequencies
#  using a visualization library.
# 
#  Tools/Resources: Examples of visualization 
#  libraries D3, Plotly, and Chart.JS.
#     D3, https://d3js.org/
#     Plotly, https://plotly.com/
#     Chart.JS, https://www.chartjs.org/
#     Google Charts, https://developers.google.com/chart/
# -----------------------------------------------

import json
import plotly.express as px
len_graph = 500
keep_common_words = False

common_words_file = json.load(open('node_modules/common-words/words.json'))
common_words = {i['word'] for i in common_words_file} # loads a collection of some of the most commonly used words in English.

with open("word_frequencies_in_titles.json", "r", encoding='utf-8') as infile:
    word_frequencies = json.load(infile)
    word_frequencies = {i: word_frequencies[i] for i in word_frequencies.keys() if i not in common_words or keep_common_words} # we trim out common words
    fig = px.bar(x=list(word_frequencies.keys())[:len_graph], y = [i['frequency'] for i in list(word_frequencies.values())[:len_graph]])
    fig.update_xaxes(type='category') #since this is a catagorical graph
    fig.show()
    pass
    

