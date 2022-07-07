from tkinter import *

win = Tk()
win.title("Calc")
win.geometry('300x430')

e = Entry(win, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define an event to close the window
def close_win(e):
    win.destroy()

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def key_type(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def c_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def k_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

def enter_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def k_minus():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def k_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def k_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

button_1 = Button(win, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(win, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(win, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(win, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(win, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(win, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(win, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(win, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(win, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(win, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add = Button(win, text="+", padx=39, pady=20, command=button_add)
button_minus = Button(win, text="-", padx=42, pady=20, command=button_minus)

button_multiply = Button(win, text="*", padx=41, pady=20, command=button_multiply)
button_divide = Button(win, text="/", padx=42, pady=20, command=button_divide)

button_equal = Button(win, text="=", padx=143, pady=20, command=button_equal)
button_clear = Button(win, text="Clr", padx=36, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=5, column=0)

button_add.grid(row=5, column=1)
button_minus.grid(row=5, column=2)

button_equal.grid(row=7, column=0, columnspan=3)
button_clear.grid(row=6, column=2, columnspan=2)

button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=0)

# Bind the C key with the callback function
win.bind('<c>', lambda e: close_win(e))

# Bind the ESC key with the callback function
win.bind('<Escape>', lambda e: c_clear())

# Bind the + key with the callback function
win.bind('+', lambda e: k_add())

# Bind the return key with the callback function
win.bind('<Return>', lambda e: enter_equal())

# Bind the - key with the callback function
win.bind('-', lambda e: k_minus())

# Bind the * key with the callback function
win.bind('*', lambda e: k_multiply())

# Bind the / key with the callback function
win.bind('/', lambda e: k_divide())

# Bind the 1 key with the callback function
win.bind('1', lambda e: key_type(1))

# Bind the 2 key with the callback function
win.bind('2', lambda e: key_type(2))

# Bind the 3 key with the callback function
win.bind('3', lambda e: key_type(3))

# Bind the 4 key with the callback function
win.bind('4', lambda e: key_type(4))

# Bind the 5 key with the callback function
win.bind('5', lambda e: key_type(5))

# Bind the 6 key with the callback function
win.bind('6', lambda e: key_type(6))

# Bind the 7 key with the callback function
win.bind('7', lambda e: key_type(7))

# Bind the 8 key with the callback function
win.bind('8', lambda e: key_type(8))

# Bind the 9 key with the callback function
win.bind('9', lambda e: key_type(9))

# Bind the 0 key with the callback function
win.bind('0', lambda e: key_type(0))

win.mainloop()
