from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function")

    print("\n")
    friendName1 = getWord("Enter a name for your friend: ", debug)
    town = getTown("Enter a town in the Kearsarge district: ", debug)
    playerName1 = getWord("Enter your name: ", debug)
    
    out = ""
    out += "Today, me and my friend, " + friendName1
    out += " were going on a bike ride to the new bike park in " + town
    out += ". When we got there, we started doing jumps and wheelies until " + friendName1
    out += "'s tyre popped. " 
    out += friendName1 + " asked me " 
    out += "'"
    out += playerName1 + ", should we go back and fix it, or just share your bike?'"
    
    print(out)

    option = getOption ("Type '1' to go home and change the tyre. Type '2' to share your bicycle with " + friendName1, ["1", "2"], debug)
    out = ""
    
    if option == "1":
        print("You go back to your house with " + friendName1 + " and put a new tyre on his bike and enjoy the rest of the day at the park.")
        
    if option == "2":
        print("You and " + friendName1 + " share your bycicle, and enjoy the rest of the day at the park.")
    

    return out
