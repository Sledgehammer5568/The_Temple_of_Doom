# Section_2.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file contains all the information the player goes through in section 2 of the game


import Main_Character
import GlobalVariables
import Section_3


def start():
    # intro to Section_2
    print('''
Jones was told by the Elder that the artifact he is searching for can
be found within a temple near the village called "The Temple of Doom" but
he can only enter at night. Jones travels to the temple after sleeping.''')
    input("press 'enter' to continue\n")

    # different dialog given if player decided to buy the torch in Section_1
    if 'torch' in Main_Character.MainCharacter.inventory:
        print("""
Jones travels at night to the outskirts of the village in search of the 
temple. He uses the torch he bought from the merchant earlier to travel 
safely through the night. He soon makes it to the entrance of the temple.""")
        input("press 'enter' to continue\n")
    else:
        print("""
Jones stumbles through the night trying to find his way to the temple. 
It takes him a while to arrive to the entrance of the temple since 
he does not have a torch to light his way.""")
        input("press 'enter' to continue\n")

    print(Main_Character.MainCharacter.name, ''': "The Elder told me I could find the artifact within a temple they call 
                'the Temple of Doom' I must travel through this temple and investigate."''')
    input("press 'enter' to continue\n")

    # if the player bought a torch they have less options because they don't need to make/buy the torch again
    if 'torch' in Main_Character.MainCharacter.inventory:
        while True:
            section_2_options_1 = input("a. Enter the Temple\nb. Return to Village store\n")
            # if the player has a torch in their inventory they can progress to the next section
            if section_2_options_1.lower() == "a":
                print("""
Jones enters the temple illuminating his way with the torch and notices
a trap in the entrance. He avoids the trap and enters the temple""")
                input("press 'enter' to continue\n")
                Section_3.start()

        # the player will always have the option to go back to the village in case they want to buy bullets for their gun
            elif section_2_options_1.lower() == "b":
                print("Jones returns to the village.")
                GlobalVariables.village_store()

        # this just checks that the user doesn't input anything else but "a" and "b"
            else:
                print("Invalid Input. Please choose a letter from the choices")

    # if the player doesn't have a torch they will be allowed to look around the temple to make their own torch or to go
    # back to the village and buy one from the store
    else:
        while not GlobalVariables.player_death:
            section_2_options_2 = input("a. Enter the Temple\nb. Return to village store\nc. Sleep by entrance\n")

            # if the player enters the temple without a torch they step on a trap and die.
            if section_2_options_2 == "a":
                # check if player has a torch and let them continue with the story if they do
                if 'torch' in Main_Character.MainCharacter.inventory:
                    print("""
Jones enters the temple illuminating his way with the torch and notices a trap in the entrance.
he avoids the trap and enters the temple""")
                    input("press 'enter' to continue\n")
                    Section_3.start()
                # if player does not have torch, and they enter the temple they die
                else:
                    print("""
Jones enters the dark temple with out a clue as to where hes going.
As he enters the temple he steps on a trap that kills him""")
                    GlobalVariables.player_died()
                    start()
                # have a message that shows that the player died and make a counter for how many deaths they had

            # the player will also have the option of returning to the village to buy the torch if they arrive to Section_2
            # without one.
            elif section_2_options_2 == "b":
                print("Jones returns to the village store.")
                GlobalVariables.village_store()
            # I have to figure out a way to allow the user to return to the village and repeat this section

            elif section_2_options_2 == "c":
                print("")

            # this just checks that the user doesn't input anything else but "a", "b" and "c"
            else:
                print("Invalid Input. Please choose a letter from the choices")

# add another option to this section so that the user can sleep in case they took damage from fighting enemies while
# looking around the entrance of the temple
# start()
