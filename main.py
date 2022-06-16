from colorama import Fore
import requests
from os import system

def mainmenu():
system(f'title [FLURO0009] MultiTool ^|')
print(f'''{Fore.LIGHTMAGENTA_EX}
  _   _ _ _             _____          _                               
 | \ | (_) |           |  __ \        | |                              
 |  \| |_| |_ _ __ ___ | |__) |___  __| | ___  ___ _ __ ___   ___ _ __ 
 | . ` | | __| '__/ _ \|  _  // _ \/ _` |/ _ \/ _ \ '_ ` _ \ / _ \ '__|
 | |\  | | |_| | | (_) | | \ \  __/ (_| |  __/  __/ | | | | |  __/ |   
 |_| \_|_|\__|_|  \___/|_|  \_\___|\__,_|\___|\___|_| |_| |_|\___|_|   
                                                                       
                                                                       {Fore.LIGHTBLACK_EX}
      Multi TOOL for Nitro :){Fore.LIGHTMAGENTA_EX}
╔═════════════════════════════════════════════╗
║                                             ║
║        [1] Nitro Auto Redeemer [1]          ║
║        [2] Nitro Checker VALID/INVALID      ║
║        [3] Nitro CC Checker                 ║  # options
║                                             ║
╚═════════════════════════════════════════════╝
  ''' + Fore.RESET)
  choice = input(f'{Fore.LIGHTMAGENTA_EX}[>] ')
  if choice == '1':
    system('cls')
    startClaimer()
    Init()
  elif choice == '2':
    system('cls')
    startChecker()
  elif choice == '3':
    system('cls')
    startccChecker()
    else:
      mainmenu()
    
