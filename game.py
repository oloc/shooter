#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.sprite import Group

from monster import Monster
from player import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.all_monsters = Group()
        self.pressed = dict()

        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)
