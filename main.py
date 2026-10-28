
while True:
    user_input = input("Type Add Edit Show Complete Exit: ")
    #user_input = user_input.strip()

    match user_input:
        case "Add":
            newitem = input("What do you want to add: ") + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(newitem)
            
            file = open('todos.txt', 'w')
            file.writelines(todos) 
            file.close()

        case "Complete":
            number = int(input("Which task do you want to remove"))
            number = number - 1
            todos.pop(number)
        
        case "Edit":
            number = int(input("which number todo do you want to edit: "))
            number = number - 1
            new_todo = input(f"Update {todos[number]} to? ")
            todos[number] = new_todo
            print(new_todo)
        
        case "Show":
            file = open('todos.txt', 'r')
            data = file.readlines()
            file.close()

            for index, i in enumerate(data):
                 print(index, i)

        case "Exit":
            break

print("bye")