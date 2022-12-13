# Section_5.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file contains all the information the player goes through in section 5 of the game
import GlobalVariables
import Main_Character


def start():
    # intro to section 5
    print("""The door slowly opened when Jones inserted the medallion. Jones eyes were adjusting 
to the change in light because the room was emitting a bright light.""")
    input("press 'enter' to continue\n")

    # intro quote by Jones
    print(Main_Character.MainCharacter.name,
          ''': "The light is so bright."''')
    input("press 'enter' to continue\n")

    # section options described by narrator
    print("""When Jones opened the door he was blinded by the light. He let his eyes
adjust. What should he do now?""")
    input("press 'enter' to continue\n")

    while "tablet" not in Main_Character.MainCharacter.inventory:
        # section_5_options, give the player options to finish the game
        section_5_options = input("""What would you like to do?
a. Look around the room
b. Grab Artifact
c. Replace artifact with item in inventory\n""")

        # if player chooses to look around the room they will find a vase that they will need to progress
        if section_5_options == "a":
            # add a quote from jones describing what he is doing
            print(Main_Character.MainCharacter.name,
                  ''': "I should look around the room to see what I can do."''')
            input("press 'enter' to continue\n")
            # add narration explaining what jones picks up and what he does with it
            print("Jones starts to look around the room.")
            input("press 'enter' to continue\n")

            choice = input("Jones finds a vase. Should he pick it up? (Y/N)")
            if choice.lower() == 'y':
                print(Main_Character.MainCharacter.name,
                      ''': "I should take this vase with me it might be useful for something."''')
                # add vase to inventory
                Main_Character.MainCharacter.inventory.append("vase")
                print("'vase' was added to inventory")
                input("press 'enter' to continue\n")

            elif choice.lower() == 'n':
                print(Main_Character.MainCharacter.name,
                      ''': "I will leave the vase here it seems useless"''')
                input("press 'enter' to continue\n")

            else:
                print("Invalid Input. Please choose a letter from the choices")

        # if the player chooses to remove the artifact they will lose because they will set off a trap
        elif section_5_options == "b":
            # add a quote from Jones
            print(Main_Character.MainCharacter.name,
                  ''': "I should try to grab the piece of the tablet."''')
            input("press 'enter' to continue\n")
            print("""Jones decided to grab the vase and ended up setting off a trap. The doors started to close and Jones 
tried running out but he couldn't make it. When the doors closed the room started to fill with water. Jones 
tried to survive for as long as possible but inevitably died due to suffocation.""")
            GlobalVariables.player_died()

        # if the user replaces the artifact with another item in their inventory they will lose
        # the only item that can be used to replace the artifact is the vase found in option "a"
        elif section_5_options == "c":
            GlobalVariables.replace_tablet()

        else:
            print("Invalid Input. Please choose a letter from the choices")

    # ending narration
    print("""Jones finally succeeded. He retrieved the tablet and can finally complete his research on
the ancient civilization that created the tablet. Lets hear what our adventurer has to say.""")
    input("press 'enter' to continue\n")

    # Jones finishing quote
    print(Main_Character.MainCharacter.name,
          ''': "I have searched so long for the meaning behind this tablet and now that I have it
                  completed I can see that this was a waste of time. The tablet was just an ancient
                  tic-tac-toe board. I HATE MY LIFEEEEEEEE!!!!"''')
    input("press 'enter' to continue\n")

    # last narration
    print("""Well that's all folks the story is finally FUCKING over so get outta here.""")
    print("GAME OVER!!")
    print("You died", GlobalVariables.player_death_count, "times. You are trash at games.")
    exit()


# add a celebratory message if the player completes the game
# the only way for the player to succeed is for them to look around the room and to find the vase and then to replace
# the artifact with the vase they acquired.
# start()
