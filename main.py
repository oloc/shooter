#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from game import Game

pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode(size=(1080, 720))

background = pygame.image.load('assets/bg.jpg')
game = Game()
game_is_running = True

# Boucle tant que le jeu est en cours
while game_is_running:

    # Application de l'arrière plan sur la surface
    screen.blit(background, (0, -200))
    # Application du joueur sur la surface
    screen.blit(game.player.image, game.player.rect)

    # Déplacement du joueur
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    # mise à jour de l'écran
    pygame.display.flip()

    # Boucle sur les événements
    for event in pygame.event.get():
        # événement de fermeture de fenêtre
        if event.type == pygame.QUIT:
            game_is_running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
