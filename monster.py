#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw, image
from pygame.sprite import Sprite
from pygame.surface import Surface


class Monster(Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 5

    def update_health_bar(self, surface: Surface):
        back_bar_color = (60, 63, 60)
        bar_color = (111, 210, 46)
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        draw.rect(surface, back_bar_color, back_bar_position)
        draw.rect(surface, bar_color, bar_position)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

    def recycle(self):
        self.rect.x = 1000
        self.health = self.max_health
