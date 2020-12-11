# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:59:57 2020

@author: Frostmoon
def isValid(passport):
   required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
   if passport.keys() not in required:
       return False
   else:
       return True

passportList = []
line_dict = {}
vpcounter = 0
with open("E:/Users/Administrator/Downloads/Advent of Code 2020/D4input.txt", "r") as f:
    for l in f:
        l = l.strip().split()
        #print(l)
        for i in l:
            k, v = i.split(":")
            line_dict[k] = v
            #passportList.append(line_dict)
            #print(k, v)
            print(line_dict)
            #continue
        #print(line_dict)
        #passportList.append(line_dict)
        #print(line_dict)
        #print(len(line_dict))
    #print(passportList)
   #print(passportList)
"""
import re
fileinput = open("E:/Users/Administrator/Downloads/Advent of Code 2020/D4input.txt").read().split("\n\n") 

# Part 1 - valid passports are required to have all fields except cid
#print(sum([all(nf in [f.split(":")[0] for f in l.replace("\n", " ").split(" ")] for nf in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]) for l in fileinput]))

# Part 2 - more strict passport requirements to be considered valid
"""
New requirements:
1. cid is still optional
2. birth year (byr) must be 4 digits long & within the range 1920-2002
3. issue year (iyr) must be 4 digits long & within the range 2010-2020
4. expiration year (eyr) must be 4 digits long & within the range 2020-2030
5. height (hgt) must be a number followed by either cm or in
    5.1 if the units are cm, height must be within the range 150-193
    5.2 if the units are in, height must be within the range 59-76
6. hair color (hcl) must be in this format: # followed by 6 characters of 0-9, a-f
7. eye color (ecl) must be 1 of these: amb, blu, brn, gry, grn, hzl, oth
8. passport id (pid) must be a 9-digit number, including leading zeroes
"""

def hval(s):
    if len(s) >= 4:
         m = ( ( s[-2:]=="in") & (59<=int(s[:-2])<=76) ) |\
        ((s[-2:]=="cm") & (150<=int(s[:-2])<=193))
    else:
        m = False
    return m

def pval(p):
    pd = dict(item.split(":") for item in p if len(item) > 1)
    if all(key in pd.keys() for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
        return all([1920 <= int(pd["byr"]) <= 2002, 
                    2010 <= int(pd["iyr"]) <= 2020,
                    2020 <= int(pd["eyr"]) <= 2030,
                    bool(re.match("^#[0-9a-f]{6}$", pd["hcl"])),
                    pd["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                    bool(re.match("^[0-9]{9}$", pd["pid"])),
                    hval(pd["hgt"])
                   ])
    else:
        return False

print(sum([pval(p) for p in [l.replace("\n", " ").split(" ") for l in fileinput]]))