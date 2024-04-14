import os
import time
import Main
from colorama import init, Fore, Back, Style
import json

init()
def printRed(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.RED + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def ThemeMain(text):
    if Main.colors == True:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            color_index = config_data.get("mainindex")
        color = Main.colorlist[color_index % len(Main.colorlist)]
        crossed_text = Style.BRIGHT + color + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
    
def welcomemsg():
    if Main.wlcanimation == True:

        wlcmsg1 ="""
         __      _
         \ \    / /
          \ \/\/ /
           \_/\_/ 
        """
        wlcmsg2 ="""
         __      _____ 
         \ \    / / __|
          \ \/\/ /| _||
           \_/\_/ |___|
        """
        wlcmsg3 ="""
         __      _____ _   
         \ \    / / __| |  
          \ \/\/ /| _|| |_
           \_/\_/ |___|____
        """
        wlcmsg4 ="""
         __      _____ _    ___
         \ \    / / __| |  / __
          \ \/\/ /| _|| |_| (_
           \_/\_/ |___|____\___
        """
        wlcmsg5 ="""
         __      _____ _    ___ ___ 
         \ \    / / __| |  / __/ _ \\1
          \ \/\/ /| _|| |_| (_| (_) 
           \_/\_/ |___|____\___\___/
        """
        wlcmsg6 ="""
         __      _____ _    ___ ___  __  __ 
         \ \    / / __| |  / __/ _ \|  \/  |
          \ \/\/ /| _|| |_| (_| (_) | |\/| |
           \_/\_/ |___|____\___\___/|_|  |_|
        """
        wlcmsg7 ="""
         __      _____ _    ___ ___  __  __ ___ 
         \ \    / / __| |  / __/ _ \|  \/  | __|
          \ \/\/ /| _|| |_| (_| (_) | |\/| | _| 
           \_/\_/ |___|____\___\___/|_|  |_|___|
        """
        pewi1 ="""
             _   __ __  __ __ __
            | | / // / / // //_/
            | |/ // /_/ // ,<   
            |___/ \____//_/|_|  
                                        """
        pewi12 ="""
         _   __ __  __ __ __
        | | / // / / // //_/
        | |/ // /_/ // ,<   
        |___/ \____//_/|_|  
                                        """
        pewi2 =""" 
             _   __ __  __ __ __
            | | / // / / // //_/
            | |/ // /_/ // ,<   
            |___/ \____//_/|_|   
                                        """
        pewi3 =""" 
        | | / // / / // //_/
        | |/ // /_/ // ,<   
        |___/ \____//_/|_|    
                                        """
        pewi4 ="""    
        | |/ // /_/ // ,<   
        |___/ \____//_/|_|  
                                        """
        pewi5 ="""  
        |___/ \____//_/|_|            
                                        """
        pewi6 ="""      
                                        """
        os.system("cls")
        print(ThemeMain(wlcmsg1))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(wlcmsg2))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(wlcmsg3))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(wlcmsg4))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(wlcmsg5))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(wlcmsg6))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(wlcmsg7))
        time.sleep(.4)
        os.system("cls")
        print(ThemeMain(pewi1))
        time.sleep(.2)
        os.system("cls")
        print(ThemeMain(pewi12))
        time.sleep(.2)
        os.system("cls")
        print(ThemeMain(pewi1))
        time.sleep(.2)
        os.system("cls")
        print(ThemeMain(pewi12))
        time.sleep(.2)
        os.system("cls")
        print(ThemeMain(pewi1))
        time.sleep(.2)
        os.system("cls")
        print(ThemeMain(pewi12))
        time.sleep(.2)
        os.system("cls")   
        print(ThemeMain(pewi2))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(pewi3))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(pewi4))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(pewi5))
        time.sleep(.15)
        os.system("cls")
        print(ThemeMain(pewi6))
        time.sleep(.15)
        os.system("cls")
    else:
        os.system("cls")
        pass
