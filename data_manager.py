import pandas as pd
import json
from Pokemon import Pokemon
from Pokemon import Move

file1 = "Pokemon Stats Dex.csv"
file2 = "Pokémon Type Chart.csv"
file3 = "Moves.csv"
def load_pokemon(filename):
    df = pd.read_csv(filename)
    pokemon_list = []
    for _, row in df.iterrows():
        stats_dict = {
            "HP": int(row["HP"]),
            "ATK": int(row["ATK"]),
            "DEF": int(row["DEF"]),
            "SPATK": int(row["SPATK"]),
            "SPDEF": int(row["SPDEF"]),
            "SPEED": int(row["SPEED"]),
        }
        forms_raw = row["Forms"]
        if pd.isna(forms_raw) or not forms_raw:
            forms_data = {}
        elif isinstance(forms_raw, dict):
            forms_data = forms_raw
        else:
            try:
                forms_data = json.loads(forms_raw)
            except json.JSONDecodeError:
                forms_data = {}

        s_type = None if row["S-Type"] == "None" else row["S-Type"]
        initial_types = [row["P-Type"], s_type]

        pokemon_obj = Pokemon(
            dex=int(row["DexID"]),
            name=str(row["Name"]),
            Stats=stats_dict,
            P_TYPE=str(row["P-Type"]),
            S_TYPE=str(row["S-Type"]),
            Tera_Type=str(row["Tera"]),
            Forms=forms_data,
        )

        pokemon_list.append(pokemon_obj)
    return pokemon_list
def load_moves(filename):
    df = pd.read_csv(filename)
    move_list = []
    for _, row in df.iterrows():
        move = Move(
            name=row["Name"],
            type=row["Type"],
            category=row["Category"],
            power=int(row["Power"]),
            accuracy=int(row["Accuracy"]),
            pp=int(row["PP"]),
            priority=int(row["Priority"]),
            crit=int(row["Crit"])
        )
        move.move_type = row["MoveType"]
        move_list.append(move)
    return move_list
def pokemon_type_effectiveness(attacker_move, defender):
    filename = "Pokemon Type Chart.csv"
    df = pd.read_csv(filename)
    list = []
    df.set_index(df.columns[0], inplace=True)
    for type in defender.TYPE:
        list.append(df.loc[attacker_move.type,type])
    if len(list) == 1:
        return list[0]
    else:
        return list[0] * list[1]