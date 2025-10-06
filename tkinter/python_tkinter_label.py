from tkinter import *

root = Tk()
# label_1 = Label(root, text="It`s my first label")
# label_1.pack()
# label_2 = Label(root, text="It`s my 2nd label")
# label_2.pack()
# label_3 = Label(root, text="It`s my 3rd label\nIt`s my 4th label on a new string")
# label_3.pack()
letter_address = "Na derevnu"
letter_name = "Ded Moroz"
letter_year = 1988
letter_label = "Address: %s\nTo: %s\n Year: %s " % (letter_address, letter_name, letter_year)
letter_ded_moroz=str("{0}\n Hi {1}.\n Long time no see".format(letter_label, letter_name)).center(70)
label_5 = Label(root, text=letter_ded_moroz)
print(letter_ded_moroz)

root.mainloop