# -----------------------------------------------
#   3. Data Parsing:
# 
#   Objective: Parse course data leveraging
#   HTML elements structure.
# 
#   Tools/Resources: Use resources like the 
#   DOMParser, BeautifulSoup, or Regular Expressions.
#       Beautiful Soup:
#           https://www.crummy.com/software/BeautifulSoup/
#       DOMParser:
#           https://developer.mozilla.org/en-US/docs/Web/API/DOMParser
#       RegEx:
#           https://regexr.com 
#           https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions
# -----------------------------------------------

from bs4 import BeautifulSoup
import json

def store_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('Data saved to: ', file)

f = open('combined.html', 'r')
html = f.read()
html = html.replace('\n', '').replace('\r', '') # removes weird indents
soup = BeautifulSoup(html, 'html.parser')
bodies = [body.contents for body in soup.find_all("div", class_="courseblock")]
exported_bodies = []

def plain_text (obj):
    """
    Function written to turn a set of text with tags into one without tags
    """
    output = ''
    for item in obj.contents:
        try:
            output += plain_text(item)
        except:
            try: 
                output += item.string
            except:
                output += ''
    return output


for body in bodies:
    title = body[0].contents[0].contents[0] #this is the course title
    try:
        desc = body[1].contents[0] # this is the course description
    except:
        desc = 'Offers elective credit for courses taken at other academic institutions. May be repeated without limit.' # all of the courses without descriptions are electives
    prereq = ''
    if len(body) == 4:
        prereq = plain_text(body[2]) # this would be the description of the prerequisites. currently, i don't pass this onto the final json but I might do in the future.
    prereq.replace('  ', ' ').replace('  ', ' ')
    exported_bodies.append((title, desc, prereq))



store_json(exported_bodies, 'bodies.json')




