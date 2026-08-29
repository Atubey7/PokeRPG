import random
from Trainer import Trainer
from data_manager import pokemon_type_effectiveness

def check_faint(trainer):
    if trainer.get_active().Health <= 0:
        trainer.get_active().Health = 0
        result = trainer.next_healthy()
        if not result:
            return "battle_over"
    return "continue"

def gimmick_choice(trainer):
    pass
def battle_text(attacker, attacker_move, defender):
    effectiveness = pokemon_type_effectiveness(attacker_move, defender.get_active())
    text = ""
    if effectiveness == 2.0:
        text = "\nIt was Super Effective"
    elif effectiveness == 4.0:
        text = "\nIt was Extremely Effective"
    elif effectiveness == 0.0:
        text = "\nIt had No Effect"
    elif effectiveness == 0.5:
        text = "\nIt was Not Very Effective"
    print(f"{attacker.get_active().name} used {attacker_move.name}{text}")
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

    #Type Effectiveness
    type = pokemon_type_effectiveness(move, defender)

    variance = random.uniform(0.85, 1.0)

    #Crit Chance
    modifiers = 0
    crit_stage = move.crit + modifiers
    if crit_stage == 0.0:
        chance = 24
    elif crit_stage == 1.0:
        chance = 8
    elif crit_stage == 2.0:
        chance = 2
    elif crit_stage >= 3.0:
        chance = 1
    num = random.randint(1, chance)
    crit = 2 if num == 1 else 1

    damage = round(base * stab * variance * type * crit)
    return damage

def move_choice(trainer, opponent, attacker_gimmick):
    if trainer.name == "AI":
        list = []
        for move in trainer.get_active().moves:
            dmg = calculate_damage(trainer.get_active(), opponent.get_active(), move, attacker_gimmick)
            list.append((dmg, move))
        best_move = max(list, key=lambda x: x[0])
        return best_move[1]
    else:
        return trainer.get_active().moves[0]


def run_battle(player, opponent):
    while True:
        player_gimmick = gimmick_choice(player)
        player_move = move_choice(player, opponent, player_gimmick)
        opponent_gimmick = gimmick_choice(opponent)
        opponent_move = move_choice(opponent, player, opponent_gimmick)
        equal = False
        if player.get_active().SPEED == opponent.get_active().SPEED and player_move.priority == opponent_move.priority:
            equal = True
            num = random.randint(1,2)
        if (player.get_active().SPEED > opponent.get_active().SPEED and player_move.priority >= opponent_move.priority) or (equal and num == 1) or player.get_active().priority > opponent.get_active().priority:
            player_damage = calculate_damage(player.get_active(), opponent.get_active(), player_move, player_gimmick)
            opponent.get_active().Health -= player_damage
            battle_text(player, player_move, opponent)
            print(f"It dealt: {player_damage}")
            if check_faint(opponent) != "battle_over":
                opponent_damage = calculate_damage(opponent.get_active(), player.get_active(), opponent_move, opponent_gimmick)
                player.get_active().Health -= opponent_damage
                battle_text(opponent, opponent_move, player)
                print(f"It dealt: {opponent_damage}")
        elif (player.get_active().SPEED < opponent.get_active().SPEED and player_move.priority >= opponent_move.priority) or (equal and num == 2):
            opponent_damage = calculate_damage(opponent.get_active(), player.get_active(), opponent_move, opponent_gimmick)
            player.get_active().Health -= opponent_damage
            battle_text(opponent, opponent_move, player)
            print(f"It dealt: {opponent_damage}")
            if check_faint(player) != "battle_over":
                player_damage = calculate_damage(player.get_active(), opponent.get_active(), player_move, player_gimmick)
                opponent.get_active().Health -= player_damage
                battle_text(player, player_move, opponent)
                print(f"It dealt: {player_damage}")
        if check_faint(opponent) == "battle_over":
            print(f"{opponent.get_active().name} fainted\n{player.name} wins!")
            break
        if check_faint(player) == "battle_over":
            print(f"{player.get_active().name} fainted\n{opponent.name} wins!")
            break

