import tkinter as tk

def show_input():
    name = name_input.get()
    date = date_input.get()
    output_label.config(text="Name: " + name + "\nDate: " + date)

root = tk.Tk()
root.title("Input Fields")

# create name input field
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)

name_input = tk.Entry(root)
name_input.grid(row=0, column=1)

# create date input field
date_label = tk.Label(root, text="Date:")
date_label.grid(row=1, column=0)

date_input = tk.Entry(root)
date_input.grid(row=1, column=1)

# create button to show input values
show_button = tk.Button(root, text="Show Input", command=show_input)
show_button.grid(row=2, column=1)

# create label to show output
output_label = tk.Label(root, text="")
output_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
