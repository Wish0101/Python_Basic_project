print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("\n\nWelcome to Treasure island :-)")
print("\t lets find the treasure --")
print("\n\n\n\tYou are in a castle which is located in a unknown island there's a treasure that will make richest person ")
print("\tlets start")
print("\t--you are in hall\n\t--there are two ways left and right where you want to go")
user_input1 = input("\t--").lower()
if user_input1 == "right":
    print("\t--There are lions\n\t--they ate you\n\t\t\t--Game Over--")
    
else:
    print("\t--You came out to the castle")
    print("\n\t--there a river you want to 'wait' for the boat or want to 'swim' and cross the river")
    user_input2 = input("\t--").lower()
    if user_input2 == "swim":
        print("\t--There are corcodial's\n\t--they ate you\n\t\t\t--Game Over--")
    else:
        print("\t--boat arived")
        print("\t--you cross the river")
        print("\n\t--There are three doors 'Red' , 'Blue' , 'Green'\n\t--you have to choose one door")
        user_input3 = input("\t--").lower()
        if user_input3 == "red":
            print("\t--You fall from the cliff\n\t\t\t--Game Over--")
        elif user_input3 == "blue":
            print("\n\t\t\t--You found the treasure--")
        else:
            print("\t--you caome to the lava room\n\t\t\t--Game Over--")
