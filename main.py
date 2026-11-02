
while True:
    user_input = input("Type Add Edit Show Complete Exit: ")
    #user_input = user_input.strip()

    match user_input:
        case "Add":
            newitem = input("What do you want to add: ") + "\n"
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                
            todos.append(newitem)

            with open('todos.txt', 'w') as file:
                file.writelines(todos) 
            
        case "Show":

            with open('todos.txt', 'r') as file:
                data = file.readlines()
                            

            for index, items in enumerate(data):
                 items = items.strip('\n')
                 print(index, items)

        case "Edit":
 
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
            
        case "Complete":

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

        
        case "Exit":
            break

print("bye")