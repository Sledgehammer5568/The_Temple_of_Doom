# main_character_name.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: file containing the main character starting stats and inventory as well as the enemies

import random


class MainCharacter:
    name = "Indiana Jones"
    life = 100
    money = 100
    whip_attk = 25
    gun_attk = 100
    bullets = 6
    inventory = []


class Enemy:
    def __init__(self, life, attk_dmg, cash):
        self.life = life
        self.attk_dmg = attk_dmg
        self.cash = cash

    # function to allow the enemy_type to do damage to the player
    def attack(self, main_character_name):
        main_character_name.life -= self.attk_dmg
        print("You were dealt", self.attk_dmg, "damage.")
        print("Your health is now:", main_character_name.life)

    # function for the player running away
    def player_ran(self, main_character_name):
        # declare a random amount of damage to deal to the player
        damage = random.randint(1, self.attk_dmg)
        # dialog explaining that the player ran
        print("You decided to run away from the enemy.")
        # do damage to the player
        main_character_name.life -= damage
        # tell the player they received damage
        print("While running away the enemy hit you for", damage, "damage.")
        # show the player their new health after damage
        print("You currently have", main_character_name.life, "health points.")

    # function to give the player the money an enemy_type drops when killed
    def loot(self, main_character_name):
        main_character_name.money += self.cash

    # function that will allow the enemy_type to take damage according to the weapon used by the player
    def damaged(self, main_character_name, damage_type):
        if damage_type == "gun":
            # check if player has bullets to shoot with
            if MainCharacter.bullets > 0:
                # deal damage to enemy
                self.life -= main_character_name.gun_attk
                # remove a bullet from the players inventory
                main_character_name.bullets -= 1
                # show player the damage they dealt
                print("You did 100 damage to the enemy.")
                print("The enemies health is now:", self.life)
                # if enemy is defeated give the player money
                if self.life <= 0:
                    self.loot(main_character_name)
                    return
            # if player doesn't have bullets they cannot attack with gun
            else:
                print("You currently have no bullets. You wasted a turn.")
                print("The enemies health is now:", self.life)
        elif damage_type == "whip":
            # deal damage to enemy
            self.life -= main_character_name.whip_attk
            # show player the damage they dealt
            print("You did 25 damage to the enemy.")
            print("The enemies health is now:", self.life)
            # if enemy is defeated give the player money
            if self.life <= 0:
                self.loot(main_character_name)
                return


# declaring an easy enemy_type with 100 life, 10 attk_dmg, and a random amount of cash
easy = Enemy(100, 10, random.randrange(25, 101, 25))

# declaring a medium enemy_type with 200 life, 15 attk_dmg, and a random amount of cash
medium = Enemy(200, 15, random.randrange(25, 101, 25))

# declaring an easy enemy_type with 400 life, 25 attk_dmg, and a random amount of cash
hard = Enemy(400, 25, random.randrange(25, 101, 25))
