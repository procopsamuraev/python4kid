from tkinter import messagebox
# messagebox.showinfo('Message title', 'Message info content')
# messagebox.showwarning('Message warning title', 'Message warning content') # show warning message
# response = messagebox.askquestion('Message title', 'Message ask content')
# print(response)
# response = messagebox.askyesno('Message title', 'Message y/n content')
# print(response)
# response = messagebox.askyesnocancel('Message title', 'Message y/n/cancel content')
# print(response)
# response = messagebox.askokcancel('Message title', 'Message ok/cancel content')
# print(response)
# response = messagebox.askretrycancel('Message title', 'Message retry/cancel content')
# print(response)
from tkinter import *
from tkinter import filedialog

root = Tk()
document_open = filedialog.askopenfilename()
print(document_open)
document_save = filedialog.asksaveasfilename()
document_save = filedialog.ask
print(document_save)
root.mainloop()