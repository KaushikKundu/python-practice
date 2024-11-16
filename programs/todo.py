todolist = []
def add():
    todo =  input("enter a todo: ")
    todolist.append(todo)
    print("todo added")
 

def display():
    print("Your todo list is: ")
    if len(todolist) == 0:
        print("no todos")
        return
    for index,todo in enumerate(todolist):
        print(f"{index+1}. {todo}")
        print("-------------")

def remove():
    print("enter the index of the todo you want to remove: ")
    index = int(input())
    if index < 1 or index > len(todolist):
        print("invalid index")
        return
    todolist.pop(index-1)
    print(f"todo {index} removed")

while True:
    print("1. add a todo\n2. display todo list\n3. remove a todo\n4. exit\n")
    choice = input("enter your choice: ")
    if choice == "1":
        add()
    elif choice == "2":
        display()
    elif choice == "3":
        remove()
    elif choice == "4":
        break
    else:
        print("invalid choice")
