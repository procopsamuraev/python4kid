from tkinter import *
# list_russian = ("Imya Polzovatelya:", "Familia Polzovatelya:", "God Rozdeniya Polzovatelya:")
list_russian = ["Imya Polzovatelya:", "Familia Polzovatelya:", "God Rozdeniya Polzovatelya:"]
# list_english = ("User Name:", "User Surname:", "User Birth Year:")
list_english = ["User Name:", "User Surname:", "User Birth Year:", 'City:']

# fix me while loop generation of strings

def change_language():
    if button["text"] == "English":
        button.config(text="Russian")
        selected_language = list_russian
    else: 
        button.config(text="English")
        selected_language = list_english
          
    i = 0
    while i < len(list_english):
        try: 
            list_elements[i].config(text=selected_language[i])
        except IndexError:
            list_elements[i].config(text=list_english[i])
        i += 1


root = Tk()
root.title("Login:")
x=len(list_english)*80
y=len(list_english)*50
size = f'{x}x{y}'
root.geometry(size)
entry_width = 18
list_elements= []

i=0
while i<len(list_english):
    y=i*30+20
    label_username = Label(text=list_english[i])
    label_username.place(x=10, y=y, anchor="w")
    list_elements.append(label_username)
    entry_user = Entry(text=list_english[i] , width=entry_width)
    entry_user.place(x=150, y=y, anchor="w")
    i = i + 1


button = Button(text="English", justify="center",  command=change_language)
button.place(relx=0.5, y=y+50, anchor="center")

root.mainloop()
