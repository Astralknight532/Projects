# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 18:21:24 2020

@author: Frostmoon

Advent of Code 2020 Day 5
Seat positions are indicated with binary space partitioning.
128 rows of seats on the plane numbered 0 to 127 (front to back). 
First 7 characters will be a combination of "F" and "B" specifying 
which half of a region the seat's in.
Example:
    FBFBBFFRLR
    1st character is F - seat is in front half of the 128 rows (rows 0 - 63)
    2nd is B - seat is in back half of rows 0 - 63 (rows 32 - 63)
    3rd is F - front half of rows 32 - 63 (rows 32 - 47)
    4th is B - back half of rows 32 - 47 (rows 40 - 47)
    5th is B - back half of rows 40 - 47 (rows 44 - 47)
    6th is F - front half of rows 44 - 47 (rows 44 - 45)
    7th is F - front half of rows 44 - 45 (row 44)
    RLR indicates the column that the seat is in (columns 0 to 7)
    R - upper half of columns 0 - 7 (columns 4 - 7)
    L - lower half of columns 4 - 7 (columns 4 - 5)
    R - upper half of columns 4 - 5 (column 5)
    Therefore the seat described by FBFBBFFRLR is in row 44 column 5.
    Formula for calculating seat ID: seatRow * 8 + seatCol = seatID
    In the case of row 44 column 5, the seatID is 44 * 8 + 5 = 357.
    Other examples:
        BFFFBBFRRR - row 70, col 7, seatID 567
        FFFBBBFRRR - row 14, col 7, seatID 119
        BBFFBBFRLL - row 102, col 4, seatID 820
With this info, find the highest seatID in the list of given seats.
"""
"""
def file_read():
    result = []
    with open("E:/Users/Administrator/Downloads/Advent of Code 2020/D5input.txt", "r") as text:
        for l in text:
            result.append(l.strip())
    return result

def rowFind(seatPosition, row_lb, row_ub):
    row = 0
    i = 0
    while seatPosition != " ":
        if seatPosition[i] == "F":
            i += 1
            rowFind(seatPosition[i:], row_lb, row_ub / 2)
        else:
            i += 1
            rowFind(seatPosition[i:], row_lb / 2, row_ub)
    
    for i in range(0, len(seatPosition)):
        if seatPosition[i] == "F":
            rowFind(seatPosition[i:], row_lb, row_ub / 2)
        else:
            rowFind(seatPosition[i:], row_lb / 2, row_ub)
    return 0

def colFind(seatPosition, col_lb, col_ub):
    col = 0
    
    
    
    return col

def getSeatID(row, col):
    return row * 8 + col
    
def findLargestID(seatList):
    highestID = 0
    seatPositionList = []
    for i in range(0, len(seatList)):
        for j in range(0, len(seatList[i] - 3)):
            lowerRow, upperRow = 0, 0
            if seatList[i].charAt(j) == "F":
                lowerRow, upperRow = 0, 63
                rowFind(seatList[i][1:7], lowerRow, upperRow)
            else:
                lowerRow, upperRow = 64, 127
                rowFind(seatList[i][1:7], lowerRow, upperRow)
        for k in range(len(seatList[i]) - 3, len(seatList[i])):
            lowerCol, upperCol = 0, 0
                            
    return highestID

seatList = file_read()
#print(seatList)
#print(len(seatList))
highestSeatID = findLargestID(seatList)
print(highestSeatID)
"""
fileinput = open("E:/Users/Administrator/Downloads/Advent of Code 2020/D5input.txt")

# Part 1 - find the highest possible seatID
t = str.maketrans("FBLR", "0101")
s = set(int(l.translate(t), 2) for l in fileinput)
low, high = min(s), max(s)
print("Highest possible seatID: %d" % high)

# Part 2 - find your seatID
yourSeatID = (next(i for i in range(low + 1, high) if i not in s))
print("Your seatID: %d" % yourSeatID)
