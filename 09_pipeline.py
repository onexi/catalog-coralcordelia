# -----------------------------------------------
#  9. Data pipeline:
# 
#  Write a program that automates the 
#  sequential execution of previously created 
#  script files, ensuring that each script 
#  runs to completion before the next begins. 
#  This program aims to streamline the 
#  generation of outputs from all your 
#  previous files, consolidating the 
#  results into one sequence.
# -----------------------------------------------
"""
Required modules/things to install before running:
- ssl
- plotly
- bs4
Run time is at most a few minutes
Notice that many files will get loaded while running the program. This is also why filedump is empty; running the program will fill the thing
"""


import os

os.system('npm i common-words --save-dev') # pulls the common words thing 




print('Pulling data from online...')
os.system('python 01_pull.py')
print('Combining data...')
os.system('python 02_combine.py')
print('Parsing data...')
os.system('python 03_parse.py')
print('Cleaning data...')
os.system('python 04_clean.py')
print('Extracting data...')
os.system('python 05_extract.py')
print('Generating word frequency...')
os.system('python 06_frequency.py')
print('Generating visualization...')
print('If the program pauses for too long, do CONTROL+C then run 07_visualization.py afterwards to see the visualization!')
os.system('python 07_visualization.py')
print('Exporting data...')
os.system('python 08_export.py')
   

