
while True:
    user_input = input("Type Add Edit Show Complete Exit: ")
    #user_input = user_input.strip()

    if "Add" in user_input:
        newitem = user_input[4:]
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            
        todos.append(newitem)

        with open('todos.txt', 'w') as file:
            file.writelines(todos) 
        
    elif "Show" in user_input:

        with open('todos.txt', 'r') as file:
            data = file.readlines()
                        

        for index, items in enumerate(data):
                items = items.strip('\n')
                print(index, items)

    elif "Edit" in user_input:

        with open('todos.txt', 'r') as file:
            data = file.readlines()

        for index, item in enumerate(data):
            item = item.strip('\n')
            print(index + 1, item)

        number = int(input("which todo would you like to edit: "))
        new_todo = input(f"what would you like to change {data[number - 1 ]} to: ")
        data[number - 1] = new_todo + '\n'
        
        with open('todos.txt', 'w') as file:
            file.writelines(data)
        
    elif "Complete" in user_input:

        with open('todos.txt', 'r') as file:
            data = file.readlines()

        for index, item in enumerate(data):
            item = item.strip('\n')
            print(index + 1, item)

        number = int(input("Which task do you want to remove: "))
        # number = number - 1
        data.pop(number - 1)

        with open('todos.txt', 'w') as file:
            file.writelines(data)

    
    elif "Exit" in user_input:
        break
    else:
        print("command is not valid")

print("bye")