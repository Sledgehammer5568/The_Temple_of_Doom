# GlobalVariables.py
#
# Emanuel Ramos
# 12/02/2022
#
# Description: file containing the global variables and functions that are tracked throughout the game

from Main_Character import MainCharacter as Mc
from Main_Character import Enemy

day = True  # starting value of day
check = 0
player_death = False
player_death_count = 0
name = Mc.name
money = Mc.money
bullets = Mc.bullets
life = Mc.life
inventory = Mc.inventory
battle_finished = False


def g_vars():
    global day
    global check
    global player_death
    global player_death_count
    global name
    global money
    global bullets
    global life
    global inventory
    global battle_finished


# function that allows for a day cycle
def day_night():
    global day, check
    print(Mc.name, ': “I should rest for a while.”')

    # this changes day to night
    if day is True:
        day = False
        check += 1  # add 1 to global variable check so that it's possible to continue into temple
        print("You rested until Night.")

        # this checks if the player has lost life points and if they have when they rest they regain 10 points
        if Mc.life < 100:
            Mc.life += 10
            print("While resting you regenerated to:", Mc.life, "life points")
            input("press 'enter' to continue\n")
        else:
            print("You are full health.")
            input("press 'enter' to continue\n")

    # this changes it from night to day
    elif day is False:
        day = True
        check -= 1  # remove a check if the
        print("You rested until Day.")

        # this checks if the player has lost life points and if they have when they rest they regain 10 points
        if Mc.life < 100:
            Mc.life += 10
            print("While resting you regenerated to:", Mc.life, "life points")
        else:
            print("You are full health.")


# function for the village store to allow the user to buy
def village_store():
    while True:
        print("Current balance:", Mc.money)  # print balance after purchase
        # Assigning a new variable so that we can allow the user to choose what to buy from the store
        store_choice = input('''
Would you like to buy any of these items
a. Torch
b. Bullets
c. Exit\n''')

        # If the user has enough money this choice allows the user to purchase a torch
        if store_choice == "a":

            # Program checks if the user has enough money to buy the torch, if they don't they can't buy
            if Mc.money < 80:
                print("Store owner: Sorry you do not have enough money.")
                print("Balance:", Mc.money)

            # If the player has enough money they are allowed to buy the torch, torch added to inventory
            else:
                Mc.money -= 80
                Mc.inventory.append("torch")
                print(Mc.name, ': “I will buy the torch.”')
                input("press 'enter' to continue\n")
                print("Jones decides to buy the torch")
                print('"torch" added to inventory')
                print("Balance:", Mc.money)  # print balance after purchase
                input("press 'enter' to continue\n")

        # If the user has funds, this choice allows the user to purchase a number of bullets that they decide
        elif store_choice == "b":
            print("Balance:", Mc.money)
            bullet_amount = int(input("Store owner: How many bullets would you like to buy?\n"))
            print(Mc.name, ': “I would like to buy', bullet_amount, 'bullets.')
            input("press 'enter' to continue\n")
            price_bullets = 10 * bullet_amount  # program calculates how much it will cost to buy the amount of bullets

            # Program checks if the player has enough to pay for at least 1 bullet, if they don't they can't buy
            if Mc.money < 10:
                print("Store owner: Sorry you do not have enough money.")
                print("Balance:", Mc.money)

            # Program checks if the player has enough money to pay for the amount of bullets they chose
            # if the user doesn't have enough money they can't buy
            elif price_bullets > Mc.money:
                print("Store owner: Sorry you do not have enough money.")
                print("Balance:", Mc.money)

            # If the checks are met then the player is allowed to buy the amount of bullets they chose
            else:
                Mc.money -= (10 * bullet_amount)
                Mc.bullets += bullet_amount  # add the bullets bought to the players bullets
                price_bullets = str(price_bullets)
                bullet_amount = str(bullet_amount)
                print("Jones decides to buy " + bullet_amount + " for " + "$" + price_bullets + ".")
                print("Bullets in Inventory:", Mc.bullets)  # updated amount of bullets
                print("Balance:", Mc.money)  # print balance after purchase
                input("press 'enter' to continue\n")

        # break the loop when player chooses "EXIT"
        elif store_choice == "c":
            break

        else:
            print("Incorrect input please try again")


# function to change the value of Player_death to make a check if the player has died, and add 1 to player death count
def player_died():
    # change value of player_death to true
    global player_death, player_death_count
    player_death = True
    # add 1 to player_death_count which will be displayed at the end and whenever they die
    player_death_count += 1
    # reset player_death global variable so that game can continue
    player_death = False
    print("A death was added to the death count.")
    print("You have:", player_death_count, "deaths.")
    input("press 'enter' to continue\n")


