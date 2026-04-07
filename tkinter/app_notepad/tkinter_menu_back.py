import os
import tkinter
import pprint
from tkinter import *
from tkinter import filedialog, messagebox

x = 0
y = 0
clipboard = ''
list_menu = [
    ['file', ['new', 'open', 'save', 'close']],
    ['edit', ['copy', 'cut', 'paste', 'delete']],
    ['format', ['word wrap', 'font']],
    ['view', ['zoom', 'status bar']],
    ['help', ['view help', 'about notepad']]
]
list_menu_gen = []

list_pop_menu = ['copy', 'cut', 'paste']

def load_config(file):
    with open(file, 'r') as config_file:
        lines = config_file.readlines()
        # print(lines)
        for line in lines:
            if line.startswith(';'):
                continue
            # print(line.split(':'))
            # line.split(':')
            # menu1 = line.split(':')[0]
            list_menu_gen.append(line.split())
            # print(line.split()[0])

            # print(line.spplit())
            # top_menu_list = []
            # top_menu_list = line.split()[0]
            # top_menu_list.append('1')
            # list_menu_gen.append(top_menu_list)
            # sub_item_menu =[]
            # for sub_item_menu_gen in line.split(','):
            #     print(sub_item_menu_gen)
            #     list_menu_gen.append(sub_item_menu_gen)
                # menu1.append(sub_item_menu.split)
            # list_meny_gen.append()

        # for line in lines.split():
        #     print(line)
        # print(config_file.read())
    # pprint.pprint(list_menu_gen)

def pop_menu(event):
    menu_pop.post(event.x_root, event.y_root)


def save_to_file(file):
    file_text = open(file, 'r+')
    file_text.write(text.get(1.0, END))


# def open_file(file):
#     file_text = open(file, 'r+')
#     strings = file_text.read()
    # text.insert('1.0', file_text.read())

def open_file(self):
    file_path = filedialog.askopenfilename()
    initial_dir = os.getcwd()
    title='Select a File'
    if file_path:
        print('Selected file:', file_path)
    else:
        print('No file selected')

def copy_text(widget):
    return widget.selection_get() if  widget.tag_ranges(tkinter.SEL) else ''


def paste_text(widget):
    widget.insert(tkinter.INSERT, clipboard)


def print_text(arg):
   print('text_text', arg)


def toggle_word_wrap(widget):
    if widget.cget('wrap') != 'word':
        widget.configure(wrap='word')
    else:
        widget.configure(wrap='char')

def delete_text(widget):
    text.delete('sel.first', 'sel.last') if widget.tag_ranges(tkinter.SEL) else None


root = Tk()
main_menu = Menu(root)
name_file = 'text_sample.txt'
def command_wrap(arg:str):
    global clipboard
    if arg == 'open':
        open_file(name_file)
    elif arg == 'save':
        save_to_file(name_file)
    elif arg == 'close':
        response = messagebox.askyesno(title="Save", message="Save before closing?")
        if response:
            save_to_file(name_file)
        exit(1)
    elif arg == 'copy':
        clipboard = copy_text(text)
    elif arg == 'paste' and clipboard:
        paste_text(text)
    elif arg == 'cut':
        clipboard = copy_text(text)
        delete_text(text)
    elif arg == 'delete':
        delete_text(text)
    elif arg == 'word wrap':
        toggle_word_wrap(text)
    else:
        print('not a command', f"{arg=}")

load_config(file='tkinter_menu.cfg')

# for menu_ , list_menu_ in list_menu:
#     menu_text_ = f"{menu_}"
#     menu_ = Menu(main_menu, tearoff=0)
#     for list_submenu_ in list_menu_:
#         menu_.add_command(label=f"{list_submenu_.title()}", command =  lambda  arg = list_submenu_ :command_wrap(arg))
#     main_menu.add_cascade(label=menu_text_.title(), menu=menu_)
for line  in list_menu_gen:
    menu_top = line[0]
    menu_ = Menu(main_menu, tearoff=0)
    # print(line)
    for  submenu in line[1:]:
        sub_menu, command, shortcut = submenu.split(',')
        menu_.add_command(label = sub_menu.title(), command = command)
    main_menu.add_cascade(label = menu_top.title(), menu=menu_)
        # for list_submenu_ in submenu.split(','):
        #     print(list_submenu_)

        # print(submenu.split(','))
        # sub_menu, command, shortcut = list_submenu
        # print(command, shortcut)
   # menu_top, sub_menu, command, shortcut = line.split()
   # menu_.add_command(label=sub_menu, command=print_text)
   # main_menu.add_cascade(label=menu_top.title(), menu=menu_)
    # menu_text_ = f"{menu_}"
    # menu_ = Menu(main_menu, tearoff=0)
    # for list_submenu_ in list_menu_:
    #     menu_.add_command(label=f"{list_submenu_.title()}", command =  lambda  arg = list_submenu_ :command_wrap(arg))
    # main_menu.add_cascade(label=menu_text_.title(), menu=menu_)
root.config(menu=main_menu)


text = Text(wrap='word')
text.pack(fill='both', expand=True)

menu_pop = Menu(tearoff=0)
for menu_pop_item in list_pop_menu:
    menu_pop.add_command(label=f"{menu_pop_item}", command = lambda arg = menu_pop_item: command_wrap(arg))
text.bind('<Button-3>', pop_menu)

text.bind('<Control-c>', lambda event : command_wrap('copy'))
text.bind('<Control-v>', lambda event : command_wrap('paste'))
text.bind('<Control-o>', lambda event : command_wrap('open'))

root.mainloop()