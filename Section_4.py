# Section_4.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file contains all the information the player goes through in section 4 of the game


import Main_Character
import Section_5


def start():

    # Jones intro quote for this section

    # intro to section 4

    # Jones quote explaining what's around him and what he has done so far

    # Give the player option to choose what to do next in this section
    section_4_options = input("""
    a. Investigate the Door
    b. Rest Near the Door
    c. Return to Village""")

    # If player chooses to investigate the door Jones will explain what he sees on the door and record it taking an
    # imprint of the door with charcoal paper. Ones this is done the player must return to the village and talk
    # to the Elder to get an item from him so the player can continue
    if section_4_options == "a":
        print("""Add text about the door and how it's locked""")
        Section_5.start()

    # the player will be allowed to rest so that they can regain health if they lost any in the previous sections
    elif section_4_options == "b":
        print(Main_Character.MainCharacter.name, ': “I should rest for a while.”')

        # this changes day to night
        if Main_Character.DayNight.day is True and Main_Character.DayNight.night is False:
            Main_Character.DayNight.day += False
            Main_Character.DayNight.night += True
            print("You rested until Night.")

            # this checks if the player has lost life points and if they have when they rest they regain 10 points
            if Main_Character.MainCharacter.life < 100:
                Main_Character.MainCharacter.life += +10
                print("While resting you regenerated to:", Main_Character.MainCharacter.life, "life points")
                input("press 'enter' to continue\n")
            else:
                print("You are full health.")
                input("press 'enter' to continue\n")

        # this changes it from night to day
        elif Main_Character.DayNight.night is True and Main_Character.DayNight.day is False:
            Main_Character.DayNight.day += True
            Main_Character.DayNight.night += False
            print("You rested until Day.")

            # this checks if the player has lost life points and if they have when they rest they regain 10 points
            if Main_Character.MainCharacter.life < 100:
                Main_Character.MainCharacter.life += +10
                print("While resting you regenerated to:", Main_Character.MainCharacter.life, "life points")
            else:
                print("You are full health.")

    # the player will have to return to the village to speak to the elder.
    elif section_4_options == "c":
        print("Jones returns to the village.")

    else:
        print("Invalid Input. Please choose a letter from the choices")

# add a way to check for an item that the player must receive from the elder in the village
# add a way to inspect the door and if the player has gone back to the Elder and received the item then they continue
# to Section_5
