# Section_4.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file contains all the information the player goes through in section 4 of the game


import Main_Character
import GlobalVariables
import Section_5


def start():
    # Jones intro quote for this section
    print(Main_Character.MainCharacter.name,
          ''': "After getting past that horrifying beast I continued walking through the corridor."''')
    input("press 'enter' to continue\n")

    # intro to section 4
    print("""Jones fought hard to get through that beast and has been traveling down the corridor
for a while now. He soon reaches something unexpected.""")
    input("press 'enter' to continue\n")

    # Jones quote explaining what's around him and what he has done so far
    print(Main_Character.MainCharacter.name,
          ''': "I came upon a massive door"''')
    input("press 'enter' to continue\n")

    # add a while loop to allow the user to pick all options
    while True:
        # Give the player option to choose what to do next in this section
        section_4_options = input(
            """What would you like to do?
a. Investigate the Door
b. Rest Near the Door
c. Return to Village\n""")

        # If player chooses to investigate the door Jones will explain what he sees on the door and record it taking an
        # imprint of the door with charcoal paper. Ones this is done the player must return to the village and talk
        # to the Elder to get an item from him so the player can continue
        if section_4_options == "a":
            print(
                """The door seems to be locked. There seems to be a weirdly shaped indent in
the center of the door.""")
            if "medallion" in Main_Character.MainCharacter.inventory:
                print("Jones went to the village and convinced the elder to let him use the medallion.")
                print("The medallion seems to be the key for the door.")
                input("press 'enter' to continue\n")
                print(Main_Character.MainCharacter.name, ''': "I think I can unlock the door with the medallion."''')
                input("press 'enter' to continue\n")
                # remove the medallion from the players inventory after use on door
                Main_Character.MainCharacter.inventory.remove("medallion")
                Section_5.start()
            else:
                print("Jones uses charcoal paper to take an imprint of the indent on the door.")
                input("press 'enter' to continue\n")

                print(Main_Character.MainCharacter.name,
                      ''': "I remember the elder having a medallion that looks like 
                the indent on the door. I should go talk to him in the village 
                and try to convince him to let me use it."''')
                input("press 'enter' to continue\n")

        # this option will allow the user to sleep so that they can change the current time in game
        elif section_4_options == "b":
            # call the day night function
            GlobalVariables.day_night()

        elif section_4_options == "c":
            if not GlobalVariables.day:
                print("Jones returns to the village.")
                # call the return elder function
                GlobalVariables.return_elder()
            else:
                print("You can only return to the village at night.")
                input("press 'enter' to continue\n")

        else:
            print("Invalid Input. Please choose a letter from the choices")

# add a way to check for an item that the player must receive from the elder in the village
# add a way to inspect the door and if the player has gone back to the Elder and received the item then they continue
# to Section_5
# start()
