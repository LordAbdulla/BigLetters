import os
from os import system
try:
  from pyfiglet import *
except:
  os.system('pip install pyfiglet')
print('''
    ____  _          __         __  __                
   / __ )(_)___ _   / /   ___  / /_/ /____  __________
  / __  / / __ `/  / /   / _ \/ __/ __/ _ \/ ___/ ___/
 / /_/ / / /_/ /  / /___/  __/ /_/ /_/  __/ /  (__  ) 
/_____/_/\__, /  /_____/\___/\__/\__/\___/_/  /____/  
        /____/                                        

        Tele : @DewTools | @LordAbdulla 
                                            ''')
dewx = input(" Enter The Text To Convert It : ")

dady = figlet_format(dewx, 'slant')
print(dady)


#Telegram : @DewTools
#Inst : @hr8k
#Github : github.com/LordAbdulla
