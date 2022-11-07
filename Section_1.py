# Section_1.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: This file contains all the information the player goes through in section 1 of the game


import Main_Character
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

    # First choice the player is allowed to make
    section_1_choices = input("""
a. Ask the villagers what happened
b. Look around the town
c. Talk to the Elder Chief of the village
d. Rest for the day\n""")

    # This happens when the user chooses "a" for the first option
    if section_1_choices == "a":
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
    elif section_1_choices == "b":
        print(Main_Character.MainCharacter.name, ''': “I should look around the village and see what I find.”''')
        input("press 'enter' to continue\n")
        print('''
Jones finds a villager selling items. He checks out the items
and notices that he is selling a torch for $80 and bullets for $10
per bullet.''')

        # Assigning a new variable so that we can allow the user to choose what to buy from the store
        store_choice = input('''
Would you like to buy any of these items
a. Torch
b. Bullets
c. Exit\n''')

        # If the user has enough money this choice allows the user to purchase a torch
        if store_choice == "a":

            # Program checks if the user has enough money to buy the torch, if they don't they can't buy
            if Main_Character.MainCharacter.money < 80:
                print("Store owner: Sorry you do not have enough money.")
                print("Balance:", Main_Character.MainCharacter.money)

            # If the player has enough money they are allowed to buy the torch, torch added to inventory
            else:
                Main_Character.MainCharacter.money += -80
                Main_Character.MainCharacter.inventory += "torch"
                print(Main_Character.MainCharacter.name, ': “I will buy the torch.”')
                input("press 'enter' to continue\n")
                print("Jones decides to buy the torch")
                print('"torch" added to inventory')
                print("Balance:", Main_Character.MainCharacter.money)  # print balance after purchase
                input("press 'enter' to continue\n")

        # If the user has funds this choice allows the user to purchase a number of bullets that they decide
        elif store_choice == "b":
            print("Balance:", Main_Character.MainCharacter.money)
            bullet_amount = int(input("Store owner: How many bullets would you like to buy?\n"))
            print(Main_Character.MainCharacter.name, ': “I would like to buy', bullet_amount, 'bullets.')
            input("press 'enter' to continue\n")
            price_bullets = 10 * bullet_amount  # program calculates how much it will cost to buy the amount of bullets

            # Program checks if the player has enough to pay for at least 1 bullet, if they don't they can't buy
            if Main_Character.MainCharacter.money < 10:
                print("Store owner: Sorry you do not have enough money.")
                print("Balance:", Main_Character.MainCharacter.money)

            # Program checks if the player has enough money to pay for the amount of bullets they chose
            # if the user doesn't have enough money they can't buy
            elif price_bullets > Main_Character.MainCharacter.money:
                print("Store owner: Sorry you do not have enough money.")
                print("Balance:", Main_Character.MainCharacter.money)

            # If the checks are met then the player is allowed to buy the amount of bullets they chose
            else:
                Main_Character.MainCharacter.money += - (10 * bullet_amount)
                Main_Character.MainCharacter.bullets += +bullet_amount  # add the bullets bought to the players bullets
                price_bullets = str(price_bullets)
                bullet_amount = str(bullet_amount)
                print("Jones decides to buy " + bullet_amount + " for " + "$" + price_bullets + ".")
                print("Bullets in Inventory:", Main_Character.MainCharacter.bullets)  # updated amount of bullets
                print("Balance:", Main_Character.MainCharacter.money)  # print balance after purchase
                input("press 'enter' to continue\n")

    elif section_1_choices == "c":
        print(Main_Character.MainCharacter.name, ''': “I should check if this village has an Elder and 
                        talk to them to figure out what is happening and what I can do.”''')
        input("press 'enter' to continue\n")

        print('''
"Elder: Hello young one I hope you found your voyage fulfilling, I am the leader of this village. 
We have recently come into a situation with our god. We have been taking care of a precious item of his and 
it was recently stolen. I believe that artifact was taken into a temple near our village but there is a 
saying in our history that says no one who enters has ever left alive. If you plan to travel to the temple 
you must go at NIGHT that is the only time the temples doors are open. Please be careful on your adventures!"''')
        input("press 'enter' to continue\n")

        print(Main_Character.MainCharacter.name, ': “I should check out the temple after I rest until night.”')
        input("press 'enter' to continue\n")

    # this option will allow the user to sleep so that they can change the current time in game
    elif section_1_choices == "d":
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
    else:
        print("Invalid Input. Please choose a letter from the choices")
    if section_1_choices == "d":
        Section_2.start()
    # I want there to be 2 things checked before the player can continue
    # for now if the player chooses "d" as an option they automatically continue
    # if section_1_choices == "c" and Main_Character.DayNight.night is True:
    #     Section_2.start()
