import random
print("Весёлый квиз!")
file1 = open("q1.txt","r")
file2 = open("q2.txt","r")
file3 = open("q3.txt","r")
file4 = open("superQ.txt","r")
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