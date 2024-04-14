import json
import time
import os
from colorama import Fore, Back, Style, init
from functools import partial
import Main
init()


#functions
def loadData():
    global tasks_todo, tasks_done
    try:
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)
            tasks_todo = data['todo']
            tasks_done= data['done']
    except:
        print("Counld't load data file, please try again.")
        time.sleep(0.5)
        quit()
def saveData(todo, done):
    data ={
        "todo": todo,
        "done": done
    }
    
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
def cc():
    os.system("cls") 
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
def nextcolor(text):
    if Main.colors == True:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            color_index = config_data.get("mainindex")
        color = Main.colorlist[(color_index + 1) % len(Main.colorlist)]
        crossed_text = Style.BRIGHT + color + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def ThemeInput(text):
    if Main.colors == True:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            main_color_index = config_data.get("mainindex")
        colored_text = f"{Main.colorlistinput[main_color_index]}{text}\033[0m"
        return colored_text
    elif Main.colors == False:
        return text
def printRed(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.RED + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def printGreen(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def settingsStatus(value):
    config_settings = Main.get_config_settings()
    status = config_settings.get(value)
    if status == True:
        on = printGreen("ON")
        return on
    elif status == False:
        off = printRed("OFF")
        return off
def cyclecolors():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            current_index = config.get('mainindex', 0)
    except (FileNotFoundError, json.JSONDecodeError):
        current_index = 0 
        config = {}
    current_index = (current_index + 1) % len(Main.colorlist)
    config['mainindex'] = current_index
    with open('config.json', 'w') as f:
        json.dump(config, f)
    return Main.colorlist[current_index]

def optionsLoop():
    while True:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        loadData()
        print(ThemeMain("SETTINGS:"))
        print(f'{ThemeMain("1.Toggle colors ")}{settingsStatus("colors")}')
        print(f'{ThemeMain("2.Toggle delete confirmation ")}{settingsStatus("delconfirm")}')
        print(f'{ThemeMain("3.Toggle welcome animation ")}{settingsStatus("wlcanimation")}')
        print(f'{ThemeMain("4.Change color theme ▹ ")}{nextcolor("◉ ")}{ThemeMain("◃")}')
        print(ThemeMain("•\n0.Back"))
        inp = input(ThemeInput('Select an option:'))
        if inp == '1': #toggle colors or on off (may add custom colors later on...)
            cc()
            if config.get('colors') == True:
                config['colors'] = False
                with open('config.json', 'w') as config_file:
                    json.dump(config, config_file, indent=4)
                config_settings = Main.get_config_settings()
                Main.colors = config_settings.get('colors')
                print(ThemeMain('Colors toggled '), end='')
                print(f"{settingsStatus('colors')}{ThemeMain('!')}\n")
            elif config.get('colors') == False:
                config['colors'] = True
                with open('config.json', 'w') as config_file:
                    json.dump(config, config_file, indent=4)
                config_settings = Main.get_config_settings()
                Main.colors = config_settings.get('colors')
                print(ThemeMain('Colors toggled '), end='')
                print(f"{settingsStatus('colors')}{ThemeMain('!')}\n")
        elif inp == '2': #deletion confirmation
            cc()
            if config.get('delconfirm') == True:
                config['delconfirm'] = False
                with open('config.json', 'w') as config_file:
                    json.dump(config, config_file, indent=4)
                config_settings = Main.get_config_settings()
                Main.delconfirm = config_settings.get('delconfirm')
                print(ThemeMain('Welcome animation toggled '), end='')
                print(f"{settingsStatus('delconfirm')}{ThemeMain('!')}\n")
            elif config.get('delconfirm') == False:
                config['delconfirm'] = True
                with open('config.json', 'w') as config_file:
                    json.dump(config, config_file, indent=4)
                config_settings = Main.get_config_settings()
                Main.delconfirm = config_settings.get('delconfirm')
                print(ThemeMain('Welcome animation toggled '), end='')
                print(f"{settingsStatus('delconfirm')}{ThemeMain('!')}\n")
        elif inp == '3': #toggle animation
            cc()
            if config.get('wlcanimation') == True:
                config['wlcanimation'] = False
                with open('config.json', 'w') as config_file:
                    json.dump(config, config_file, indent=4)
                config_settings = Main.get_config_settings()
                Main.wlcanimation = config_settings.get('wlcanimation')
                print(ThemeMain('Welcome animation toggled '), end='')
                print(f"{settingsStatus('wlcanimation')}{ThemeMain('!')}\n")
            elif config.get('wlcanimation') == False:
                config['wlcanimation'] = True
                with open('config.json', 'w') as config_file:
                    json.dump(config, config_file, indent=4)
                config_settings = Main.get_config_settings()
                Main.wlcanimation = config_settings.get('wlcanimation')
                print(ThemeMain('Welcome animation toggled '), end='')
                print(f"{settingsStatus('wlcanimation')}{ThemeMain('!')}\n")
        elif inp == '4':
            cc()
            cyclecolors()
        elif inp == '0':
            saveData(tasks_todo,tasks_done)
            cc()
            break
        else:
            cc()
            print(printRed(f'"{inp}" is an invalid choice, please try again!\n'))
