# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:27:02 2023

@author: Gary Wee
"""

import tkinter as tk
from tkinter import ttk
from tkinter import *

class View(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.label = ttk.Label(self, text="LOL Game")
        self.label.grid(row=0,column=0)
        self.label2 = ttk.Label(self, text="")
        self.label2.grid(row=1,column=0)
        self.pk_zone = PanedWindow()
        self.pk_zone.pack(fill=BOTH)
        self.controller = None
    
    def Panel(self,hero,var,isLeft = True):
        panel = PanedWindow(orient='vertical')
        name = ttk.Label(panel,text=hero.name)
        name.grid(row=0,column=0)
        hp = ttk.Label(panel,textvariable=var)
        hp.grid(row=1,column=0)
        mp = ttk.Label(panel,text=hero.properties.MP)
        mp.grid(row=2, column=0)
        ad = ttk.Label(panel,text=hero.properties.AD)
        ad.grid(row=3, column=0)
        
        if (isLeft):
            btn_attack = ttk.Button(panel,text="Attack", command=self.left_attack_button_clicked)
        else:
            btn_attack = ttk.Button(panel,text="Attack", command=self.right_attack_button_clicked)
        btn_attack.grid(row=4,column=0)
        return panel
    
    def left(self,hero):
        self.left_hero = hero
        self.left_hero_hp = StringVar()
        self.left_hero_hp.set(hero.properties.HP)
        panel = self.Panel(hero,self.left_hero_hp)
        self.pk_zone.add(panel)
    
    def right(self,hero):
        self.right_hero = hero
        self.right_hero_hp = StringVar()
        self.right_hero_hp.set(hero.properties.HP)
        panel = self.Panel(hero, self.right_hero_hp, False)
        self.pk_zone.add(panel)

    def mid(self):
        panel = self.MidPanel()
        self.pk_zone.add(panel)

    def left_attack_button_clicked(self):
        if self.controller:
            self.controller.Attack(self.left_hero, self.right_hero)
    
    def right_attack_button_clicked(self):
        if self.controller:
            self.controller.Attack(self.right_hero, self.left_hero)
    
    def MidPanel(self):
        panel = PanedWindow(orient='vertical')
        name = ttk.Label(panel,text="Hero")
        name.grid(row=0,column=0)
        hp = ttk.Label(panel,text="HP")
        hp.grid(row=1,column=0)
        mp = ttk.Label(panel,text="MP")
        mp.grid(row=2, column=0)
        ad = ttk.Label(panel,text="AD")
        ad.grid(row=3, column=0)
        return panel
    
    def set_controller(self,controller):
        self.controller = controller
