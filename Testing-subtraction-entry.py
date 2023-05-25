import tkinter as tk

def update_number(*args):
    try:
        number = 1 - float(entry.get())  # Perform the mathematical operation

        if number < 0:
            number_label.config(text="Invalid input: Entry cannot be greater than 1")
        else:
            number_label.config(text=str(number))  # Update the label text
    
    except ValueError:
        number_label.config(text="Invalid input")

root = tk.Tk()

entry_text = tk.StringVar()
entry_text.trace("w", update_number)  # Call update_number when the entry text changes

entry = tk.Entry(root, textvariable=entry_text)
entry.pack()

number_label = tk.Label(root, text="0")
number_label.pack()

root.mainloop()