# battle function
def battle(enemy_type):
    global player_death, battle_finished, player_death_count
    # show the enemies stats
    print("This enemy has", enemy_type.life, "life points.")
    print("The enemy deals", enemy_type.attk_dmg, "damage.")
    input("press 'enter' to continue\n")

    # show the players stats
    print("You currently have", Mc.life, "health points.")
    print("You currently have", Mc.bullets, "bullets.")

    while not battle_finished:
        # allow the player to choose whether to fight or run away
        fight_run = input("would you like to fight or run? (F/R)\n")
        input("press 'enter' to continue\n")

        # if the player chooses F or f start the fight
        if fight_run.lower() == 'f':
            # print the damage each weapon does before allowing the player to choose
            print("The gun does 100 damage and the whip does 25 damage")
            # allow the player to attack first, give them a choice of weapon
            weapon_choice = input("What weapon would you like to use whip or gun? (W/G)\n")
            # if player chooses W or w deal damage to enemy with the whip
            if weapon_choice.lower() == 'w':
                # call the function from Enemy class that allows the enemy to be damaged, do damage with whip
                Enemy.damaged(enemy_type, Mc, "whip")
                # check if the enemy is still alive
                if enemy_type.life > 0:
                    # allow the enemy to attack the player if it is alive
                    Enemy.attack(enemy_type, Mc)
                    if Mc.life > 0:
                        continue
                    else:
                        player_died()
                        print("GAME OVER! You were defeated by the enemy")
                        battle_finished = True
                # if enemy is dead conclude the battle
                else:
                    # complete the battle if enemy is dead
                    battle_finished = True
                    print("Congratulation! You killed the enemy. You received", enemy_type.cash, "cash.")
                    # show the player their new balance after defeating the enemy
                    print("Your new balance is:", Mc.money)
            # if player chooses G or g deal damage to enemy with the gun, display bullet amount before and after
            if weapon_choice.lower() == 'g':
                # call the function from Enemy class that allows the enemy to be damaged, do damage with whip
                Enemy.damaged(enemy_type, Mc, "gun")
                # check if the enemy is still alive
                if enemy_type.life > 0:
                    # allow the enemy to attack the player if it is alive
                    Enemy.attack(enemy_type, Mc)
                    if Mc.life > 0:
                        continue
                    else:
                        player_died()
                        print("GAME OVER! You were defeated by the enemy")
                        battle_finished = True
                # if enemy is dead conclude the battle
                else:
                    # complete the battle if enemy is dead
                    battle_finished = True
                    print("Congratulation! You killed the enemy. You received", enemy_type.cash, "cash.")
                    # show the player their new balance after defeating the enemy
                    print("Your new balance is:", Mc.money)

        # if the player chooses R or r allow them to run from the fight
        elif fight_run.lower() == 'r':
            Enemy.player_ran(enemy_type, Mc)
            break

        # account for users incorrect input
        else:
            print("Invalid Input. Please choose a letter from the choices")
    battle_finished = False


# village return to village elder to receive medallion
def return_elder():
    print(Mc.name, ''': "I made it back to the village I should go talk to the elder."''')
    input("press 'enter' to continue\n")

    print(Mc.name, ''': "Hello elder I traveled through the temple but came across a locked door
                I brought back an imprint of what I think is the locking mechanism. 
                I believe that your medallion is a perfect match of the lock. 
                Can I borrow your medallion?"''')
    input("press 'enter' to continue\n")

    print('''Elder: "Yes son. You can take my medallion I hope it can help you out."''')
    input("press 'enter' to continue\n")

    # add the medallion to the players inventory
    Mc.inventory.append("medallion")
    while True:
        choice = input("""Do you want to do something else?
a. sleep
b. go to village store
c. exit\n""")

        if choice.lower() == "a":
            # call day night cycle
            day_night()

        elif choice.lower() == "b":
            # call village store function
            village_store()

        elif choice.lower() == "c":
            break

        else:
            print("Invalid Input. Please choose a letter from the choices")


# function to replace the tablet with an item the player has in their inventory
def replace_tablet():
    # add a quote from jones
    print(Mc.name,
          ''': "I could try replacing the tablet with something in my inventory."''')
    input("press 'enter' to continue\n")

    # give the player a choice
    choice = input("Should I use an item in my inventory or bullets? (I/B)")

    if choice.lower() == 'i':
        # print out the players inventory
        print("You currently have", Mc.inventory, "in your inventory.")
        input("press 'enter' to continue\n")

        inventory_choice = input("What item would you like to use to replace with the tablet?\n")

        if inventory_choice.lower() == 'vase':
            # player receives tablet and leaves vase
            print(Mc.name,
                  ''': "I should replace the tablet with the vase I collected earlier."''')
            # remove vase from inventory
            Mc.inventory.remove("vase")
            # tell the player the vase was removed
            print("'vase' was removed from inventory.")
            input("press 'enter' to continue\n")
            # add tablet to inventory
            Mc.inventory.append("tablet")
            print("'tablet' was added to inventory")
            input("press 'enter' to continue\n")

        else:
            print(
                """Jones decided to replace the artifact with an item he had stored. But because the weight of the items
did not match a trap was activated. The doors started to close and Jones tried running out but he couldn't make
it. When the doors closed the room started to fill with water. Jones tried to survive for as long as possible 
but inevitably died due to suffocation.\n""")
            player_died()

    elif choice.lower() == 'b':
        # show the user how many bullets they have
        print("You currently have", Mc.bullets, "bullets.")
        input("press 'enter' to continue\n")

        bullet_choice = int(input("How many bullets would you like to use?\n"))

        if bullet_choice == 16:
            if Mc.bullets >= 16:
                # Jones quote
                print(Mc.name,
                      ''': "I have a lot of bullets I could try matching the weight of the tablet."''')
                input("press 'enter' to continue\n")

                # remove bullets from inventory
                Mc.bullets -= 16
                # tell the player the bullets were removed
                print("16 bullets were removed from inventory.")
                input("press 'enter' to continue\n")
                # add tablet to inventory
                Mc.inventory.append("tablet")
                print("'tablet' was added to inventory")
                input("press 'enter' to continue\n")

            else:
                print(
                    """Jones decided to replace the artifact with an item he had stored. But because the weight of the items
did not match a trap was activated. The doors started to close and Jones tried running out but he couldn't make
it. When the doors closed the room started to fill with water. Jones tried to survive for as long as possible 
but inevitably died due to suffocation.\nn""")
                player_died()

        else:
            print(
                """Jones decided to replace the artifact with an item he had stored. But because the weight of the items
did not match a trap was activated. The doors started to close and Jones tried running out but he couldn't make
it. When the doors closed the room started to fill with water. Jones tried to survive for as long as possible 
but inevitably died due to suffocation.\n""")
            player_died()
