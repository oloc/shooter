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

    # Vérification si le jeu a commencé
    if game.is_playing:
        game.update(screen)

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
            # Détection de la barre espace
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
