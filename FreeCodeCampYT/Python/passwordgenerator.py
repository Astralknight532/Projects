# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:31:23 2022

@author: Frostmoon
"""

import random

# Making a password generator
print("Welcome to your password generator!")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789"
numberOfPasswords = int(input("How many passwords do you want to generate? "))
passwordLength = int(input("How long do the passwords need to be? "))

if numberOfPasswords == 1:
    print("\nHere is your password:")
else:
    print("\nHere are your passwords:")

for pwd in range(numberOfPasswords):
    passwords = ""
    
    for c in range(passwordLength):
        passwords += random.choice(chars)
        
    print(passwords)