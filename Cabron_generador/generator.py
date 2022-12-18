from random import randint


first = open("first.txt").read().split('\n')
second = open("second.txt").read().split('\n')
third = open("third.txt").read().split('\n')

while True:
    if input()=="":
        name=[]
        name.append(first[randint(0,len(first))-1])
        name.append(second[randint(0,len(second)-1)])
        name.append(third[randint(0,len(third)-1)])
        print(str(name))
        