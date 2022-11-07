# Section_5.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file contains all the information the player goes through in section 5 of the game


import Main_Character


def start():

    # intro to section 5

    # intro quote by Jones

    # section options described by narrator

    # section_5_options, give the player options to finish the game
    section_5_options = input("""
    a. Look around the room
    b. Grab Artifact
    c. Replace artifact with item in inventory""")

    # if player chooses to look around the room they will find a vase that they will need to progress
    if section_5_options == "a":
        # add a quote from jones describing what he is doing
        # add narration explaining what jones picks up and what he does with it
        print("Jones finds a vase and picks it up")
        # add vase to inventory
        # allow user to return to section_5_options

    # if the player chooses to remove the artifact they will lose because they will set off a trap
    elif section_5_options == "b":
        # add a quote from Jones
        print("""Jones decided to grab the vase and ended up setting off a trap. The doors started to close and Jones 
        tried running out but he couldn't make it. When the doors closed the room started to fill with water. Jones 
        tried to survive for as long as possible but inevitably died due to suffocation.""")
        # allow the user to return to section_5_options
        # remove option "b" when the user has tried it.

    # if the user replaces the artifact with another item in their inventory they will lose
    # the only item that can be used to replace the artifact is the vase found in option "a"
    elif section_5_options == "c":
        # add a quote from jones
        # give the player a choice as to what item they would like to replace the artifact with
        print("""Jones decided to replace the artifact with an item he had stored. But because the weight of the items
        did not match a trap was activated. The doors started to close and Jones tried running out but he couldn't make
        it. When the doors closed the room started to fill with water. Jones tried to survive for as long as possible 
        but inevitably died due to suffocation.""")

    else:
        print("Invalid Input. Please choose a letter from the choices")

# add a celebratory message if the player completes the game
# the only way for the player to succeed is for them to look around the room and to find the vase and then to replace
# the artifact with the vase thy acquired.
