# -*- coding: utf-8 -*-

# Python code to do bulk file renaming
import os

# function to do a bulk-rename of files in a folder
def main():
    i = 1
    
    # the path to the folder containing the files you want to bulk-rename
    path = "E:/Users/Administrator/Downloads/Pictures/Powerpoint Pics/"
    
    for filename in os.listdir(path): # loop through all the files in the folder
        my_dest = "p" + str(i) + ".png" # provide the file name you want to rename each file to
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
        
if __name__ == '__main__':
    main()