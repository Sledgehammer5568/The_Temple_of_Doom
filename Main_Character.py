# Main_game.py
#
# Emanuel Ramos
# 11/04/2022
#
# Description: file containing the main character starting stats and


class MainCharacter:
    name = "Indiana Jones"
    life = 100
    money = 100
    whip_attk = 25
    gun_attk = 100
    weapon_list = [whip_attk, gun_attk]
    bullets = 6
    inventory = ["torch"]


class DayNight:
    day = True
    night = False


class EasyEnemy:
    life = 100
    attk_dmg = 10
    cash = [25]


class MediumEnemy:
    life = 200
    attk_dmg = 15
    cash = [50]


class HardEnemy:
    life = 400
    attk_dmg = 25
    cash = [100]
