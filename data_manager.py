import pandas as pd
import json
from Pokemon import Pokemon

filename = "/Users/ayaanbeig/PycharmProjects/PokeRPG/Pokemon Stats Dex.csv"
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

        initial_types = [row["P-Type"], row["S-Type"]]

        pokemon_obj = Pokemon(
            dex=int(row["DexID"]),
            name=row["Name"],
            Stats=stats_dict,
            P_TYPE=row["P-Type"],
            S_TYPE=row["S-Type"],
            Tera_Type=row["Tera"],
            Forms=forms_data,
        )

        pokemon_list.append(pokemon_obj)
    return pokemon_list