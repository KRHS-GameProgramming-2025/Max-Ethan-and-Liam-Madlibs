from Screens import *
from Getters import *
from Story1 import *


def Madlibs(debug = False):
    if debug: print("Welcome to debug")

    print(TitleScreen(debug))
    try:
    
        input("Press enter to continue")
    except:
        pass
        
    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption (debug)
        
        if choice == "q":
            exit()
        
        elif choice == "1":
            print(Story1(debug))
            print("\n")
            input("Press enter to continue")




Madlibs(False)
