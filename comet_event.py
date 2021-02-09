#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import draw
from pygame.surface import Surface


class CometFallEvent:

    def __init__(self) -> None:
        self.percent = int()

    def add_percent(self, amount: int = 1) -> None:
        self.percent += amount

    def update_bar(self, surface: Surface) -> None:
        draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        draw.rect(surface, (187, 11, 11), [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])
