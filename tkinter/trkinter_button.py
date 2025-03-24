from tkinter import *

root = Tk()
root.title("GUI in Python")
root.geometry("300x250")
icon_image = PhotoImage(file=r"/usr/share/pixmaps/htop.png")
button = Button(root, text="Hello", image=icon_image, bg='black')
button.pack()
print(button['bg'])
root.mainloop()
