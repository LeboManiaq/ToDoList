from misc import functions
while True:

#Starting input
    user_input = input("Type Add Edit Show Complete Exit: ")
    #user_input = user_input.strip()
  
    if user_input.startswith('add') or user_input.startswith('Add') :
        newitem = user_input[4:]

        todos = functions.get_todo()

        todos.append(newitem.capitalize() + '\n')

        functions.write_todo(todos) 
        
    elif user_input.startswith('show') or user_input.startswith("Show") :

        todos = functions.get_todo()
                        
        for index, items in enumerate(todos):
                items = items.strip('\n')
                print(index + 1, items)

    elif user_input.startswith('edit') or user_input.startswith('Edit'):
        try:

            todos = functions.get_todo()

            number = int(user_input[5:])
            newtodo = input(f'what would you like {todos[number -1]} to be?: ')
            todos[number -1] = newtodo.capitalize() + '\n'

            functions.write_todo(todos)
            
        except ValueError:
            print("input is incorrect")
            continue
        except IndexError:
            print("item value doesnt exist")
            continue

    elif user_input.startswith('complete') or user_input.startswith('Complete'):
        try:

            todos = functions.get_todo()

            number = int(user_input[8:])
            # number = number - 1
            todos.pop(number - 1)

            functions.write_todo(todos)

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