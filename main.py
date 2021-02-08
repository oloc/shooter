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

    # Application de la barre de vie du joueur
    game.player.update_health_bar(screen)

    # Déplacement des projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()
    # Déplacement des montres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Application des projectiles sur la surface
    game.player.all_projectiles.draw(screen)
    # Application des monstres sur la surface
    game.all_monsters.draw(screen)

    # Déplacement du joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
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
            # Détection de la barre espace
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
