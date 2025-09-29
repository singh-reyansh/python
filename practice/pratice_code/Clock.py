from tkinter import *
from tkinter.ttk import *
from time import strftime

# Create the main window
root = Tk()
root.title("Digital Clock")

# Define the clock update function
def time():
    string = strftime("%I:%M:%S %p")  # Use %I for 12-hour format with AM/PM
    label.config(text=string)
    label.after(1000, time)  # Call this function again after 1000ms

# Create and style the clock label
label = Label(root, font=("Arial", 80), background="black", foreground="dark blue")
label.pack(anchor='center')

# Start the clock
time()
mainloop()
