import tkinter as tk
import psutil
from time import strftime

def update_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    if plugged:
        status = f"{percent}% ⚡ Charging"
    else:
        status = f"{percent}% 🔋 Not Charging"

    if percent >= 60:
        color = "green"
    elif percent >= 40:
        color = "orange"
    else:
        color = "red"

    battery_label.config(text=status, fg=color)
    root.after(10000, update_battery)

def update_clock():
    time_string = strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    clock_label.config(text=time_string)
    root.after(1000, update_clock)

# GUI setup
root = tk.Tk()
root.title("Clock + Battery Widget")
root.geometry("600x400")
root.configure(bg="black")
root.resizable(False, False)
#root.attributes("-topmost", True)

# Clock label
clock_label = tk.Label(
    root,
    font=("Arial", 80),
    fg="dark blue",
    bg="black"
)
clock_label.pack(pady=(40, 10))

# Battery label
battery_label = tk.Label(
    root,
    font=("Arial", 40),
    bg="black"
)
battery_label.pack(pady=(0, 30))

# Start updates
update_clock()
update_battery()

root.mainloop()
