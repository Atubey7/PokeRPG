class Trainer:
    def __init__(self, name, pokemon_team, active_pokemon, gimmick_used):
        self.name = name
        self.pokemon_team = pokemon_team
        self.active_pokemon = 0
        self.gimmick_used = False
    def getactive(self):
        return self.pokemon_team[self.active_pokemon]
    def next_healthy(self):
        for i, pokemon in enumerate(self.pokemon_team):
            if pokemon.Health > 0:
                self.active_pokemon = i
                return True
        return False
    def switch_pokemon(self, index):
        if self.pokemon_team[index].health != 0:
            self.active_pokemon = index
        else:
            next_healthy()
