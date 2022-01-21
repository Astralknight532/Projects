# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 18:04:58 2022

@author: Frostmoon
"""

import time
from tkinter import Tk, Entry, StringVar, messagebox, Button

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1
        
    print('Time to get a drink of water & go for a walk.')
    
#t = input("Enter the amount of time you want to count down in seconds: ")
#countdown(int(t))

# Countdown timer with a Tkinter GUI
root = Tk() # create a tk window
root.geometry("300x250") # set geometry of tk window
root.title("Countdown Timer") # Using title() to display a message in the message dialogue box of the title bar

# create necessary variables
hour, minute, second = StringVar(), StringVar(), StringVar()

# set the variables' default values
hour.set("00")
minute.set("00")
second.set("00")

# take input from the user via the Entry class
hourEntry = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = hour)
hourEntry.place(x = 80, y = 20)

minuteEntry = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = minute)
minuteEntry.place(x = 130, y = 20)

secondEntry = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = second)
secondEntry.place(x = 180, y = 20)

def submit():
    try: # user input validation using a temp variable
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input valid values for the time.")
    
    while temp > -1:
        mins, secs = divmod(temp, 60) # first value is temp // 60, second value is temp % 60
        
        # converting the user input (which is either in minutes or seconds) to hours (mins, secs -> hours)
        # for example, user inputs 110 minutes (which is 110 * 60, or 6600, seconds), 
        # which is 1 hour, 50 minutes, 0 seconds
        hours = 0
        if mins > 60:
            # use divmod(firstVal = temp // 60, secondVal = temp % 60)
            hours, mins = divmod(mins, 60)
        
        # use format() to store up to 2 decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        
        # update the GUI window after decrementing the temp variable each time
        root.update()
        time.sleep(1)
        
        # when the temp variable = 0, a messagebox appears with a message
        if (temp == 0):
            messagebox.showinfo("Countdown Timer", "Time's up!")
            
        # after each second, the value of the temp variable will be decremented by 1
        temp -= 1
        
# create a button widget on the GUI
btn = Button(root, text = "Set Countdown Timer", bd = '5', command = submit)
btn.place(x = 70, y = 120)

# infinite loop to run tkinter endlessly until an interrupt occurs
root.mainloop()