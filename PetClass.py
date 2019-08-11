#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:26:17 2019

@author: daizh
"""

class Pet:
    #Create two variables kind and color; assign values
    kind='animal'
    color='black'
    
    speak_script='{name} says {sound}'
    str_script='I am a {kind} named {name}'
    
    def __init__ (self,name):
        self.name=name
        
    def do_tricks(self):
        print('{name} is doing tricks'.format(name=self.name))
        
        self.speak()
        self.jump()
        
    def speak(self):
        pass
    def jump(self):
        pass
    
class Jumper:
    'This is a minxin class for jump'
    
    def jump(self):
        print('{name} is jumping'.format(name=self.name))

class Dog(Jumper,Pet):
    kind='canine'
    owner='Jenny'
    
    def __str__ (self):
        return('I am a {kind} named {name})'.format(name=self.name,kind=self.kind))
        
    def __call__(self,action):
        if action =='rollover':
            print('{name} is rolling over'.format(name=self.name))
        
        elif action =='owner':
            print('The owner is:'+self.owner)
        
class BigDog(Dog):
    color='tan'
    owner='Rachel'
    spoken_sound='WOOF!'
    
    def __str__ (self):
        return('I am a {kind} named {name}'.format(name=self.name,kind=self.kind))
        
    def speak(self):
        print(self.speak_script.format(name=self.name,sound=self.spoken_sound))
        
class SmallDog(Dog):
    spoken_sound='woof'
    owner='Alexander'
    color='brindle'
    
    def __str__ (self):
        return('I am a {kind} named {name})'.format(name=self.name,kind=self.kind))
        
    def speak(self):
        print(self.speak_script.format(name=self.name,sound=self.spoken_sound))
        
class Cat(Jumper,Pet):
    spoken_sound='Meow'
    def __str__ (self):
        return('I am a {kind} named {name})'.format(name=self.name,kind=self.kind))
        
    def speak(self):
        print(self.speak_script.format(name=self.name,sound=self.spoken_sound))
        
    def climb(self):
        print('{name} is climbing'.format(name=self.name))
        
class HouseCat(Cat):
    spoken_sound='meyow'
    color='white'
    
    def __str__ (self):
        return('I am a {kind} named {name})'.format(name=self.name,kind=self.kind))
        
    def speak(self):
        print(self.speak_script.format(name=self.name,sound=self.spoken_sound))
        
        
        
def main():
    pet=Pet('Animal')
    dog=Dog('Rocky')
    big_dog=BigDog('Clifford')
    small_dog=SmallDog('Spuds')
    cat=Cat('Heathcliff')
    house_cat=HouseCat('Garfield')
    
    pet=[pet,dog,big_dog,small_dog,cat,house_cat]
    
    for pet in pet:
        print(pet. __str__())
        print(pet.kind)
        print(pet.color)
        pet.do_tricks()
        if pet in [dog,big_dog,small_dog]: 
            pet('rollover')
            pet('owner')
            print('------------------------------')
        elif pet in [cat,house_cat]:
            pet.climb()
            print('------------------------------')
        else:
            print('------------------------------')    
main()
