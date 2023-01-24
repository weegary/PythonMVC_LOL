# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:06:31 2023

@author: Gary Wee
"""

class Hero:
    
    def __init__(self,name, properties):
        self.HERO = self.hero(name,properties)
    
    def hero(self,name, properties):
        self.__name = name
        self.name = name
        self.properties = self.Properties(properties)
    
    #%%
    class Properties:
        
        def __init__(self, properties, from_dict = False):
            if (not from_dict):
                self.HP = properties.HP
                self.HP_gen = properties.HP_gen
                self.MP = properties.MP
                self.MP_gen = properties.MP_gen
                self.AD = properties.AD
                self.Armor = properties.Armor
                self.Magic_resist = properties.Magic_resist
                self.Move_speed = properties.Move_speed
                self.Attack_range = properties.Attack_range
            else:
                self.HP = properties['HP']
                self.HP_gen = properties['HP_gen']
                self.MP = properties['MP']
                self.MP_gen = properties['MP_gen']
                self.AD = properties['AD']
                self.Armor = properties['Armor']
                self.Magic_resist = properties['Magic_resist']
                self.Move_speed = properties['Move_speed']
                self.Attack_range = properties['Attack_range']
                                     
            
    #%%       
    def Attack(self,enemy):
        enemy.properties.HP = enemy.properties.HP + enemy.properties.Armor - self.properties.AD
        if (enemy.properties.HP < 0):
            enemy.properties.HP = 0
        print(enemy.name, "HP:" , enemy.properties.HP)
