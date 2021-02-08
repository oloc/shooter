#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import image
from pygame.sprite import Sprite


class Monster(Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
