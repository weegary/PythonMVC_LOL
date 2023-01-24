# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:01:43 2023

@author: Gary Wee
"""

class Controller:
    def __init__(self,hero,view):
        self.hero = hero
        self.view = view
        
    def Attack(self, hero, enemy):
        self.hero.Attack(enemy)
        if (hero == self.view.left_hero):
            self.view.right_hero_hp.set(enemy.properties.HP)
        elif (hero == self.view.right_hero):
            self.view.left_hero_hp.set(enemy.properties.HP)    
