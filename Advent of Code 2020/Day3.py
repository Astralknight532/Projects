# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:15:31 2020

@author: Frostmoon

import numpy as np

def file_read():
    result = []
    with open("E:/Users/Administrator/Downloads/Advent of Code 2020/D3input.txt", "r") as text:
       for l in text:
           l = l.strip()
           row = [c for c in l]
           result.append(row * 32)
    return result

def display_grid(slopepath):
    for i in range(0, len(slopepath)):
        print(" ".join([c for c in slopepath[i]]), "\n")
    #for j in range(0, len(slopepath[i])):
        
slopepath = file_read()
#display_grid(slopepath)
print(len(slopepath[322]))
sp_array = np.array(slopepath)
#print(sp_array)

for i in range(0, len(slopepath)):
    for j in range(0, len(slopepath[i]), 3):
        if slopepath[i][j] == "#":
            print("Row: %d Column: %d" % (i, j))
            break
"""
"""
import math as m

def p1(data: list, slope: tuple) -> int:
    t = 0
    r, d = (3, 1)
    while d < len(data):
        if data[d][r % len(data[0])] == "#":
            t += 1
        r += slope[0]
        d += slope[1]
    return t

def p2(data: list, slopes: tuple) -> int:
    return m.prod(p1(data, slope) for slope in slopes)
    
def main():
    d = open("E:/Users/Administrator/Downloads/Advent of Code 2020/D3input.txt").read().splitlines()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    #for i in range(0, len(slopes)):
    #    print("Number of trees encountered using %s %d" % (slopes[i]), p1(d, slopes[i]))
    print(p1(d, slopes[1]))
    print(p2(d, slopes))
    
if __name__ == '__main__':
    main()
"""

# Part 1
"""
skip, position, counter, projector = 1, 3, 0, 1
with open("E:/Users/Administrator/Downloads/Advent of Code 2020/D3input.txt") as f:
    for line in f:
        line = list(line.strip())
        
        if skip < 0:
            skip -= 1
            #print((''.join(line)))
            continue
        
        if position >= len(line):
            position -= len(line)
        
        if line[position] == ".":
            line[position] = "X"
        elif line[position] == "#":    
            line[position] = "O"
            counter += 1
        
        position += 3
        #print(''.join(line))
print(counter)
"""

#Part Two
counter = 0
result = 1
for position, skip in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
    position_helper = position
    skip_helper = skip
    with open("E:/Users/Administrator/Downloads/Advent of Code 2020/D3input.txt") as f:
        for line in f:
            line = list(line.strip())
            if skip > 0:
                skip -= 1
                #print((''.join(line)))
                continue
            else:
                skip = skip_helper -1
            if position >= len(line):
                position -= len(line)
            if line[position] == ".":
               line[position] = "X"
            elif line[position] == "#":
                line[position] = "O"
                counter += 1
            position += position_helper
            #print(''.join(line))
    result *= counter
    #print(counter)
    counter = 0
print(result)