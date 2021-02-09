#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import draw
from pygame.surface import Surface

from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def launch_projectile(self) -> None:
        # Instanciation du projectile dans le groupe
        self.all_projectiles.add(Projectile(self))

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def update_health_bar(self, surface: Surface):
        draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])
