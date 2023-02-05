#!/usr/bin/env python
print("\033c")
def print_todos():
    print("Todo List:")
    for todo in todos:
        print(" - ", todo)

alternatives = ["Add to todo list", "Remove from todo list", "Quit"]
todos = ["Running", "Cleaning", "Cooking"]
answer = ""

while answer != "3":
    print_todos()
    print("")
    for alternative in alternatives:
        print(alternatives.index(alternative) + 1, alternative)
    answer = input("What do you want to do? ")
    #clean screen
    print("\033c")
    if answer == "1":
        print_todos()
        print("")
        new_todo = input("What do you want to add? ")
        todos.append(new_todo)
        print("\033c")
    if answer == "2":
        print_todos()
        print("")   
        remove = input("What do you want to remove? ")
        todos.remove(remove)
        print("\033c")

