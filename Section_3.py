# Section_3.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file contains all the information the player goes through in section 3 of the game


import Main_Character
import Section_4


def start():

    # intro to Section_3
    print("""Jones has traveled inside the temple and avoided a pressure plate that would set off a trap. He now must 
    decide what direction he would like to continue in since this temple is setup like a maze.""")
    input("press 'enter' to continue\n")

    # Jones Section_3 quote
    print(Main_Character.MainCharacter.name, '''"This temple is eerie, and there seem to be traps everywhere I must 
                tread carefully and find the artifact within."''')
    input("press 'enter' to continue\n")

    # Narrator decision intro Section_3
    print("""Jones has safely entered the temple and is now presented with another predicament. The temple has split 
    off into 3 corridors and he has no way of knowing which way is correct. He must decide what way to go before 
    continuing.""")
    input("press 'enter' to continue\n")

    # Jones Section_3 quote 2
    print(Main_Character.MainCharacter.name, '''"I can see three different paths ahead of me I wonder which one is 
                the correct one? I can go left, right or continue going forward. It might
                be wise to rest at the entrance before continuing as well"''')
    input("press 'enter' to continue\n")

    # Ask the user for their input
    section_3_options = input("""
a. Go Left
b. Go Straight
c. Go Right
d. Get some rest before continuing
e. Return to Village""")

# if the player goes left they will end up dying to a trap that they couldn't avoid
    if section_3_options == "a":
        print("""
Jones decided to go left. He followed the path for a while not noticing he had set off a trap that 
locked him in this tunnel. Their was no end to this tunnel and Jones died from starvation.""")
        input("press 'enter' to continue\n")
# add a way to show the player died and a way for them to retry from the last part they were in
# add a death to the death counter

# if the player goes straight they will encounter a Hard enemy, if they beat it they can go back and try a different
# option but if they lose the battle against the hard enemy it will be game over. The player can also run from the
# enemy if they do not want to fight, but they will lose life points. If their life points reach 0 it will be game over.
    elif section_3_options == "b":
        print("""
Jones decided to continue going straight. He continued walking down this path 
until he encountered a huge monster Jones must now decide what to do.""")
        input("press 'enter' to continue\n")
        # add a fighting scene against a hard enemy. give player options. a. fight, b. run

# if the player chooses to go right they will face off against a medium enemy and if they defeat it they will be able
# to continue to the next section. If the player loses against the enemy it will be game over.
    elif section_3_options == "c":
        print("""
Jones decided to go to the right. After walking down this path for a while he encounters
an enemy. He must defeat the enemy to continue walking down this path. What will Jones do?""")
        input("press 'enter' to continue\n")
        # add a fighting scene against a hard enemy. give player options. a. fight, b. run
        # if the player defeats the enemy they can continue to Section_4
        # add a way to allow the player to return to the previous section if they would like
        Section_4.start()

    elif section_3_options == "d":
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

    elif section_3_options == "e":
        print("Jones returns to the village.")

    else:
        print("Invalid Input. Please choose a letter from the choices")
