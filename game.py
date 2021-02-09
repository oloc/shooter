#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import K_LEFT, K_RIGHT
from pygame.sprite import Group, Sprite, collide_mask, spritecollide

from monster import Monster
from player import Player


class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.all_players = Group()
        self.all_players.add(self.player)
        self.all_monsters = Group()
        self.pressed = dict()

        self.spawn_monster()
        self.spawn_monster()

    def check_collision(self, sprite: Sprite, group: Group):
        return spritecollide(sprite, group, False, collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def update(self, screen):
        # Application du joueur sur la surface
        screen.blit(self.player.image, self.player.rect)

        # Application de la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Déplacement des projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        # Déplacement des montres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # Application des projectiles sur la surface
        self.player.all_projectiles.draw(screen)
        # Application des monstres sur la surface
        self.all_monsters.draw(screen)

        # Déplacement du joueur
        if self.pressed.get(K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
