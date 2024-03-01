# -----------------------------------------------
#   4. Data Cleaning:
# 
#   Objective: Clean and preprocess the 
#   extracted data for analysis.
# 
#   Tools/Resources: Use Regular Expressions 
#   or string manipulation functions in 
#   your programming language.
# 
#    
# -----------------------------------------------

import json

def store_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print('Data saved to: ', file)

def add_strings_in_array(arr, start, end, char=''):
    """
    Function takes in an array, start index, end index, and string to put in between them
    """
    output = ''
    for i in range(start, end-1):
        output += arr[i]
        output += char
    output += arr[end-1]
    return output

def mod_item(item):
    """
    this function takes a course item and puts it into a format we can use.
    """
    output = [] #[course department, course #, course name, hours, description, [prerequisites (not right now)]]
    split_course = item[0].split(".")
    output.extend(split_course[0].split("\xa0")) # course department and number
    output.append(add_strings_in_array(split_course, 1, len(split_course) - 1, '.').strip()) # course name. I had to do this funky thing because U.S. Foreign Policy has periods in its title.
    hrs_string = split_course[-1].replace("(", "").replace(")", "").strip().split(" ")[0]
    try:
        output.append([int(hrs_string), int(hrs_string)]) # array is like [minimum possible hours, maximum possible hours]
    except:
        hrs = [int(i) for i in hrs_string.replace(",", "-").split("-")] # some thesises have this thing where like they say "4,8 hours"? electives have 1-4 hours usually, so this is a workaround for them. Unfortunately, we lose the dashes.
        output.append(hrs) 

    output.append(item[1].strip())
    return output


with open("bodies.json", "r", encoding='utf-8') as infile:
    bodies = json.load(infile)
    output_bodies = [mod_item(body) for body in bodies] #
    store_json(output_bodies, 'cleaned_bodies.json') 

