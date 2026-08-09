from data_manager import load_pokemon
pokemon_list = load_pokemon("/Users/ayaanbeig/PycharmProjects/PokeRPG/Pokemon Stats Dex.csv")
print(pokemon_list[0].name)

import pygame
import sys
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PokeRPG')

clock = pygame.time.Clock()

running = False

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