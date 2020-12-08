# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 00:15:02 2020

@author: Frostmoon
"""
# Advent of Code Day 2:
# Password validation checker: given a list of passwords and criteria,
# test each password to see if it meets its corresponding criteria and
# return the number of valid passwords

testlist = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

def file_read():
    result = []
    with open("E:/Users/Administrator/Downloads/Advent of Code 2020/D2input.txt", "r") as text:
        for l in text:
            result.append(l.strip())
    return result

def pword_check1(actuallist): # Day 2 Part 1
    vpcount = 0
    for i in range(0, len(actuallist)):
        lettercount = 0
        bounds_str, letter, password = actuallist[i].split()
        letter = letter.strip(":")
        lb, ub = bounds_str.split("-")
        lb, ub = int(lb), int(ub)
        for j in password:
            if j == letter:
                lettercount += 1
        if lettercount >= lb and lettercount <= ub:
            vpcount += 1
    print("Number of valid passwords: %d" % vpcount)
    
def pword_check2(actuallist): # Day 2 Part 2
    vpcount = 0
    for i in range(0, len(actuallist)):
        indexpositions, letter, password = actuallist[i].split()
        letter = letter.strip(":")
        p1, p2 = indexpositions.split("-")
        p1, p2 = int(p1) - 1, int(p2) - 1
        if (password[p1] != letter and password[p2] != letter) or (password[p1] == letter and password[p2] == letter):
            continue
        else:
            vpcount += 1
    print("Number of valid passwords: %d" % vpcount)
    
actuallist = file_read()
#print(actuallist)
#pword_check1(actuallist)
#pword_check2(actuallist)