import json
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #.title() method returns a copy of the string in which first characters of all the words are capitalized
        return data[word.title()]
    elif word.upper() in data: #.upper() returns a copy of the string in which all case-based characters have been uppercased
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        YN = input("Did you mean to type '%s'? Type y for yes or n for no: " % get_close_matches(word, data.keys())[0])
        YN = YN.lower()
        if YN == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif YN == 'n':
            return "Word does not exist in Dictionary, please try again!"
        else:
            return "Not a valid entry, please try again!"
    else:
        return "Word does not exist in Dictionary."

word = input("Enter a word: ")
output = (get_definition(word))
if type(output) == list:
    for o in output:
        print(o)
else:
    print(output)
