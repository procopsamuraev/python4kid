import tkinter as tk

def change_label_text():
    """Updates the StringVar's value, which automatically updates the label."""
    # Use the .set() method to change the variable's value
    my_var.set("Text updated after button click!")

# --- Main application setup ---
root = tk.Tk()
root.title("StringVar Label Example")

# 1. Create the StringVar instance
my_var = tk.StringVar(value="Initial label text") # Optional initial value

# 2. Create the Label, linking it with the 'textvariable' option
# Use textvariable=my_var, NOT text=my_var
label = tk.Label(root, textvariable=my_var, font=("Helvetica", 12))
label.pack(pady=20) # Use a geometry manager like pack or grid

# 3. Create a Button to trigger the text change
button = tk.Button(root, text="Click to Update Label", command=change_label_text)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()