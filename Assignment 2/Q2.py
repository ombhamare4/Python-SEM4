#Om Ghansyam Bhamare Div A Roll No:3
#A Python program to append data to an existing file and then displaying the entire file.

file1= open("D:\\Om\\OM BHAMARE\\COLLEGE\\2nd Year\\Sem4\\Python SEM4\\Assignment 2\\Q2.txt","a")
file1.write("Hello!")
file1.close()

file2=open("D:\\Om\\OM BHAMARE\\COLLEGE\\2nd Year\\Sem4\\Python SEM4\\Assignment 2\\Q2.txt","r")
print(file2.read())
