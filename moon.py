# coding: utf-8

import sys, os
sys.path.insert(0, os.getcwd() + "/mapengine")

import mapengine
from mapengine import simpleloop, Scene, GameObject, Hero

class Armadilha(GameObject):
    def on_over(self, other):
        if not isinstance(other, Hero):
            return
        other.kill()
        
class Loser(GameObject):
    def on_over(self, other):
        if not isinstance(other, Hero):
            return
        other.kill()
        
class Agua(GameObject):
    def on_over(self, other):
        if not isinstance(other, Hero):
            return
        other.kill()
    
class Saida(GameObject):
    hardness = 10
    def on_touch(self, other):
        cena = Scene("faseagua")
        self.controller.load_scene(cena)
        self.controller.force_redraw = True
        
class Winner(GameObject):
    def on_touch(self, other):
        if not isinstance(other, Hero):
            return
        self.show_text(u"Parabéns, você ganhou!", duration=10)       

def main():
    cena = Scene("faseagua")
    simpleloop(cena, (800, 600))



main()

