import os
import random
print("Весёлый квиз!")
root = os.getcwd()+"/Packages/voprosnick/"
file1 = open((root+"q1.txt"),"r")
file2 = open((root+"q2.txt"),"r")
file3 = open(root+"q3.txt","r")
file4 = open(root+"superQ.txt","r")
n1 = random.randint(1,100)
if (n1>=1 and n1<=30):
    print(file1.read()) 
elif (n1>=30 and n1<=60):
    print(file2.read())
elif (n1>=60 and n1<=90):
    print(file3.read())
elif (n1>=90):
    print(file4.read())
file1.close()
file2.close()
file3.close()
file4.close()
print (n1)