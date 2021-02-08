#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.sprite import Group, Sprite, collide_mask, spritecollide

from monster import Monster
from player import Player


class Game:

    def __init__(self):
        self.player = Player(self)
        self.all_players = Group()
        self.all_players.add(self.player)
        self.all_monsters = Group()
        self.pressed = dict()

        self.spawn_monster()

    def check_collision(self, sprite: Sprite, group: Group):
        return spritecollide(sprite, group, False, collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
