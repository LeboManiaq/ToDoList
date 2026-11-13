from misc import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a todo: ")
inputbox = sg.InputText(tooltip="Enter todo" ,key = "Todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button =sg.Button("Exit")

interface = sg.Window("My To-Do App", 
                      layout=[[label],
                              [inputbox,add_button,edit_button,complete_button,exit_button]],
                              font=('Helvetica', '20'))

event, values  = interface.read()
print(event)
print(values)
interface.close()

