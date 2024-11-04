def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")

    goodInput = False
    while not goodInput:
        option = input("Please select an option" " ")
        option = option.lower()
        
        if option == "q" or option == "quit" or option == "exit" or option == "x":
            option = "q"
            goodInput = True
            
        elif option == "story 1" or option == "1" or option == "one" or option == "story1":
            option = "1"
            goodInput = True
            
        else:
            print ("Please make a valid choice" " ")
            
    return option

def getWord(prompt, debug = False):
    if debug: print("getWord Function")

    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear(word):
            goodInput = False
            print("brother eugh")

    return word


def getTown(prompt, debug = False):
    if debug: print("getTown Function")

    goodInput = False
    
    townList = ["Sutton",
                "North Sutton",
                "Wilmot",
                "Newbury",
                "Warner",
                "New London",
                "Bradford",
                "Springfield",
                ]
    
    while not goodInput:
        word = input(prompt)
        
        if isSwear(word):
            goodInput = False
            print("brother eugh")
        elif word.title() in townList:
            goodInput = True
        else:
            print("I don't know that town yet, please choose another one")

    return word.title()
    
    
    
def getOption(prompt, optionList, debug = False):
    if debug: print("getOption Function")
    
    goodInput = False
    
    
    while not goodInput:
        word = input(prompt)
        
        if isSwear(word):
            goodInput = False
            print("brother eugh")
        elif word.lower() in optionList:
            goodInput = True
        else:
            print("That isn't an avalible option")

    return word.lower()


def isSwear(word, debug = False):
    if debug: print ("isSwear Function")
    if word in swearList:
        return True
    else:
        return False


swearList = ["bitch",
             "ass",
             "asshole",
             "fuck",
             "fucking",
             "fucker",
             "fuckin",
             "shit",
             "shitter",
             "shitting",
             "nigga",
             "nigger",
             "niggas",
             "niggers",
             "fag",
             "faggot",
             "fags",
             "gyatt",
             "skibidi",
             "rizz",
             "cunt",
             "cum"
             "jizz",]
