# -----------------------------------------------
#  2. Data Preparation:
# 
#  Objective: Combine multiple HTML files into 
#  a single document.
# 
#  Tools/Resources: Concatenate HTML text using 
#  python or javascript.
# -----------------------------------------------
import glob, os

os.chdir(".")

with open('combined.html', 'w') as outfile:
    for file in glob.glob("filedump/*.html"):
        with open(file) as infile:
            outfile.write(infile.read()) # writes the html script into the combined file
