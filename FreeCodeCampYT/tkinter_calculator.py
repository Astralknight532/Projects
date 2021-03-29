# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:27:55 2020

@author: Frostmoon
"""

# Using tkinter to make a GUI for a calculator
import tkinter as tk
import tkinter.ttk as ttk 

win = tk.Tk()
win.title("Calculator")

# Method 1 for controlling the window's attributes
#win.configure(width = 300, height = 300, background = 'red')

# Method 2 for controlling the window's attributes
#win.geometry('300x300+500+200') # the addition signs let you change where the window appears onscreen

# Note: buttons & labels have to be packed, and the order in which they're
# packed will affect the order that they appear onscreen
#label = ttk.Label(win, text = "Hello World")
#button = ttk.Button(win, text = "Hello")
#label.pack()
#button.pack()

# Empty string to store the entered expression
expression = ""

# tkinter String object to be used as a cursor for the calculator
text = tk.StringVar()

# function to detect key presses -> use the command argument to link buttons & functions
def press(num):
    global expression
    expression += str(num)
    text.set(expression)

# function to clear the expression for "C"
def clr():
    global expression
    expression = ""
    text.set(expression)

# function to do the equals operation for "="
def equal():
    global expression
    ttl = str(eval(expression))
    text.set(ttl)

# Entry bar for the calculator, justify changes the justification of text, sticky stretches an item in all 4 directions
entry = ttk.Entry(win, justify = "right", textvariable = text)
entry.grid(row = 0, columnspan = 4, sticky = "nsew")

# Row 1 of calculator keys
button7 = ttk.Button(win, text = "7", command = lambda:press(7)) # 7
button7.grid(row = 1, column = 0)

button8 = ttk.Button(win, text = "8", command = lambda:press(8)) # 8
button8.grid(row = 1, column = 1)

button9 = ttk.Button(win, text = "9", command = lambda:press(9)) # 9
button9.grid(row = 1, column = 2)

button_divide = ttk.Button(win, text = "/", command = lambda:press("/")) # division
button_divide.grid(row = 1, column = 3)

# Row 2 of calculator keys
button4 = ttk.Button(win, text = "4", command = lambda:press(4)) # 4
button4.grid(row = 2, column = 0)

button5 = ttk.Button(win, text = "5", command = lambda:press(5)) # 5
button5.grid(row = 2, column = 1)

button6 = ttk.Button(win, text = "6", command = lambda:press(6)) # 6
button6.grid(row = 2, column = 2)

button_multiply = ttk.Button(win, text = "*", command = lambda:press("*")) # multiplication
button_multiply.grid(row = 2, column = 3)

# Row 3 of calculator keys
button1 = ttk.Button(win, text = "1", command = lambda:press(1)) # 1
button1.grid(row = 3, column = 0)

button2 = ttk.Button(win, text = "2", command = lambda:press(2)) # 2
button2.grid(row = 3, column = 1)

button3 = ttk.Button(win, text = "3", command = lambda:press(3)) # 3
button3.grid(row = 3, column = 2)

button_subtract = ttk.Button(win, text = "-", command = lambda:press("-")) # subtraction
button_subtract.grid(row = 3, column = 3)

# Row 4 of calculator keys
button0 = ttk.Button(win, text = "0", command = lambda:press(0)) # 0
button0.grid(row = 4, column = 0)

button_decimal = ttk.Button(win, text = ".", command = lambda:press(".")) # decimal
button_decimal.grid(row = 4, column = 1)

button_clear = ttk.Button(win, text = "C", command = clr) # clear
button_clear.grid(row = 4, column = 2)

button_add = ttk.Button(win, text = "+", command = lambda:press("+")) # addition
button_add.grid(row = 4, column = 3)

# Row 5 of calculator keys (since there's only 1 button, we make it take up all 4 columns)
button_equals = ttk.Button(win, text = "=", command = equal) # equals
button_equals.grid(row = 5, columnspan = 4, sticky = "nsew")

win.mainloop()