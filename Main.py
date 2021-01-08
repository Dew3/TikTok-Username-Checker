#####################################################################
#                                                                   #
#  Dew3's TikTok Username Checker                                   # 
#  v0.1                                                             #
#  Utilizes TikTokApi by David Teather to get user information      #
#  Open README.txt before running the program                       #
#                                                                   #
#####################################################################

from TikTokApi import TikTokApi
import asyncio
import pandas
import requests
import string
import pathlib
import colorama
import os, sys
import time
from urllib.request import urlopen as uReq
from pathlib import Path
from colorama import *


api = TikTokApi()
current_path = os.path.dirname(os.path.realpath(__file__))
open(current_path +"/"+str("Available")+str("")+".txt","a") #Creates 'Available.txt'
open(current_path +"/"+str("Usernames")+str("")+".txt","a") #Creates 'Usernames.txt'
names = open('Usernames.txt', 'r') 
available = open('Available.txt', 'w') 
mypath = Path('Usernames.txt')
numberOfUsernames = 0


def check():
    print(Fore.LIGHTBLACK_EX+"["+Fore.CYAN+"+"+Fore.LIGHTBLACK_EX+"]"+"Dew3's TikTok Username Checker")

    if mypath.stat().st_size == 0: #If the Usernames files is empty it will prompt the user to enter usernames and close the program
        print(Fore.WHITE+"\nPlease put your names in Usernames.txt"+ Fore.RED + "\nClosing in 5 seconds")
        time.sleep(5)
        sys.exit()
    else:  
            pass
    with open('Usernames.txt', 'r') as u: 
            
            for line in u:
                username = line.rstrip("\n") #Gets each usernames line in 'Usernames.txt'
                if len(username) < 25:
                  global numberOfUsernames
                  numberOfUsernames += 1 #Counter for the total number of usernames

                  try: #Use a try block since there is a potential of an account not existing
                      

                      user = api.getUserObject(username) #TikTokApi returns a user as an object OR throws a TikTokNotFound exception (I forget the exact name of the exception but you get what I mean)

                      #If the previous line doesn't throw an exception we know the username is taken
                      print(Fore.WHITE+"["+Style.BRIGHT + Fore.RED + Back.BLACK+"Taken"+Fore.WHITE+"]" +Fore.WHITE +username)

                  except: #Catches the TikTokNotFound exception. Therefore the username isn't taken.

                      available.write(username + "\n") #The username isn't taken so we store it into 'Availables.txt'
                      print(Fore.WHITE+"["+Style.BRIGHT + Fore.GREEN + Back.BLACK+"Not Taken"+Fore.WHITE+"]" +Fore.WHITE +username)
              
tic = time.perf_counter() #Program timer start
check()
toc = time.perf_counter() #Program timer stop
available.close()         
print(Fore.CYAN+"\nChecker finished " + str(numberOfUsernames) + f" usernames in {toc - tic:0.4f} seconds")
print("Available usernames saved!")
print(Fore.RED +"Closing in 5 seconds")
time.sleep(5)
sys.exit()

