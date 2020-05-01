from Class_Template import Template
import pyperclip
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

def refresh_window():


    template_file = open("Templates.txt", "r")
    lines_file = template_file.readlines()

    length = len(lines_file)
    if length > 2:
        template_button_names[0] = lines_file[2]

    i = 0
    for lines in lines_file:
        if lines == "End of template: " + template_button_names[i]:
            if lines_file.index(lines)+3 > len(lines_file):
                break

            template_button_names[i+1] = lines_file[lines_file.index(lines)+3]

            i = i + 1

    template_file.close()

    #creating buttons
    i = 0
    for template in template_buttons:
        if template == None:
            if template_button_names[template_buttons.index(template)] != None:
                length = len(template_button_names[template_buttons.index(template)])
                name = template_button_names[template_buttons.index(template)]
                name = name[:length - 1]
                template_buttons[template_buttons.index(template)] = Button(templates_frame, text = name, width = 10, height = 1, command = lambda j = name: copy_template(j))
        i = i + 1

    #putting buttons on screen
    for template in template_buttons:
        if template != None:
            template.grid(row = 1, column = template_buttons.index(template))

def create_template():

    def confirm_name():

        def confirm_template():

            def yes():
                new_template = Template(name, text)
                template_file = open("Templates.txt", "a+")
                template_file.write("\n\n" + new_template.name + "\n\n" + new_template.text + "\n" + "End of template: " + new_template.name + "\n")
                template_file.close()
                create_window.destroy()
                refresh_window()

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

def copy_template(name):

    template_file = open("Templates.txt", "r")
    lines_file = template_file.readlines()

    for lines in lines_file:

        i = 1
        if lines != name+"\n":
            continue

        else:
            i = 0
            loop = 0

            start = int(lines_file.index(name + "\n")) + 2
            end = int(lines_file.index("End of template: " + name + "\n"))

            output = ""
            for n in range(start, end):
                if ((n - start) % 2) == 0:  #because in txt are extra new lines for some reason
                    output = output + lines_file[n]

            pyperclip.copy(output)
            return

def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

root = Tk()
root.title("Sanity")
#root.deiconify()
#root.iconbitmap('')
#root.overrideredirect(True)
root.geometry('1000x29+0+0')
root.bind('<B1-Motion>', move_window)


options_frame = LabelFrame(root)
#options_frame.grid(row = 1, column = 1)
options_frame.grid(row = 1, column = 1)

templates_frame = LabelFrame(root)
#templates_frame.grid(row = 1, column = 2)
templates_frame.grid(row = 1, column = 2)

exit_frame = LabelFrame(root)
#exit_frame.grid(row = 1, column = 3)
exit_frame.grid(row = 1, column = 3, sticky = W+E)




create_button = Button(options_frame, text = "+", command = create_template, width = 5, height = 1)
create_button.grid(row = 1, column = 1)
copy_button = Button(options_frame, text = "=", command = copy_template, width = 5, height = 1)
copy_button.grid(row = 1, column = 2)
change_button = Button(options_frame, text = "~", command = change_template, width = 5, height = 1)
change_button.grid(row = 1, column = 3)
delete_button = Button(options_frame, text = "-", command = delete_template, width = 5, height = 1)
delete_button.grid(row = 1, column = 4)

exit_button = Button(exit_frame, text = "X", command = exit, width = 5, height = 1)
exit_button.grid(row = 1, column = 1, sticky = E)

template_buttons = [None] * 10
template_button_names = [None] * 10

refresh_window()

root.mainloop()

#clipboard_content = pyperclip.paste()
#pyperclip.copy("Hello World")
