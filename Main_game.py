# Main_game.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file is the main game of the project that runs all other code in the project


import Section_1
import Section_2
import Section_3
import Section_4
import Section_5
import Main_Character

# intro to game
print("""
Hope you enjoy!\n
Hello, step forward young one!
Let me tell you the story of an incredible adventurer.""")
input("press 'enter' to continue\n")

print("""
The story begins with an adventure named Indiana Jones.
He has been searching for the pieces of an ancient tablet for some time now,
and he has finally discovered the location of the last piece.""")
input("press 'enter' to continue\n")

Section_1.start()

# I want to add a way for the player to check what they have in their inventory in all sections
# I want to add a way for the player to check how many bullets they have in their inventory in all sections
# add a way for the user to fight with monsters
# figure out a way to loop the sections so that the player can go through all options
# figure out a way to check for multiple requirements before allowing user to go to next section
# allow user to display their health any time they want
# to add a way for options to be removed if they serve no purpose anymore
# for section 3 - 5 add a way for the player to return to the village but only if it's night
# add a way for the player to know what time it is at all times
# add a way for the user to retry at every input section if they accidentally typed the wrong thin
