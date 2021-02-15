#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import K_LEFT, K_RIGHT
from pygame.sprite import Group, Sprite, spritecollide

from typing import List

from comet_event import CometFallEvent
from monster import Monster
from player import Player


class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.all_players = Group()
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent()
        self.all_monsters = Group()
        self.pressed = dict()

    def check_collision(self, sprite: Sprite, group: Group) -> List[Sprite]:
        return spritecollide(sprite, group, False)

    def game_over(self) -> None:
        self.all_monsters = Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def spawn_monster(self) -> None:
        monster = Monster(self)
        self.all_monsters.add(monster)

    def start(self) -> None:
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def update(self, screen) -> None:
        # Application du joueur sur la surface
        screen.blit(self.player.image, self.player.rect)

        # Application de la barre de vie du joueur
        self.player.update_health_bar(screen)

        self.comet_event.update_bar(screen)

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
        # Application des comètes sur la surface
        self.comet_event.all_comets.draw(screen)

        # Déplacement du joueur
        if self.pressed.get(K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
