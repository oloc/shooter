#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("Comet Fall Game")
pygame.display.set_mode(size=(500, 300))

game_is_running = True

# Boucle tant que le jeu est en cours
while game_is_running:

    # Boucle sur les événements
    for event in pygame.event.get():
        # événement de fermeture de fenêtre
        if event.type == pygame.QUIT:
            game_is_running = False
            pygame.quit()
