# -----------------------------------------------
#  8. Export a Clean Formatted Dataset
#  of the Entire University Catalog:
# 
#  Export a Clean Formatted Dataset of 
#  the Entire University Catalog: The 
#  dataset you would have liked when you 
#  started. Prepare and export a clean, 
#  well-formatted dataset encompassing 
#  the entire university catalog. This 
#  dataset should be in a form that is 
#  readily usable for analysis and 
#  visualization, reflecting the cleaned 
#  and consolidated data you've worked 
#  with throughout the project. Document 
#  the structure of your dataset, including 
#  a description of columns, data types, and 
#  any assumptions or decisions made during 
#  the data preparation process.
# -----------------------------------------------
"""
A few assumptions that were made:
- There is no partial Course Hour count
- Each thing in the Course Hour thing was formatted "(# Hours)", "(#-# Hours)", or "(#.# Hours)
- Each course title is of the form (Department) (Course Number). (Course Title). (# of hours)
- Each course on https://catalog.northeastern.edu/course-descriptions/ was listed under the letters

A few things to note:
- On 07_visualization.py, you can choose to include common words or increase the number of words graphed.
- In cleaning, I had to make an adjustment so that "U.S." wouldn't cause issues.
- Some courses had no description, but were electives, so I filled their descriptions.

The format of the data is:
[
    {  
        'Department': ..., # records department that the course is in - string
        'Course Code': ..., # recordes the... uh... course code? - string
        'Course Name': ..., # records the name of the course (including department) - string
        'Course Hours': ..., # records number of hours obtained by taking the course. Is a string because things like 1-4 hours exist
        'Course Description': ... # course description - string
    }
]

Note that I didn't add the course prerequisites (yet...)

It is sorted by course name in alphabetical order.

"""


import json

def store_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('Data saved to: ', file)

with open('cleaned_bodies.json') as infile:
    bodies = json.load(infile)
    formatted_dataset = []
    for i in bodies:
        item = { 
            'Department': i[0], # records department that the course is in - string
            'Course Code': f"{i[0]} {i[1]}", # recordes the... uh... course code? - string
            'Course Name': i[2], # records the name of the course - string
            'Course Hours': "", # records # of hours obtained by taking the course. Is a string because things like 1-4 hours exist
            'Course Description': i[4] # course description - string
        }
        if i[3][0] != i[3][1]:
            item['Course Hours'] = f"{i[3][0]}-{i[3][1]}"
        else:
            item['Course Hours'] = f"{i[3][0]}"
        formatted_dataset.append(item)
    formatted_dataset = sorted(formatted_dataset, key=lambda a: a['Course Code']) # sorts the dataset by alphabetical order
    store_json(formatted_dataset, 'Northeastern_Courses.json')
