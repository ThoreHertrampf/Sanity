from Class_Template import Template
import pyperclip

def create_template():
    template_file = open("Templates.txt", "r")
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
            break

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

while 1:
    switch_functions()

#clipboard_content = pyperclip.paste()
#pyperclip.copy("Hello World")
