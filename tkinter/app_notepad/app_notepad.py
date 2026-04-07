import os
import tkinter
import pprint
from tkinter import *
from tkinter import filedialog, messagebox


x = 0
y = 0
clipboard = ''
list_menu_gen = []

list_pop_menu = []
file_path = ''

#def load_config(file):
#    global list_pop_menu
#    with open(file, 'r') as config_file:
#        lines = config_file.readlines()
#        for line in lines:
#            if line.startswith(';'): # ignore comments
#                continue
#            elif line.startswith('edit'): # for right click menu
#                list_pop_menu=line.strip().split(';')[1:]
#            list_menu_gen.append(line.strip().split(';'))
#    pprint.pprint(list_menu_gen)

def load_config(file):
    global list_pop_menu
    with open(file, 'r') as config_file:
        lines = config_file.readlines()
        list_ = []
        for line in lines:
            line = line.strip().strip(',').strip("'")
            if line.startswith(';'): # ignore comments
                continue
            elif line.startswith('['):
                if len(list_) > 0:
                    list_menu_gen.append(list_)
                list_ = []
            elif line.startswith(']'):
                list_menu_gen.append(list_)
            else:
                list_.append(line)

    pprint.pprint(list_menu_gen)
    exit(1)

def pop_menu(event):
    menu_pop.post(event.x_root, event.y_root)


def save_to_file(widget):
    global file_path
    if not file_path:
        file_path = filedialog.asksaveasfilename(
            defaultextension='.txt'
        )
    with open(file_path, 'w') as file:
        file.write(widget.get("1.0", END))


def open_file(widget):
    file_path = filedialog.askopenfilename()
    initial_dir = os.getcwd()
    title='Select a File'
    if file_path:
        with open(file_path, 'r+') as file:
            text_content = file.read()
            widget.delete(1.0, END)
            widget.insert("1.0", text_content)
    else:
        print('No file selected')
    return  file_path


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
    global clipboard, file_path
    if arg == 'open':
        file_path = open_file(text)
    elif arg == 'save':
        save_to_file(text)
    elif arg == 'close':
        response = messagebox.askyesno(title="Save", message="Save before closing?")
        if response:
            save_to_file(text)
        exit(1)
    elif arg == 'copy':
        clipboard = copy_text(text)
        print(clipboard)
    elif arg == 'paste' and clipboard:
        paste_text(text)
    elif arg == 'cut':
        clipboard = copy_text(text)
        delete_text(text)
    elif arg == 'delete':
        delete_text(text)
    elif arg == 'word_wrap':
        toggle_word_wrap(text)
    else:
        print('command is not defined', f"{arg=}")

load_config(file='tkinter_menu.cfg')

for line  in list_menu_gen:
    menu_top = line[0]
    menu_ = Menu(main_menu, tearoff=0)
    for  submenu in line[1:]:
        list_submenu_= submenu.split(',')
        if len(list_submenu_) == 3:
            sub_menu, command, shortcut = list_submenu_
            shortcut = '' if shortcut == 'none' else shortcut
            menu_.add_command(label = f"{sub_menu.title()} {shortcut}", command = lambda  arg = command: command_wrap(arg))
        else:
            print(f"Error in config. Please check the config file near: {list_submenu_}")
    main_menu.add_cascade(label = menu_top.title(), menu=menu_)
root.config(menu=main_menu)


text = Text(wrap='word')
text.pack(fill='both', expand=True)

menu_pop = Menu(tearoff=0)
for menu_pop_item in list_pop_menu:
    sub_menu, command, shortcut = menu_pop_item.split(',')
    menu_pop.add_command(label=f"{sub_menu} {shortcut}", command = lambda arg = command: command_wrap(arg))
text.bind('<Button-3>', pop_menu)

text.bind('<Control-c>', lambda event : command_wrap('copy'))
text.bind('<Control-v>', lambda event : command_wrap('paste'))
text.bind('<Control-o>', lambda event : command_wrap('open'))

root.mainloop()