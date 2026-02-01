# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk

root = tk.Tk()
root.title("unit_converter")
root.geometry("500x500")

# from_field = tk.Text(root, height=5, width=20, font=("Arial", 12))
# from_field.grid(row=0, column=0,)
# to_field = tk.Text(root, height=5, width=20, font=("Arial", 12))
# to_field.grid(row=0, column=2)
# connecting_Box = tk.Label(root, text = "=", font=("Arial", 12))
# connecting_Box.grid(row=0, column=1)
top_frame = tk.Frame(root)
top_frame.grid(row=0, column=0, columnspan=4)

from_field = tk.Text(top_frame, height=5, width=30, font=("Arial", 12))
from_field.grid(row=0, column=0)

connecting_Box = tk.Label(top_frame, text="=", font=("Arial", 12))
connecting_Box.grid(row=0, column=1)

to_field = tk.Text(top_frame, height=5, width=30, font=("Arial", 12))
to_field.grid(row=0, column=2)


unit = ""
command = ""
def convert(value):
    global unit
    unit += value
    from_field.delete("1.0",tk.END )
    from_field.insert("1.0",unit)

def cm_to_m (symbol):
    return int(symbol) / 100
def m_to_cm(symbol):
    return int(symbol) * 100

conversion_list = [cm_to_m, m_to_cm]
def conversion():
    global unit
    result =""
    for conversion_func in conversion_list:
        if command == conversion_func.__name__:
            result = conversion_func(unit)
            break
    to_field.delete("1.0",tk.END)
    to_field.insert("1.0", result)

def set_command(name):
    global command
    command = name
    conversion()


def clear_boxes ():
    global unit
    unit =""
    from_field.delete("1.0", tk.END)
    to_field.delete("1.0", tk.END)


# button that chooses conversion goal centimeter_button
# centimeter_button = tk.Button(root, text = "cm to m", command = lambda:conversion(), width=5, font=("Arial", 12))
Btn_1 = tk.Button(root, text="1", command=lambda: convert("1"), width=5, font=("Arial", 12))
# Btn_1.grid(row=1, column=0, pady=5, padx=5)
Btn_1.grid(row=1, column=0)

Btn_2 = tk.Button(root, text="2", command=lambda: convert("2"), width=5, font=("Arial", 12))
Btn_2.grid(row=1, column=1)

Btn_3 = tk.Button(root, text="3", command=lambda: convert("3"), width=5, font=("Arial", 12))
Btn_3.grid(row=1, column=2)

Btn_4 = tk.Button(root, text="4", command=lambda: convert("4"), width=5, font=("Arial", 12))
Btn_4.grid(row=2, column=0)

Btn_5 = tk.Button(root, text="5", command=lambda: convert("5"), width=5, font=("Arial", 12))
Btn_5.grid(row=2, column=1)

Btn_6 = tk.Button(root, text="6", command=lambda: convert("6"), width=5, font=("Arial", 12))
Btn_6.grid(row=2, column=2)

Btn_7 = tk.Button(root, text="7", command=lambda: convert("7"), width=5, font=("Arial", 12))
Btn_7.grid(row=3, column=0)

Btn_8 = tk.Button(root, text="8", command=lambda: convert("8"), width=5, font=("Arial", 12))
Btn_8.grid(row=3, column=1)

Btn_9 = tk.Button(root, text="9", command=lambda: convert("9"), width=5, font=("Arial", 12))
Btn_9.grid(row=3, column=2)

Btn_0 = tk.Button(root, text="0", command=lambda: convert("0"), width=5, font=("Arial", 12))
Btn_0.grid(row=4, column=1)

# Conversion buttons
centimeter_button = tk.Button(root, text="cm to m", command=lambda: set_command("cm_to_m"), width=10, font=("Arial", 12))
centimeter_button.grid(row=1, column=3)

meter_button = tk.Button(root, text="m to cm", command=lambda: set_command("m_to_cm"), width=10, font=("Arial", 12))
meter_button.grid(row=2, column=3)


clear_frame= tk.Frame(root)
clear_frame.grid(row=5,column = 0, columnspan=5, sticky = "w", padx = 45)
clear_button = tk.Button(clear_frame, text ="clear", command = lambda: clear_boxes(), width=30, font =("Arial", 12))
clear_button.grid(row = 5, column =0)

#  for i in conversion_list:
#     if command == i:
#       result = conversion_list[i](symbol)





root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
