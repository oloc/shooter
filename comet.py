#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

from pygame import image, sprite


class Comet(sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = randint(1, 3)

    def fall(self):
        self.rect.y += self.velocity
