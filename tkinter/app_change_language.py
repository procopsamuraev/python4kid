from tkinter import *


def change_language():
    if button["text"] == "English":
        button.config(text="Russian")
        label_username.config(text=list_russian[0])
        label_surname.config(text=list_russian[1])
        label_birth_year.config(text=list_russian[2])
    else:
        button.config(text="English")
        label_username.config(text=list_english[0])
        label_surname.config(text=list_english[1])
        label_birth_year.config(text=list_english[2])


root = Tk()
root.title("Login:")
root.geometry("350x150")
entry_width = 18
list_russian = ("Imya Polzovatelya:", "Familia Polzovatelya:", "God Rozdeniya Polzovatelya:")
list_english = ("User Name:", "User Surname:", "User Birth Year:")
label_username = Label(text=list_english[0])
label_username.place(x=10, y=20, anchor="w")
username = StringVar()
entry_username = Entry(textvariable=username, width=entry_width)
entry_username.place(x=150, y=20, anchor="w")

label_surname = Label(text=list_english[1])
label_surname.place(x=10, y=50, anchor="w")
surname = StringVar()
entry_surname = Entry(textvariable=surname, width=entry_width)
entry_surname.place(x=150, y=50, anchor="w")

label_birth_year = Label(text=list_english[2])
label_birth_year.place(x=10, y=80, anchor="w")
birth_year = StringVar()
entry_birth_year = Entry(textvariable=birth_year, width=entry_width)
entry_birth_year.place(x=150, y=80, anchor="w")

button = Button(text="English", justify="center",  command=change_language)
button.place(relx=0.5, y=120, anchor="center")


root.mainloop()