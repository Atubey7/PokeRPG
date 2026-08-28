class Trainer:
    def __init__(self, name, pokemon_team, active_pokemon, gimmick_used):
        self.name = name
        self.pokemon_team = pokemon_team
        self.active_pokemon = 0
        self.gimmick_used = False
    def get_active(self):
        return self.pokemon_team[self.active_pokemon]
    def next_healthy(self):
        for i, pokemon in enumerate(self.pokemon_team):
            if pokemon.Health > 0:
                self.active_pokemon = i
                return True
        return False
    def switch_pokemon(self, index):
        if self.pokemon_team[index].Health != 0:
            self.active_pokemon = index
        else:
            self.next_healthy()
    def get_gimmick(self):
        return self.pokemon_team[self.active_pokemon].current_form
    def set_gimmick(self, form):
        self.gimmick_used = True
        self.pokemon_team[self.active_pokemon].current_form = form
        self.pokemon_team[self.active_pokemon].activate_form(form)
