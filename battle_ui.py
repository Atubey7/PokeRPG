import pygame
class BattleUI:
    def __init__(self, screen, player, opponent):
        self.screen = screen
        self.player = player
        self.opponent = opponent
        self.state = "menu"  # menu → move_select → gimmick → animating
        self.message = ""
        self.selected_move = None

        # Colours
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.DARK_BLUE = (40, 40, 80)
        self.HP_GREEN = (80, 200, 80)
        self.HP_YELLOW = (240, 200, 40)
        self.HP_RED = (220, 60, 60)
        self.GREY = (180, 180, 180)

        # Type colours for move buttons (Sword/Shield style)
        self.TYPE_COLOURS = {
            "Water": (80, 160, 220),
            "Fire": (240, 100, 50),
            "Grass": (80, 190, 80),
            "Electric": (240, 200, 40),
            "Fighting": (180, 60, 60),
            "Steel": (160, 170, 185),
            "Dragon": (80, 60, 200),
            "Ground": (200, 160, 80),
            "Flying": (160, 180, 220),
            "Ghost": (100, 80, 160),
            "Normal": (160, 160, 140),
            "Dark": (80, 60, 60),
            "Psychic": (240, 80, 140),
            "Fairy": (240, 160, 200),
            "Ice": (140, 210, 230),
            "Rock": (160, 140, 100),
        }

        # Fonts
        self.font_large = pygame.font.SysFont("monospace", 22, bold=True)
        self.font_med = pygame.font.SysFont("monospace", 18)
        self.font_small = pygame.font.SysFont("monospace", 14)
    def draw_hp_box(self, pokemon, is_player):
        bar_width = 80
        bar_length = 300
        bar_max_length = 220
        bar_area = bar_width * bar_length
        healthPercent = pokemon.Health / pokemon.HP
        bar = int(healthPercent*bar_max_length)
        if healthPercent >= 0.5:
            bar_colour = self.HP_GREEN
        elif healthPercent <= 0.25:
            bar_colour = self.HP_RED
        else:
            bar_colour = self.HP_YELLOW
        if is_player:
            x = 760
            y = 400
        else:
            x = 20
            y = 20
        pygame.draw.rect(self.screen, self.WHITE, (x, y, bar_length, bar_width))
        pygame.draw.rect(self.screen, self.BLACK , (x, y, bar_length, bar_width), 2)
        pygame.draw.rect(self.screen, bar_colour, (x+40, y+35, bar, 10))
        pokemon = self.font_med.render(pokemon.name, False, self.WHITE, background=None)
        if is_player:
            text_rect = pokemon.get_rect(center=(400, 300))
        else:
            text_rect = pokemon.get_rect(center=(400, 300))
        self.screen.blit(pokemon, text_rect)

    def draw_move_menu(self):
        pass
    def draw_text_box(self):
        pass
    def draw_gimmick_wheel(self):
        pass
    def draw(self):
        pass