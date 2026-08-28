import random
from Trainer import Trainer

def check_faint(trainer):
    if trainer.get_active().Health <= 0:
        trainer.get_active().Health = 0
        result = trainer.next_healthy()
        if not result:
            return "battle_over"
    return "continue"

def gimmick_choice(trainer):
    pass
def move_choice(trainer):
    return trainer.get_active().moves[0]

def calculate_damage(attacker, defender, move, attacker_gimmick):
    # Pick correct attack and defense stats
    if move.category == "Physical":
        attack = attacker.ATK
        defense = defender.DEF
    elif move.category == "Special":
        attack = attacker.SPATK
        defense = defender.SPDEF

    # Base damage formula
    base = ((2 * attacker.Level / 5) + 2) * move.power * (attack / defense) / 50 + 2

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
        player_gimmick = gimmick_choice(player)
        player_move = move_choice(player)
        opponent_gimmick = gimmick_choice(opponent)
        opponent_move = move_choice(opponent)
        equal = False
        if player.get_active().SPEED == opponent.get_active().SPEED and player_move.priority == opponent_move.priority:
            equal = True
            num = random.randint(1,2)
        if (player.get_active().SPEED > opponent.get_active().SPEED and player_move.priority >= opponent_move.priority) or (equal and num == 1) or player.getactive().priority > opponent.get_active().priority:
            player_damage = calculate_damage(player.get_active(), opponent.get_active(), player_move, player_gimmick)
            opponent.get_active().Health -= player_damage
            if check_faint(opponent) != "battle_over":
                opponent_damage = calculate_damage(opponent.get_active(), player.get_active(), opponent_move, opponent_gimmick)
        elif (player.get_active().SPEED < opponent.get_active().SPEED and player_move.priority >= opponent_move.priority) or (equal and num == 2):
            opponent_damage = calculate_damage(opponent.get_active(), player.get_active(), opponent_move, opponent_gimmick)
            player.get_active().Health -= opponent_damage
            if check_faint(player) != "battle_over":
                player_damage = calculate_damage(player.get_active(), opponent.get_active(), player_move, player_gimmick)
                opponent.get_active().Health -= player_damage
        if check_faint(opponent) == "battle_over":
            print(f"{player.name} wins!")
            break

