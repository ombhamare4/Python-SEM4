#Om Ghanshyam Bhamare SE A 3
#Assignmet 3 
#Q4.A Python program to remove a sub directory that is inside another dictionary
import os

file1 = 'Q4_1.txt'
loc = "D:\\Om\\OM BHAMARE\\COLLEGE\\2nd Year\\Sem4\\Python SEM4\\Assignment 2"
path = os.path.join(loc,file1)
os.remove(path)
