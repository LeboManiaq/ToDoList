
while True:

#Starting input
    user_input = input("Type Add Edit Show Complete Exit: ")
    #user_input = user_input.strip()

    if user_input.startswith('add') or user_input.startswith('Add') :
        newitem = user_input[4:]
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
            
        todos.append(newitem.capitalize() + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos) 
        
    elif user_input.startswith('show') or user_input.startswith("Show") :

        with open('todos.txt', 'r') as file:
            data = file.readlines()
                        

        for index, items in enumerate(data):
                items = items.strip('\n')
                print(index, items)

    elif user_input.startswith('edit') or user_input.startswith('Edit'):
        try:
            with open('todos.txt', 'r') as file:
                data = file.readlines()

            number = int(user_input[5:])
            newtodo = input(f'what would you like {data[number -1]} to be?: ')
            data[number -1] = newtodo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(data)
        except ValueError:
            print("input is incorrect")
            continue
        except IndexError:
            print("item value doesnt exist")
            continue

    elif user_input.startswith('complete') or user_input.startswith('Complete'):
        try:
            with open('todos.txt', 'r') as file:
                data = file.readlines()

            for index, item in enumerate(data):
                item = item.strip('\n')
                print(index + 1, item)

            number = int(user_input[8:])
            # number = number - 1
            data.pop(number - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(data)
        except ValueError:
            print("Input is incorrect")
            continue
        except IndexError:
            print("item value doesnt exist")
            continue
    
    elif user_input.startswith('exit') or user_input('Exit'):
        break
    else:
        print("command is not valid")

print("bye")