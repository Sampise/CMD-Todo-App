import json
import time
import os
import Editor
import Checklist
from colorama import Fore, Back, Style, init
import Options
from Welcome import welcomemsg
import pandas as pd
import ctypes

def set_terminal_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_terminal_title("Todo app")
init()


def get_config_settings():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    return config
config_settings = get_config_settings()

colors = config_settings.get('colors')  # on by default (can change in options or config.json)
delconfirm = config_settings.get('delconfirm')  # off by default (can change in options or config)
wlcanimation = config_settings.get('wlcanimation')

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
def cc():
    os.system("cls")
def saveData(todo, done):
    data ={
        "todo": todo,
        "done": done
    }
    
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
def printRed(text):
    if colors == True:
        crossed_text = Style.BRIGHT + Fore.RED + text + Style.RESET_ALL
        return crossed_text
    elif colors == False:
        return text
def printYellow(text):
    if  colors == True:
        crossed_text = Style.BRIGHT + Fore.YELLOW + text + Style.RESET_ALL
        return crossed_text
    elif colors == False:
        return text

colorlist = [Fore.BLUE, Fore.GREEN, Fore.MAGENTA, Fore.YELLOW, Fore.BLACK, Fore.CYAN, Fore.RED, Fore.WHITE]
colorlistinput = ["\033[0;34m", "\033[0;32m", "\033[0;35m", "\033[0;33m", "\033[0;30m", "\033[0;36m", "\033[0;31m", "\033[0;37m"]
def ThemeMain(text):
    if colors == True:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            color_index = config_data.get("mainindex")
        color = colorlist[color_index % len(colorlist)]
        crossed_text = Style.BRIGHT + color + text + Style.RESET_ALL
        return crossed_text
    elif colors == False:
        return text
    
def ThemeInput(text):
    if colors == True:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            main_color_index = config_data.get("mainindex")
        colored_text = f"{colorlistinput[main_color_index]}{text}\033[0m"
        return colored_text
    elif colors == False:
        return text
loadData()
cc()

def printGreen(text):
    if colors == True:
        crossed_text = Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL
        return crossed_text
    elif colors == False:
        return text

def saveexcel():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
    max_length = max(len(data['todo']), len(data['done']))
    data['todo'] += [''] * (max_length - len(data['todo']))
    data['done'] += [''] * (max_length - len(data['done']))
    df = pd.DataFrame(data)
    df.to_excel('TodoData.xlsx', index=False)

saveexcel()

menu = """MAIN MENU:
1.Show checklist
2.Checklist editor
3.Settings
4.Save data to excel file
•
0.Quit"""

def menuig():
    os.system('mode con: cols=100 lines=25') #prob change to 25 when finished
    global config_settings
    global colors
    global delconfirm
    while True:
        config_settings = get_config_settings()
        colors = config_settings.get('colors')
        delconfirm = config_settings.get('delconfirm')
        print(ThemeMain(menu))
        numinp = input(ThemeInput('Select an option:'))
        try:
            service_choice = int(numinp)
            if service_choice == 1: #checklist
                cc()
                saveData(tasks_todo,tasks_done)
                Checklist.checklistLoop()
                loadData()
            elif service_choice == 2: #editor
                cc()
                saveData(tasks_todo,tasks_done)
                Editor.editorLoop()
                loadData()
            elif service_choice == 3: #options
                cc()
                saveData(tasks_todo,tasks_done)
                Options.optionsLoop()
                loadData()
            elif service_choice == 4: #save data as excel file
                cc()
                print(ThemeMain('Working on it, please wait...'))
                saveData(tasks_todo,tasks_done)
                saveexcel()
                cc()
                print(printGreen("All data successfully saved in excel file! (TodoData.xslx)\n"))
                loadData()
            elif service_choice == 0:
                saveData(tasks_todo, tasks_done)
                cc()
                break
            else:
                cc()
                print(printRed(f'"{service_choice}" does not exist, please try again.'))
        except ValueError:
            cc()
            print(printRed(f'"{numinp}" is invalid input. Please enter a valid number.'))

if __name__ == "__main__":
    welcomemsg()
    cc()
    menuig()