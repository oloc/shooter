#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.rect = self.image.get_rect()
