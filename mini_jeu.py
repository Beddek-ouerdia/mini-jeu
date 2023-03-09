
#PLS (python Standard Library)

import math
import platform
import random
import os 
import sys

#classe import

class AdventureGame_:
  """
  personnage qui est dans un desert et qui souhaite trouver 5 tresors legendaires , mais qui  doit combattre 10 monstre et sauver 5 amis

  -lieu:desert
  -animaux:
  -personnage
  -5 amis
  -10 monstre
  -5 tresors
  """
# attribut de la classe
game_name="Legendary Desert"
game_player_number=1
game_over=False


#constructor
def __init__(self):
      
      #customkinter window initialization
      Super().__init__()
      self.geometry("120.900")
      self.title(f"(self.game_name)")
      
      # function to use
      self.AdventureGame_Startup()
      self.AdventureGame_clean()
      

  

def AdventureGame_Startup(self):
    print(" chargement du jeux en cours")



def AdventureGame_Main (self):
    pass

def AdventureGame_NewGame(self):
    print("welcome to the mew adventure")
    print("would you like to walk?")
    user_choice=input()
    player_character=Game_Character()

    

def AdventureGame_LoadGame(self):
    pass

def AdventureGame_Quit(self):
    pass
Appli=AdventureGame
