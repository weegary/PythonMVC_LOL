# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:53:22 2023

@author: Gary Wee
"""

import tkinter as tk
from tkinter import ttk

from Hero import *
from View import *
from Controller import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self_hero_properties = Hero.Properties(
                               {'HP':630,'HP_gen':5.5,'MP':340,'MP_gen':11,
                                'AD':56,'Armor':25,'Magic_resist':30,
                                'Move_speed':335, 'Attack_range':450}
                               ,True)
        self_hero = Hero('Morgana',self_hero_properties)
        enemy_hero_properties = Hero.Properties(
                                {'HP':620,'HP_gen':4,'MP':280,'MP_gen':7.45,
                                 'AD':65,'Armor':33,'Magic_resist':32,
                                 'Move_speed':335, 'Attack_range':125}
                                  ,True)
        enemy_hero = Hero('Warwick',enemy_hero_properties)
        view = View(self)
        view.left(self_hero)
        view.mid()
        view.right(enemy_hero)
        # view.grid(row=0,column=0,padx=10,pady=10)
        controller = Controller(self_hero,view)
        view.set_controller(controller)

if (__name__) == '__main__':
    app = App()
    app.mainloop()
