print("Welcome to this evening's presentation!")
print("")
print("You wake up in unfamiliar room and your head hurts. You can't remember anything.")
print("You go check the door...")
answer = raw_input("Do you try to open the door? (yes/no) ")
if answer == "no":
    print("You do nothing to escape and you die of starvation.")
    print("You lose")
    print("")
    print("Game over!")
else:
    print("The door is locked. You are starting to remember...")
    print("Someone hit you in the head.")
    print("You look around room and you see a window.")
    print("You go to the window and...")
    answer = raw_input("Do you try to open a window? (yes/no) ")
    if answer == "no":
        print("You again do nothing to escape.")
        print("Someone opens the door and shoot you in the head.")
        print("You lose")
        print("")
        print("Game over!")
    else:
        print("Window is sealed shut. There is no escaping trough that window.")
        print("You look at the door and see shadow under it.")
        print("You know someone is standing there.")
        print("If kidnapper opens the door it might be your only chance to escape")
        answer = raw_input("Do you go to the door? (yes/no) ")
        if answer == "yes":
            print("When you get to the door they open and hit you in the head.")
            print("You bleed out and die.")
            print("You lose")
            print("")
            print("Game over!")
        else:
            print("You stand still unable to move.")
            print("Door open and you see man with a gun.")
            print("He points it at you and you think you are going to die.")
            print("")
            print("To be continued!")
            print("")
            print("Game over!")
