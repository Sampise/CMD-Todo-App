import json
import time
import os
from colorama import init, Fore, Back, Style
import Main
from functools import partial

init()
STRIKETHROUGH_ON = "\x1b[9m"
STRIKETHROUGH_OFF = "\x1b[29m"
#functions
def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def reset_color():
    return "\033[0m"
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
def switchList(list_a, index, list_b):
    if 0 <= index < len(list_a):
        item_to_switch = list_a.pop(index)
        list_b.append(item_to_switch)
def printRed(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.RED + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def printYellow(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.YELLOW + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def printMagenta(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.MAGENTA + text + Style.RESET_ALL
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
def ThemeInput(text):
    if Main.colors == True:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            main_color_index = config_data.get("mainindex")
        colored_text = f"{Main.colorlistinput[main_color_index]}{text}\033[0m"
        return colored_text
    elif Main.colors == False:
        return text
def printGreen(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def printBold(text, **kwargs):
    if Main.colors == True:
        todo_text = Style.BRIGHT + Fore.BLUE + text + Style.RESET_ALL
        print(todo_text)
    else:
        todo_text= text
        print_func = partial(print, todo_text, **kwargs)
        print_func()
def progressbar(todo_tasks, done_tasks):
    total_tasks = len(todo_tasks) + len(done_tasks)
    completed_tasks = len(done_tasks)
    try:
        completion_percentage = (completed_tasks / total_tasks) * 100
    except:
        completion_percentage = 0
    progress = int(67 * completion_percentage / 100)
    print(f"[{printGreen('●' * progress)}{'·' * (67 - progress)}]", end="")
    print(ThemeMain(f' {completion_percentage:.0f}% Complete\n'))
def showLists(list_a, list_b):
    print(ThemeMain(f"To do: ({len(list_a)})                                                            Done: ({len(list_b)})"))
    print(ThemeMain('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='))
    counter_a = 1
    counter_b = 1

    for line in range(max(len(list_a), len(list_b))):
        a = list_a[counter_a - 1] if counter_a <= len(list_a) else ""
        b = list_b[counter_b - 1] if counter_b <= len(list_b) else ""

        if counter_a <= len(list_a):
            if Main.colors == True:
                if counter_a == 1:
                    a = f'{counter_a}.{rgb_to_ansi(255, 165, 0)}{a}{reset_color()}'
                else:
                    a = f"{counter_a}.{printYellow(a)}"
            elif Main.colors == False:
                if a != None:
                    a = f"{counter_a}.{a}"
            counter_a += 1
        else:
            a = " " * 50

        if counter_b <= len(list_b):
            if Main.colors == True:
                b = f"{counter_b}.{printRed(b)}"
            elif Main.colors == False:
                if b != None:
                    b = f"{counter_b}.{b}"
            counter_b += 1
        else:
            b = ""
        if Main.colors == False:
            if len(a) == 50: 
                print(f"{a:<70}{b}")
            else:
                print(f"{a:<70}{b}")
        elif Main.colors == True:
            if counter_a == 2:
                if len(a) == 50: 
                    print(f"{a:<70}{b}")
                else:
                    print(f"{a:<91}{b}")
            else:  
                if len(a) == 50: 
                    print(f"{a:<70}{b}")
                else:
                    print(f"{a:<83}{b}")  
    print(ThemeMain('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='))
    progressbar(tasks_todo, tasks_done)  
options = """CHECKLIST:
1.Show Checklist
2.Mark tasks as done
3.Mark tasks as todo
4.Clear lists
•
0.Back"""

chooselist='''Choose a list to clear:
1.ToDo List
2.Done List
•
0.Cancel'''

def checklistLoop():
    config_settings = Main.get_config_settings()
    Main.colors = config_settings.get('colors')
    loadData()
    while True: 
        print(ThemeMain(options))
        nam = input(ThemeInput('Select an option:'))
        if nam == '1':
            cc()
            showLists(tasks_todo, tasks_done)
        elif nam == '2': #mark todo as done
            cc()
            while True:
                showLists(tasks_todo, tasks_done)
                index = input(ThemeInput('0.Back\nChoose a taks to mark as done.'))
                if index != '0':
                    try:
                        index = int(index)
                        if 0 <= index <= len(tasks_todo):
                            index -= 1
                            item = tasks_todo[index]
                            switchList(tasks_todo, index, tasks_done)
                            cc()
                            print(printGreen(f'"{item}" was successfuly marked as done!\n'))
                        else:
                           cc()
                           print(printRed(f'Task number {index} does not exist, please enter a valid number.\n')) 
                    except:
                        cc()
                        print(printRed(f'"{index}" is not a valid number, please try again.\n'))   
                else:
                    cc()
                    break
                saveData(tasks_todo,tasks_done)
        elif nam == '3': #mark done as todo
            cc()
            while True:
                showLists(tasks_todo, tasks_done)
                index = input(ThemeInput('0.Back\nChoose a taks to mark as todo.'))
                if index != '0':
                    try:
                        index = int(index)
                        if 0 <= index <= len(tasks_done):
                            index -= 1
                            item = tasks_done[index]
                            switchList(tasks_done, index, tasks_todo)
                            cc()
                            print(printGreen(f'"{item}" was successfuly marked as todo!\n'))
                        else:
                           cc()
                           print(printRed(f'Task number {index} does not exist, please enter a valid number.\n')) 
                    except:
                        cc()
                        print(printRed(f'"{index}" is not a valid number, please try again.\n'))   
                else:
                    cc()
                    break
                saveData(tasks_todo,tasks_done)
        elif nam == '4': #clear whole list(either todo or done)
            cc()
            print((ThemeMain(chooselist)))
            listnum = input(ThemeInput('Select an option:'))
            if listnum == '1':
                cc()
                confirmation = input(printRed('Are you sure you want to clear todo list? (Y/N)'))
                if confirmation.lower() == 'y':
                    cc()
                    tasks_todo.clear()
                    print(printGreen('Todo list sucessfuly cleared!\n'))
                else:
                    cc()
                    print(printRed('Clearing canceled!\n'))
                saveData(tasks_todo,tasks_done)
            elif listnum == '2':
                cc()
                confirmation = input(printRed('Are you sure you want to clear done list? (Y/N)'))
                if confirmation.lower() == 'y':
                    cc()
                    tasks_done.clear()
                    print(printGreen('Done list sucessfuly cleared!\n'))
                else:
                    cc()
                    print(printRed('Clearing canceled!\n'))
                saveData(tasks_todo,tasks_done)
            elif listnum == '0':
                cc()
                print(printRed('Tasklist clearing canceled!\n'))
                saveData(tasks_todo, tasks_done)
            else:
                cc()
                print(printRed(f'Invalid input! "{listnum}" is not a valid choice! Please try again.\n'))
        elif nam == '0':
            cc()
            saveData(tasks_todo, tasks_done)
            break
        else:
            cc()
            print(printRed(f'Invalid input! "{nam}" is not a valid choice! Please try again.\n'))