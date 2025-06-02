from tkinter import *
# list_russian = ("Imya Polzovatelya:", "Familia Polzovatelya:", "God Rozdeniya Polzovatelya:")
list_russian = ["Imya Polzovatelya:", "Familia Polzovatelya:", "God Rozdeniya Polzovatelya:"]
# list_english = ("User Name:", "User Surname:", "User Birth Year:")
list_english = ["User Name:", "User Surname:", "User Birth Year:", 'City:']


def change_language():
    if button["text"] == "English":
        button.config(text="Russian")
        selected_language = list_russian
    else: 
        button.config(text="English")
        selected_language = list_english
    
    for index, label in enumerate(list_labels): 
        try: 
            label.config(text=selected_language[index])
        except IndexError:
            label.config(text=list_english[index])


root = Tk()
root.title("Login:")
x=len(list_english)*80
y=len(list_english)*50
size = f'{x}x{y}'
root.geometry(size)
entry_width = 18
list_labels = []
list_entries = []

for index, label in enumerate(list_english):
    y=index*30+20
    label_name = Label(text=label)
    label_name.place(x=10, y=y, anchor="w")
    list_labels.append(label_name)
    entry = Entry(text='1' , width=entry_width)
    entry.place(x=150, y=y, anchor="w")
    list_entries.append(entry)


button = Button(text="English", justify="center",  command=change_language)
button.place(relx=0.5, y=y+50, anchor="center")

root.mainloop()
