import os
from tkinter import *
from tkinter import filedialog


class FileActions:
    def __init__(self, parent: Tk) -> None:
        pass


    def save_to_file(self):
        print('saving to file')


    def open_file(self):
        file_path = filedialog.askopenfilename()
        initial_dir = os.getcwd()
        title='Select a File'
        if file_path:
            print('Selected file:', file_path)
        else:
            print('No file selected')


# def file_open() -> None:
#     print('file_path')
#
# def file_save(file_path:str) -> None:
#     pass
#
# def file_close() -> None:
#     pass


root = Tk()
main_menu = Menu(root)

command1 = FileActions(root)
# command.save_to_file()

list_menu = [
    ['file', ['new', 'open', 'close']],
    ['edit', ['undo', 'cut', 'paste', 'delete']],
    ['format', ['word wrap', 'font']],
    ['view', ['zoom', 'status bar']],
    ['help', ['view help', 'about notepad']]
]

for menu_ , list_menu_ in list_menu:
    menu_text_ = f"{menu_}"
    menu_ = Menu(main_menu, tearoff=0)
    for list_submenu_ in list_menu_:
        # menu_.add_command(label=f"{list_submenu_.title()}")
        menu_.add_command(label=f"{list_submenu_.title()}", command=command1)
    main_menu.add_cascade(label=menu_text_.title(), menu=menu_)
root.config(menu=main_menu)


text = Text(wrap='word')
text.pack(fill='both', expand=True)


root.mainloop()