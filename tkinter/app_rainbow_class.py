from tkinter import *

class ButtonRainbow:
    font_text: str = ('Ubuntu Mono', 12)

    def __init__(self, parent: Tk, color: str = 'white', color_code: str = '#ff0000', text: str = '', color_code_var: StringVar = None, label: Label = None):
        self.color = color
        self.color_code = color_code
        self.text = text
        self.color_code_var = color_code_var
        self.label = label
        Button(parent, font=ButtonRainbow.font_text, text=self.text, bg=self.color_code, command=self.draw_button).pack(fill='x')

    def draw_button(self):
        self.color_code_var.set(self.color_code)
        self.label.config(text=self.color, background=self.color)

list_colors = [
    ['red', '#ff0000'],
    ['orange', '#ff7d00'],
    ['yellow', '#ffff00'],
    ['green', '#00ff00'],
    ['lightblue', '#007dff'],
    ['blue', '#0000ff'],
    ['purple', '#7d00ff']
]

root = Tk()
root.title("Colors")
label_color = Label(text="Color name", font=ButtonRainbow.font_text, fg="black" )
label_color.pack(fill='x')
string_code_color = StringVar()
Entry(textvariable=string_code_color, justify="center", fg="black").pack(fill='x')
string_code_color.set("Color code")

for index, color_combo in enumerate(list_colors):
    ButtonRainbow(root, text=str(index+1), color= color_combo[0], color_code=color_combo[1], color_code_var=string_code_color, label=label_color)

root.mainloop()
