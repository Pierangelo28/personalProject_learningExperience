# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
root = tk.Tk()
root.title("first graphic project")
root.geometry("500x500")

label = tk.Label(root, text = "first calculator")
label.grid(row = 0, column=0 , columnspan= 5, pady=20)
# button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked"))
# button.pack(pady=10)

calculation_result = tk.Text(root,height=2, width=30, font = ("Arial",24))
calculation_result.grid(row = 0, column= 0, columnspan= 10, pady=(10,10), padx=30)
calculation =""

def calculate(symbol):
    global calculation
    calculation += symbol
    calculation_result.delete("1.0", tk.END)
    calculation_result.insert("1.0", calculation)
def evaluate():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        calculation_result.delete("1.0", tk.END)
        calculation_result.insert("1.0", result)
    except:
        clear()
        calculation_result.insert("1.0", "Error")
        pass

def clear():
    global calculation
    calculation = ""
    calculation_result.delete("1.0", tk.END)

Btn_1 = tk.Button(root, text="1", command=lambda: calculate("1"), width=5, font=("Arial",12))
Btn_1.grid(row=1, column=0, pady=5, padx=5)

Btn_2 = tk.Button(root, text="2", command=lambda: calculate("2"), width=5, font=("Arial",12))
Btn_2.grid(row=1, column=1, pady=5, padx=5)

Btn_3 = tk.Button(root, text="3", command=lambda: calculate("3"), width=5, font=("Arial",12))
Btn_3.grid(row=1, column=2, pady=5, padx=5)

Btn_4 = tk.Button(root, text="4", command=lambda: calculate("4"), width=5, font=("Arial",12))
Btn_4.grid(row=2, column=0, pady=5, padx=5)

Btn_5 = tk.Button(root, text="5", command=lambda: calculate("5"), width=5, font=("Arial",12))
Btn_5.grid(row=2, column=1, pady=5, padx=5)

Btn_6 = tk.Button(root, text="6", command=lambda: calculate("6"), width=5, font=("Arial",12))
Btn_6.grid(row=2, column=2, pady=5, padx=5)

Btn_7 = tk.Button(root, text="7", command=lambda: calculate("7"), width=5, font=("Arial",12))
Btn_7.grid(row=3, column=0, pady=5, padx=5)

Btn_8 = tk.Button(root, text="8", command=lambda: calculate("8"), width=5, font=("Arial",12))
Btn_8.grid(row=3, column=1, pady=5, padx=5)

Btn_9 = tk.Button(root, text="9", command=lambda: calculate("9"), width=5, font=("Arial",12))
Btn_9.grid(row=3, column=2, pady=5, padx=5)

# Optional: Button 0, operators, = and Clear
Btn_0 = tk.Button(root, text="0", command=lambda: calculate("0"), width=5, font=("Arial",12))
Btn_0.grid(row=4, column=1, pady=5, padx=5)
Btn_plus = tk.Button(root, text="+", command=lambda: calculate("+"), width=5, font=("Arial",12))
Btn_plus.grid(row=1, column=3, pady=5, padx=5)

Btn_minus = tk.Button(root, text="-", command=lambda: calculate("-"), width=5, font=("Arial",12))
Btn_minus.grid(row=2, column=3, pady=5, padx=5)

Btn_multiply = tk.Button(root, text="*", command=lambda: calculate("*"), width=5, font=("Arial",12))
Btn_multiply.grid(row=3, column=3, pady=5, padx=5)

Btn_divide = tk.Button(root, text="/", command=lambda: calculate("/"), width=5, font=("Arial",12))
Btn_divide.grid(row=4, column=3, pady=5, padx=5)

Btn_equal = tk.Button(root, text="=", command=evaluate, width=5, font=("Arial",12))
Btn_equal.grid(row=4, column=2, pady=5, padx=5)

Btn_clear = tk.Button(root, text="C", command=clear, width=5, font=("Arial",12))
Btn_clear.grid(row=4, column=0, pady=5, padx=5)

root.mainloop()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
