from Class_Template import Template
import pyperclip
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image


def create_template():

    def confirm_name():

        def confirm_template():

            def yes():
                new_template = Template(name, text)
                template_file = open("Templates.txt", "a+")
                template_file.write("\n\n" + new_template.name + "\n\n" + new_template.text + "\n" + "End of template: " + new_template.name + "\n")
                template_file.close()
                create_window.destroy()

            def no():
                template.destroy()
                question.destroy()
                yes.destroy()
                no.destroy()
                cancel.destroy()
                return

            def cancel():
                create_window.destroy()


            text = pyperclip.paste()
            question = Label(create_window, text = "Is this the input you want to save as a template?")
            question.grid(row = 3, column = 2)
            template = Label(create_window, text = text)
            template.grid(row = 4, column = 2)


            yes = Button(create_window, text = "Yes", command = yes)
            yes.grid(row = 5, column = 1)
            no = Button(create_window, text = "No", command = no)
            no.grid(row = 5, column = 2)
            cancel = Button(create_window, text = "Cancel", command = cancel)
            cancel.grid(row = 5, column = 3)


        name = template_name.get()
        template_name.delete(0, END)

        template_file = open("Templates.txt", "r")
        lines_file = template_file.readlines()

        for lines in lines_file:
            while lines == name+"\n":
                global wrong_name
                wrong_name = Label(create_window, text = "This name is already in use, please choose another one")
                wrong_name.grid(row = 2, column = 2)
                return
        template_file.close()
        pyperclip.copy("")

        if 'wrong_name' in globals():
            wrong_name.destroy()

        right_name = Label(create_window, text = "The name \"" + name + "\" is good!")
        right_name.grid(row = 2, column = 2)

        enter_template = Label(create_window, text = "Copy template to clipboard!")
        enter_template.grid(row = 3, column = 1)

        confirmation_template = Button(create_window, text = "Confirm!", command = confirm_template)
        confirmation_template.grid(row = 3, column = 3)




    create_window = Toplevel()
    create_window.title("Create Template")
    create_window.geometry("1000x600")

    label_entry = Label(create_window, text = "Enter the name of a new template!")
    label_entry.grid(row = 1, column = 1)

    template_name = Entry(create_window,  width = 40, borderwidth = 10)
    template_name.grid(row = 1, column = 2)

    confirm_button = Button(create_window, text = "Confirm!", command = confirm_name)
    confirm_button.grid(row = 1, column = 3)






    '''template_file = open("Templates.txt", "r")
    lines_file = template_file.readlines()
    name = input("Enter the name of a new template: ")

    for lines in lines_file:
        while lines == name+"\n":
            print("This name is already in use, please choose another one")
            name = input("Enter the name of a new template: ")
    template_file.close()
    pyperclip.copy("")

    while 1:
        print("Copy the template you want to save into the clipboard!\n")
        input("Press 'Enter' to continue!")
        text = pyperclip.paste()
        print(text)
        confirmation = input("Is this the input you want to save as a template? "
              "(Yes/No/Exit): ")

        if confirmation == "Yes" or confirmation == "yes":
            new_template = Template(name, text)
            template_file = open("Templates.txt", "a+")
            template_file.write("\n\n" + new_template.name + "\n\n" + new_template.text + "\n" + "End of template: " + new_template.name + "\n")
            template_file.close()
            break
        elif confirmation == "No" or confirmation == "no":
            continue
        elif confirmation == "Exit" or confirmation == "exit":
            break'''



def change_template():
    print("Changed Template")

def delete_template():
    loop = 1
    while loop == 1:
        template_file = open("Templates.txt", "r")
        lines_file = template_file.readlines()
        template_file.close()

        name = input("Type the name of the template you want to delete: ")

        if name == "exit":
            break

        for lines in lines_file:

            i = 1
            if lines != name + "\n":
                continue

            else:
                i = 0
                loop = 0
                print("Template found and deleted.")

                start = int(lines_file.index(name + "\n")) - 2
                end = int(lines_file.index("End of template: " + name + "\n"))

                for n in range(start, end + 1):
                    lines_file.pop(start)

                template_file = open("Templates.txt", "w")

                for lines in lines_file:
                    template_file.write(lines)

                template_file.close()
                break

        if i == 1:
            print("No template matching the name was found.")

def copy_template():

    loop = 1
    while loop == 1:
        template_file = open("Templates.txt", "r")
        lines_file = template_file.readlines()

        name = input("Type the name of the template you want to see: ")

        if name == "exit":
            break

        for lines in lines_file:

            i = 1
            if lines != name+"\n":
                continue

            else:
                i = 0
                loop = 0
                print("Template found and copied to clipboard.")

                start = int(lines_file.index(name + "\n")) + 2
                end = int(lines_file.index("End of template: " + name + "\n"))

                output = ""
                for n in range(start, end):
                    if ((n - start) % 2) == 0:  #because in txt are extra new lines for some reason
                        output = output + lines_file[n]

                pyperclip.copy(output)
                break

        if i == 1:
            print("No template matching the name was found.")

def switch_functions():
    print("What do you want to do?\n\n"
          "1: Create a new template\n"
          "2: Change an existing template\n"
          "3: Delete an existing template\n"
          "4: Copy existing template to clipboard\n")
    arg = 0
    while arg < 1 or arg > 4:
        arg = int(input("Number: "))

    switch_functions = {
        1: create_template,
        2: change_template,
        3: delete_template,
        4: copy_template,
    }
    function = switch_functions.get(arg, lambda: print("Invalid input!"))
    function()

#while 1:
#    switch_functions()



root = Tk()
root.title("Sanity")
#root.iconbitmap('')
root.geometry("1000x600")

function_button_1 = Button(root, text = "Create Template", command = create_template)
function_button_1.grid(row = 1, column = 1, padx = 10, pady = 5, ipadx = 10)
function_button_2 = Button(root, text = "Change Template", command = change_template)
function_button_2.grid(row = 2, column = 1, padx = 10, pady = 5, ipadx = 10)
function_button_3 = Button(root, text = "Copy Template", command = copy_template)
function_button_3.grid(row = 3, column = 1, padx = 10, pady = 5, ipadx = 10)
function_button_4 = Button(root, text = "Delete Template", command = delete_template)
function_button_4.grid(row = 4, column = 1, padx = 10, pady = 5, ipadx = 10)




root.mainloop()

#clipboard_content = pyperclip.paste()
#pyperclip.copy("Hello World")

#test2
