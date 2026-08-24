import random
from Trainer import Trainer

def check_faint(trainer):
    # To be Coded
    pass

def calculate_damage(attacker, defender, move):
    # Pick correct attack and defense stats
    if move.category == "Physical":
        attack = attacker.ATK
        defense = defender.DEF
    elif move.category == "Special":
        attack = attacker.SPATK
        defense = defender.SPDEF

    # Base damage formula
    base = ((2 * attacker.level / 5) + 2) * move.power * (attack / defense) / 50 + 2

    # STAB - same type attack bonus
    if move.type in attacker.TYPE:
        stab = 1.5
    else:
        stab = 1.0
    #Tera STAB TBC
    if stab == 1.5:
        pass

    variance = random.uniform(0.85, 1.0)

    damage = round(base * stab * variance)
    return damage
def run_battle(player, opponent):
    while True:
        player_gimmick = ???
        player_move = player.get_active().moves[???]
        opponent_move = opponent.get_active().moves[???]
        opponent_gimmick = ???
        equal = False
        if player.get_active().SPEED == opponent.get_active().SPEED and player.getactive().PRIORITY == opponent.get_active().PRIORITY:
            equal = True
            num = random.randint(1,2)
        if (player.get_active().SPEED > opponent.get_active().SPEED and player.get_active.PRIORITY >= opponent.get_active.PRIORITY) or (equal and num == 1) or player.getactive().PRIORITY > opponent.get_active().PRIORITY:
            player_damage =
            opponent.get_active().health -= player_damage
            if opponent.get_active().health > 0:
                opponent_damage =
        elif player.get_active().SPEED < opponent.get_active().SPEED and player.get_active.PRIORITY >= opponent.get_active.PRIORITY) or (equal and num == 2):
            opponent_damage =
            player.get_active().health -= opponent_damage
            if player.get_active().health > 0:
                player_damage =
                opponent.get_active().health -= player_damage

