from Battle import run_battle
from data_manager import load_pokemon
from Trainer import Trainer
from data_manager import load_moves
from Pokemon import Move
pokemon_list = load_pokemon("Pokemon Stats Dex.csv")
move_list = load_moves("Moves.csv")

import pygame
import sys
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PokeRPG')

clock = pygame.time.Clock()

running = False


greninja = pokemon_list[2]
test_move = Move("Water Shuriken", "Water", "Physical", 15, 100, 20, 1, 0)
greninja.moves.append(test_move)

# Give Charizard a test move
charizard = pokemon_list[5]
fire_move = Move("Flamethrower", "Fire", "Special", 90, 100, 15, 0, 0)
charizard.moves.append(fire_move)

player = Trainer("Ayaan", [greninja], 0, False)
opponent = Trainer("AI", [charizard], 0, False)

run_battle(player, opponent)

while running:
    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Game Logic



    #Rendering



    clock.tick(60)

pygame.quit()
sys.exit()