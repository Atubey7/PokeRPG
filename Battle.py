import random
from Trainer import Trainer

def check_faint(trainer):
    # To be Coded
    pass

def calculate_damage(attacker, defender, move):
    damage = ((2 * attacker.level/5)+2)*attacker.move.power*(attacker.Stats["ATK"]/defender.Stats["DEF"]) * modifiers
    # Finish the code for the modifiers
def run_battle(player, opponent):
    while True:
        player_gimmick = ???
        player_move = player.get_active().moves[???]
        opponent_move = opponent.get_active().moves[???]
        opponent_gimmick = ???
        equal = False
        if player.get_active().SPEED == opponent.get_active().SPEED:
            equal = True
            num = random.randint(1,2)
        if player.get_active().SPEED > opponent.get_active().SPEED or (equal and num == 1):
            player_damage =
            opponent.get_active().health -= player_damage
            if opponent.get_active().health > 0:
                opponent_damage =
        elif player.get_active().SPEED < opponent.get_active().SPEED or (equal and num == 2):
            opponent_damage =
            player.get_active().health -= opponent_damage
            if player.get_active().health > 0:
                player_damage =
                opponent.get_active().health -= player_damage

