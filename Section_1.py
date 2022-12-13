# Section_1.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file contains all the information the player goes through in section 1 of the game


import Main_Character
import GlobalVariables
import Section_2


def start():
    # Intro to first section
    print("""
Jones has travelled to a small remote town in India in search
of an artifact that he needs for the final piece of an Aztec tablet
he has been collecting for the past six years. As he arrives, he is
greeted by the cries of the town exclaiming that they have lost their
children due to an evil gods wrath.""")
    input("press 'enter' to continue\n")

    # Jones quote
    print(Main_Character.MainCharacter.name, ''': “I must find the missing piece only then will I finally solve the 
                mysteries of this ancient Aztec tablet.”''')
    input("press 'enter' to continue\n")

    # checks if the player has talked to the elder and then slept
    while GlobalVariables.check != 2:
        # First choice the player is allowed to make
        section_1_options = input("""
a. Ask the villagers what happened
b. Look around the town
c. Talk to the Elder Chief of the village
d. Rest for the day\n""")

        # This happens when the user chooses "a" for the first option
        if section_1_options == "a":
            print(Main_Character.MainCharacter.name, ''': “I should check on the villagers and figure out whats wrong with
                them. Hopefully I can help them out.”''')
            input("press 'enter' to continue\n")
            print('''
The villagers explain to Jones that they have lost their children
to a vengeful god who tasked them with protecting a sacred 
artifact that was precious to the god.They explain to Jones that
the children where all taken to the a temple on the outskirts of
the village. They call this temple "THE TEMPLE OF DOOM!!"''')
            input("press 'enter' to continue\n")

        # This happens when the user chooses "b" for the first option
        elif section_1_options == "b":
            print(Main_Character.MainCharacter.name, ''': “I should look around the village and see what I find.”''')
            input("press 'enter' to continue\n")
            print('''
Jones finds a villager selling items. He checks out the items
and notices that he is selling a torch for $80 and bullets for $10
per bullet.''')
            GlobalVariables.village_store()

        elif section_1_options == "c":
            print(Main_Character.MainCharacter.name, ''': “I should check if this village has an Elder and 
                talk to them to figure out what is happening and what I can do.”''')
            input("press 'enter' to continue\n")

            print('''
Elder: "Hello young one I hope you found your voyage fulfilling, I am the leader of this village. 
We have recently come into a situation with our god. We have been taking care of a precious item of his and 
it was recently stolen. I believe that artifact was taken into a temple near our village but there is a 
saying in our history that says no one who enters has ever left alive. If you plan to travel to the temple 
you must go at NIGHT that is the only time the temples doors are open. Please be careful on your adventures!"''')
            input("press 'enter' to continue\n")

            print(Main_Character.MainCharacter.name, ': “I should check out the temple after I rest until NIGHT.”')
            # adds 1 to the global variable check to symbolize that the player talked to the elder
            GlobalVariables.check += 1
            input("press 'enter' to continue\n")

        # this option will allow the user to sleep so that they can change the current time in game
        elif section_1_options == "d":
            GlobalVariables.day_night()
            if GlobalVariables.check == 2:
                Section_2.start()
            else:
                continue

        else:
            print("Invalid Input. Please choose a letter from the choices")

# start()  # <-- test if section works
