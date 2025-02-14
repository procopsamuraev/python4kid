from tkinter import *

# fix me while loop generation of strings

def change_language():
    if button["text"] == "English":
        button.config(text="Russian")
        list_elements[0].config(text=list_russian[0])
        list_elements[2].config(text=list_russian[1])
        list_elements[4].config(text=list_russian[2])
    else:
        button.config(text="English")
        list_elements[0].config(text=list_english[0])
        list_elements[2].config(text=list_english[1])
        list_elements[4].config(text=list_english[2])


root = Tk()
root.title("Login:")
root.geometry("350x150")
entry_width = 18
list_russian = ("Imya Polzovatelya:", "Familia Polzovatelya:", "God Rozdeniya Polzovatelya:")
list_english = ("User Name:", "User Surname:", "User Birth Year:")
list_elements= []
# list_vars = []
i=0
while i<len(list_english):
    y=i*30+20
    label_username = Label(text=list_english[i])
    label_username.place(x=10, y=y, anchor="w")
    list_elements.append(label_username)
    entry_user = Entry(text=list_english[i] , width=entry_width)
    entry_user.place(x=150, y=y, anchor="w")
    list_elements.append(entry_user)

    i = i + 1
button = Button(text="English", justify="center",  command=change_language)
button.place(relx=0.5, y=120, anchor="center")

root.mainloop()
