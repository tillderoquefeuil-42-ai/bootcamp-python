import re

def text_analyzer(text=None):

    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''

    if text is None:
        text = input("What is the text to analayze?\n")

    # characters
    print("The text contains " + str(len(text)) + " characters:")

    # upper
    upper = len(re.findall(r"[A-Z]", text)) 
    print("\n- " + str(upper) + " upper letters")
    
    # lower
    lower = len(re.findall(r"[a-z]", text)) 
    print("\n- " + str(lower) + " lower letters")

    # ponctuation marks
    ponctuation = len(re.findall(r"[!\"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", text)) 
    print("\n- " + str(ponctuation) + " punctuation marks")

    # spaces
    print("\n- " + str(text.count(" ")) + " spaces")
