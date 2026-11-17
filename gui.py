from misc import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a todo: ")
inputbox = sg.InputText(tooltip="Enter todo" ,key = "todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button =sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todo(), key="todos",
                      enable_events=True, size=[45,10])


interface = sg.Window("My To-Do App", 
                      layout=[[label],
                              [inputbox,add_button,edit_button,complete_button,exit_button],
                              [list_box]],
                              font=('Helvetica', '20'))


while True:
    event, values  = interface.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + '\n'

            todos.append(new_todo)
            functions.write_todo(todos)

            interface['todos'].update(values=[todos])

        case "Edit":
            new_todos = values['todo']
            todo_to_change = values['todos'][0]

            todos = functions.get_todo()
            index = todos.index(todo_to_change)

            todos[index] = new_todos + "\n"

            functions.write_todo(todos)
            interface['todos'].update(values=todos)

        case 'todos':
             interface['todo'].update(value=values['todos'][0])

        case "Complete":
            todos = functions.get_todo()
            todo_to_delete = values('todo')

            todos = functions.get_todo()
            index = todos.index(todo_to_delete)
            
            todos.pop[index]
            
            functions.write_todo(todos)

        case sg.WIN_CLOSED:
            break

        case "Exit":
            break

