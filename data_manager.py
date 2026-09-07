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

def load_pokemon_moves(pokemon_list, move_list, filename):
    # Build lookup dicts for speed
    move_by_id = {m.id: m for m in move_list}  # need to add ID to Move
    move_by_name = {m.name: m for m in move_list}
    pokemon_by_dex = {p.dex: p for p in pokemon_list}

    df = pd.read_csv(filename)
    for _, row in df.iterrows():
        dex = int(row["DexID"])
        pokemon = pokemon_by_dex.get(dex)
        if not pokemon:
            continue
        # Assign 4 normal moves
        for col in ["MoveID1", "MoveID2", "MoveID3", "MoveID4"]:
            move_id = int(row[col])
            move = move_by_id.get(move_id)
            if move:
                pokemon.moves.append(move)
        # Assign Z-move
        if row["ZMove"] != "None":
            zmove = move_by_name.get(row["ZMove"])
            if zmove:
                pokemon.z_move = zmove
        # Assign GMax move
        if row["GMaxMove"] != "None":
            gmove = move_by_name.get(row["GMaxMove"])
            if gmove:
                pokemon.gmax_move = gmove

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