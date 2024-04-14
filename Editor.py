import json
import time
import os
import Main
from colorama import Fore, Back, Style, init
import pyperclip
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
def addTask(todo):
    tasks_todo.append(todo)
def printGreen(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.GREEN + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def removeTask(listnum, num):
    num = num - 1
    cc()
    if listnum == 1:
        try:
            if Main.delconfirm:
                confirmation = input(printRed("Are you sure you want to delete this Task? (Y/N): "))
                if confirmation.lower() == 'y':
                    cc()
                    print(printRed(f'"{tasks_todo[num]}" deleted!\n'))
                    tasks_todo.pop(num)
                else:
                    cc()
                    print(printGreen("Deletion canceled.\n"))
            else:
                cc()
                print(printRed(f'"{tasks_todo[num]}" deleted!\n'))
                tasks_todo.pop(num)
        except:
            amt = len(tasks_todo)
            print(printRed(f'"{num}" is invalid input, please enter a number between 1 and {amt}!\n'))
    elif listnum == 2:
        try:
            if Main.delconfirm:
                confirmation = input(printRed("Are you sure you want to delete this Task? (Y/N): "))
                if confirmation.lower() == 'y':
                    cc()
                    print(printRed(f'"{tasks_done[num]}" deleted!\n'))
                    tasks_done.pop(num)
                else:
                    print(printGreen("Deletion canceled.\n"))
            else:
                cc()
                print(printRed(f'"{tasks_done[num]}" deleted!\n'))
                tasks_done.pop(num)
        except:
            amt = len(tasks_done)
            print(printRed(f'"{num}" is invalid input, please enter a number between 1 and {amt}!\n'))
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
def printRed(text):
    if Main.colors == True:
        crossed_text = Style.BRIGHT + Fore.RED + text + Style.RESET_ALL
        return crossed_text
    elif Main.colors == False:
        return text
def sort_list_items(lst, option):
    if option == 'abc_up':
        lst.sort(key=lambda x: x.lower())
    elif option == 'abc_down':
        lst.sort(key=lambda x: x.lower(), reverse=True)
    elif option == 'char_count_up':
        lst.sort(key=len)
    elif option == 'char_count_down':
        lst.sort(key=len, reverse=True)
menu = """EDITOR:
1.Add a task
2.Remove a task
3.Sort lists
•
0.Back"""

chooselist='''Choose a list to remove from:
1.ToDo List
2.Done List
•
0.Cancel'''

#write tasks to excel                                                                                               -

def editorLoop():
    config_settings = Main.get_config_settings()
    Main.colors = config_settings.get('colors')
    loadData()
    while True:
        print(ThemeMain(menu))
        nam = input(ThemeInput('Select an option:'))
        if nam == '1':
            cc()
            print(ThemeMain("Add a task to checklist:\n•\n0.Cancel"))
            todo = input(ThemeInput('Enter task:'))
            cc()
            if todo != '' and todo != '0':
                if len(todo) > 28:
                    print(printRed('Task input too long(28 char max), your input has been copied to your clipboard.\n'))
                    pyperclip.copy(todo)
                else:
                    addTask(todo)
                    print(printGreen(f'"{todo}" added to todo list!'))
            elif todo == '0':
                cc()
                print(printRed("Task addition canceled.\n"))
                pass
            else:
                print(printRed("Couldn't add the task, please try again!\n"))
            saveData(tasks_todo,tasks_done)

        elif nam == '2':
            cc()
            print((ThemeMain(chooselist)))
            listnum = input(ThemeInput('Select an option:'))
            try:
                listint = int(listnum)
                if listint == 1:  
                    cc() 
                    print(ThemeMain('Choose a task to remove:'))
                    for i, item in enumerate(tasks_todo, start=1):
                        print(ThemeMain(f'{i}.{item}'))
                    print(ThemeMain('•\n0.Cancel'))
                    index = input(ThemeInput('Select an option:'))
                    if index != '0':
                        try:
                            numindex = int(index) 
                            removeTask(listint, numindex)
                        except:
                            cc()
                            print(printRed(f'"{index}" is invalid input. Please enter a valid number.\n'))
                    else:
                        cc()
                    saveData(tasks_todo,tasks_done)
                elif listint == 2:
                    cc() 
                    print(ThemeMain('Choose a task to remove:'))
                    for i, item in enumerate(tasks_done, start=1):
                        print(ThemeMain(f'{i}.{item}'))
                    print(ThemeMain('•\n0.Cancel'))
                    index = input(ThemeInput('Select an option:'))
                    if index != '0':
                        try:
                            numindex = int(index) 
                            removeTask(listint, numindex)
                        except:
                            cc()
                            print(printRed(f'"{index}" is invalid input. Please enter a valid number.\n'))
                    else:
                        cc()
                    saveData(tasks_todo,tasks_done)
                elif listint == 0:
                    cc()
                    pass
                else:
                    cc()
                    print(printRed(f'{listint} is not a valid option.\n'))
            except:
                cc()
                print(printRed(f'"{listnum}" is invalid input. Please enter a valid number.\n'))
        elif nam == '3': #sort tasks
            cc()
            print(ThemeMain("Sorting options:\n1.Ascending alphabetical order\n2.Descending alphabetical order\n3.Ascending character length order\n4.Descending character length order\n•\n0.Back"))
            ordernum = input(ThemeInput('Select an option:'))
            if ordernum == '1':
                cc()
                print(ThemeMain('Select list:\n1.Todo list\n2.Done list\n3.Both\n•\n0.Back'))
                listchoice = input(ThemeInput('Select an option:'))
                if listchoice == '1':
                    cc()
                    sort_list_items(tasks_todo,'abc_up')
                    print(printGreen('List succesfully sorted in ascending alphabetical order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '2':
                    cc()
                    sort_list_items(tasks_done,'abc_up')
                    print(printGreen('List succesfully sorted in ascending alphabetical order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '3':
                    cc()
                    sort_list_items(tasks_todo,'abc_up')
                    sort_list_items(tasks_done,'abc_up')
                    print(printGreen('Lists succesfully sorted in ascending alphabetical order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '0':
                    cc()
                else:
                    cc()
                    print(printRed(f'"{ordernum}" is invalid input. Please enter a valid number.\n'))
            elif ordernum == '2':
                cc()
                print(ThemeMain('Select list:\n1.Todo list\n2.Done list\n3.Both\n•\n0.Back'))
                listchoice = input(ThemeInput('Select an option:'))
                if listchoice == '1':
                    cc()
                    sort_list_items(tasks_todo,'abc_down')
                    print(printGreen('List succesfully sorted in descending alphabetical order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '2':
                    cc()
                    sort_list_items(tasks_done,'abc_down')
                    print(printGreen('List succesfully sorted in descending alphabetical order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '3':
                    cc()
                    sort_list_items(tasks_todo,'abc_down')
                    sort_list_items(tasks_done,'abc_down')
                    print(printGreen('Lists succesfully sorted in descending alphabetical order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '0':
                    cc()
                else:
                    cc()
                    print(printRed(f'"{ordernum}" is invalid input. Please enter a valid number.\n'))
            elif ordernum == '3':
                cc()
                print(ThemeMain('Select list:\n1.Todo list\n2.Done list\n3.Both\n•\n0.Back'))
                listchoice = input(ThemeInput('Select an option:'))
                if listchoice == '1':
                    cc()
                    sort_list_items(tasks_todo,'char_count_up')
                    print(printGreen('List succesfully sorted in ascending character length order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '2':
                    cc()
                    sort_list_items(tasks_done,'char_count_up')
                    print(printGreen('List succesfully sorted in ascending character length order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '3':
                    cc()
                    sort_list_items(tasks_todo,'char_count_up')
                    sort_list_items(tasks_done,'char_count_up')
                    print(printGreen('Lists succesfully sorted in ascending character length order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '0':
                    cc()
                else:
                    cc()
                    print(printRed(f'"{ordernum}" is invalid input. Please enter a valid number.\n'))
            elif ordernum == '4':
                cc()
                print(ThemeMain('Select list:\n1.Todo list\n2.Done list\n3.Both\n•\n0.Back'))
                listchoice = input(ThemeInput('Select an option:'))
                if listchoice == '1':
                    cc()
                    sort_list_items(tasks_todo,'char_count_down')
                    print(printGreen('List succesfully sorted in descending character length order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '2':
                    cc()
                    sort_list_items(tasks_done,'char_count_down')
                    print(printGreen('List succesfully sorted in descending character length order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '3':
                    cc()
                    sort_list_items(tasks_todo,'char_count_down')
                    sort_list_items(tasks_done,'char_count_down')
                    print(printGreen('Lists succesfully sorted in descending character length order!\n'))
                    saveData(tasks_todo,tasks_done)
                elif listchoice == '0':
                    cc()
                else:
                    cc()
                    print(printRed(f'"{ordernum}" is invalid input. Please enter a valid number.\n'))
            elif ordernum == '0':
                cc()
                saveData(tasks_todo,tasks_done)
            else:
                cc()
                print(printRed(f'"{ordernum}" is invalid input. Please enter a valid number.\n'))
        elif nam == '0':
            cc()
            saveData(tasks_todo,tasks_done)
            break
        else:
            cc()
            print(printRed(f'"{nam}" is invalid input. Please enter a valid number.\n'))


