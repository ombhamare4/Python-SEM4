#Om Ghansyam Bhamare SE A 3
# Assignment 2 
#Q1 A Python program to copy an 
# image file into another file.
file1 = open('jett.jpg','rb')

file2 = open('newjett.jpg','wb')

for line in file1:
    file2.write(line)