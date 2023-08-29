#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == "__main__":
    g1 = Game("Stardew")
    g2 = Game("Animal Crossing")
    g3 = Game("Halo")
    g4 = Game("Tears of the Kingdom")

    p1 = Player("ravishingriley")
    p2 = Player("braillejord")
    p3 = Player("franknbeans")
    p4 = Player("puffpuffpass")

    r1 = Result(p1, g3, 5)
    r2 = Result(p2, g1, 9)
    r3 = Result(p3, g2, 7)
    r4 = Result(p4, g4, 10)
    r5 = Result(p1, g1, 8)
    r6 = Result(p3, g3, 2)
    r7 = Result(p3, g3, 4)
    r8 = Result(p3, g3, 8)

    ipdb.set_trace()
