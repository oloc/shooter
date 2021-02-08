#!/usr/bin/env python
# -*- coding: utf-8 -*-

from player import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = dict()
