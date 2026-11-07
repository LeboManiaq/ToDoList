#Creating Todo's function
def get_todo(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todo(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        todos_local = file_local.writelines(todos_arg)


            
while True:

#Starting input
    user_input = input("Type Add Edit Show Complete Exit: ")
    #user_input = user_input.strip()
  
    if user_input.startswith('add') or user_input.startswith('Add') :
        newitem = user_input[4:]

        todos = get_todo('todos.txt')

        todos.append(newitem.capitalize() + '\n')

        write_todo('todos.txt',todos) 
        
    elif user_input.startswith('show') or user_input.startswith("Show") :

        todos = get_todo('todos.txt')
                        
        for index, items in enumerate(todos):
                items = items.strip('\n')
                print(index, items)

    elif user_input.startswith('edit') or user_input.startswith('Edit'):
        try:

            todos = get_todo('todos.txt')

            number = int(user_input[5:])
            newtodo = input(f'what would you like {todos[number -1]} to be?: ')
            todos[number -1] = newtodo.capitalize() + '\n'

            write_todo('todos.txt',todos)
            
        except ValueError:
            print("input is incorrect")
            continue
        except IndexError:
            print("item value doesnt exist")
            continue

    elif user_input.startswith('complete') or user_input.startswith('Complete'):
        try:

            todos = get_todo('todos.txt')

            number = int(user_input[8:])
            # number = number - 1
            todos.pop(number - 1)

            write_todo('todos.txt',todos)

        except ValueError:
            print("Input is incorrect")
            continue
        except IndexError:
            print("item value doesnt exist")
            continue
    
    elif user_input.startswith('exit') or user_input.startswith('Exit'):
        break
    else:
        print("command is not valid")

print("bye")