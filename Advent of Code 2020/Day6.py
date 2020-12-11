# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:42:29 2020

@author: Frostmoon

Advent of Code 2020 Day 6

Part 1: find the number of questions that were answered "yes"
Part 2: find the number of questions where everyone answered "yes

Customs declarations forms
26 questions labeled a to z
count the number of "yes" answers to the each of the questions per group 
and sum them

letters on the same line = 1 person's yes answers
strings of letters with no newline in-between them = answers from members of
the same group

Example:
    abc - 1 person answered "yes" to questions a, b, and c
    
    a
    b - 3 people, 1 answered "yes" to a, 1 to b, and 1 to c
    c
    
    ab - 2 people, 1 answered "yes" to a & b, the other answered "yes" to a & c
    ac
    
    a
    a - 4 people, each answered "yes" to a
    a
    a
    
    b - 1 person, answered "yes" to b
    
Duplicate answers for a question still count as 1 question with a "yes" answer
since we're looking for the questions that got a "yes" answer, not how many
"yes" answers each question got.

Therefore sum of the number of questions that got a "yes" answer in the above 
example are:
    group 1: 3 (questions a,b, and c)
    group 2: 3 (questions a, b, and c)
    group 3: 3 (questions a, b, and c)
    group 4: 1 (question a)
    group 5: 1 (question b)
    
    sum: 11 <- find this number given the input file for Part 1 
"""

with open("E:/Users/Administrator/Downloads/Advent of Code 2020/D6input.txt", "r") as f:
    input = f.read().strip().split("\n\n")
    
def yesAnswers(input, fcn):
    for group in input:
        yield len(fcn(*(set(s) for s in group)))
        
input = [line.split() for line in input]

print("Part 1: %d questions where anyone gave a \"yes\" answer" % sum(yesAnswers(input, set.union)))
print("Part 2: %d questions where everyone gave a \"yes\" answer" % sum(yesAnswers(input, set.intersection)))
