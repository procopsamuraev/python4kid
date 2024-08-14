from tkinter import *

root = Tk()
root.title("Top")
root.geometry("400x300+830+0")  # 2560/2-400 = 830
root.title("Bottom")
root.geometry("400x300+830+1600")
root.title("Right")
root.geometry("400x300+2560+800")
root.title("Left")
root.geometry("400x300+0+800")
b = 1080//2
print("400x300+0+" + str(b))
# root.geometry("400x300+0+str(b)")
w_size = root.winfo_screenwidth()
h_size = root.winfo_screenheight()
window_size = "400x300"
location_1 = f'{window_size}+{int(w_size)//2}+0'
location_2 = f'{window_size}+{int(w_size)//2}+0'
print(location_1)
root.geometry(location_1)
root.mainloop()
# 3
root.title("Center")
root.geometry("400x300+1180+650")
# root.mainloop()
# 4
application_name = "python_tkinter"
application_version = 0.1
f = "Vladimir`s application - " + application_name + " - v." + str(application_version)
print(f)
root.title(f)
root.mainloop()
# 5 icon change
root.wm_iconbitmap("my_icon.ico")
root.mainloop()

