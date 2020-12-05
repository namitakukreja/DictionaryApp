import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def srch(word):
    # print(data[word])
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if Yes , else N: " % get_close_matches(word, data.keys())[0])
        print(yn)
        if yn == 'Y' or yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N' or yn == 'n':
            return "Please re-enter correct word!!!"
        else:
            return "We could not get your request. Please try again"

    else:
        return "The word doesn't exist. Please re-verify!"

word = input("Enter word: ")
output = srch(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
