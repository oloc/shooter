#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw
from pygame.surface import Surface


class CometFallEvent:

    def __init__(self) -> None:
        self.percent = int()
        self.percent_speed = 5

    def add_percent(self) -> None:
        self.percent += self.percent_speed / 100

    def update_bar(self, surface: Surface) -> None:
        self.add_percent()
        draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        draw.rect(surface, (187, 11, 11),
                  [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])
