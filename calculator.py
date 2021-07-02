# This is my Calculator project
from tkinter import *

mainWindow = Tk()
mainWindow.title('Calculator')
screen = Entry(mainWindow, width=35, borderwidth=5, fg='white', bg='black')
screen.grid(row=0, column=0, columnspan=4)


# Place numbers on screen
def press_btn(num):
    now = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(now) + str(num))


# Clear the screen
def clear():
    screen.delete(0, END)


# This will Add
def add():
    global fd
    global choice
    first_digit = screen.get()
    choice = 'add'
    fd = float(first_digit)
    screen.delete(0, END)


# This will Subtract
def subtract():
    global fd
    global choice
    first_digit = screen.get()
    choice = 'subtract'
    fd = float(first_digit)
    screen.delete(0, END)


# This will Divide
def divide():
    global fd
    global choice
    first_digit = screen.get()
    choice = 'divide'
    fd = float(first_digit)
    screen.delete(0, END)


# This will Multiply
def multiply():
    global fd
    global choice
    first_digit = screen.get()
    choice = 'multiply'
    fd = float(first_digit)
    screen.delete(0, END)


# This will do the math
def equal():
    second_digit = screen.get()
    screen.delete(0, END)
    if choice == 'add':
        screen.insert(0, fd + float(second_digit))
    if choice == 'subtract':
        screen.insert(0, fd - float(second_digit))
    if choice == 'divide':
        screen.insert(0, fd / float(second_digit))
    if choice == 'multiply':
        screen.insert(0, fd * float(second_digit))


# Calculator buttons
button_7 = Button(mainWindow, text='7', padx=42, pady=20, command=lambda: press_btn(7))
button_7.grid(row=2, column=0)
button_8 = Button(mainWindow, text='8', padx=42, pady=20, command=lambda: press_btn(8))
button_8.grid(row=2, column=1)
button_9 = Button(mainWindow, text='9', bg='blue', padx=42, pady=20, command=lambda: press_btn(9))
button_9.grid(row=2, column=2)

button_4 = Button(mainWindow, text='4', padx=42, pady=20, command=lambda: press_btn(4))
button_4.grid(row=3, column=0)
button_5 = Button(mainWindow, text='5', padx=42, pady=20, command=lambda: press_btn(5))
button_5.grid(row=3, column=1)
button_6 = Button(mainWindow, text='6', padx=42, pady=20, command=lambda: press_btn(6))
button_6.grid(row=3, column=2)

button_1 = Button(mainWindow, text='1', padx=42, pady=20, command=lambda: press_btn(1))
button_1.grid(row=4, column=0)
button_2 = Button(mainWindow, text='2', padx=42, pady=20, command=lambda: press_btn(2))
button_2.grid(row=4, column=1)
button_3 = Button(mainWindow, text='3', padx=42, pady=20, command=lambda: press_btn(3))
button_3.grid(row=4, column=2)

button_add = Button(mainWindow, text='+', padx=42, pady=20, command=add)
button_add.grid(row=1, column=3)
button_subtract = Button(mainWindow, text='-', padx=42, pady=20, command=subtract)
button_subtract.grid(row=2, column=3)
button_divide = Button(mainWindow, text='/', padx=42, pady=20, command=divide)
button_divide.grid(row=3, column=3)

button_multiply = Button(mainWindow, text='*', padx=42, pady=20, command=multiply)
button_multiply.grid(row=4, column=3)
button_zero = Button(mainWindow, text='0', padx=93, pady=20, command=lambda: press_btn(0))
button_zero.grid(row=5, column=0, columnspan=2)
button_dot = Button(mainWindow, text='.', padx=42, pady=20, command=lambda: press_btn('.'))
button_dot.grid(row=5, column=2)
button_equal = Button(mainWindow, text='=', padx=42, pady=20, command=equal)
button_equal.grid(row=5, column=3)
button_AC = Button(mainWindow, text='AC', padx=136, pady=20, command=clear)
button_AC.grid(row=1, column=0, columnspan=3)

mainWindow.mainloop()
