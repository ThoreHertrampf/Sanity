from Class_Template import Template
import pyperclip
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

def refresh_window():
    for template in template_buttons:
        if template != None:
            template.grid(row = 1, column = template_buttons.index(template))


def create_template():
    name = "Test"
    for template in template_buttons:
        if template != None:
            template_buttons[template_buttons.index(template)] = Button(templates_frame, text = name)
            refresh_window()
            break



root = Tk()
root.title("Sanity")

options_frame = LabelFrame(root)
options_frame.grid(row = 1, column = 1)
templates_frame = LabelFrame(root, width = 100)
templates_frame.grid(row = 1, column = 2)

template_buttons = [None] * 10
template_buttons[0] = Button(templates_frame, text = "Name")

function_button_1 = Button(options_frame, text = "+", command = create_template, width = 5, height = 1)
function_button_1.grid(row = 1, column = 1)





root.mainloop()
