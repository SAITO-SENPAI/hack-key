import pyfiglet 
import time
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()



time.sleep(1)
os.system('clear')
banner = pyfiglet.figlet_format("SAITO SENPAI", font = "slant"  ) 
print(Fore.RED)
print(banner) 



print("==================================================================================")
print("")
print(Fore.YELLOW)
print("Author : SAITO SENPAI")
print("Github : https://github.com/SAITO-SENPAI")




while True:
	key = input(Fore.RED + 'Your Key: ')
	if key == "Z139":
		print("Successful Login")
		break
	else:
		print("The Key You Used Expired Or Wrong!")

