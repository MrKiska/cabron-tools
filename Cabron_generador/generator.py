from random import randint


first = open("first.txt").read().split('\n')
second = open("second.txt").read().split('\n')
third = open("third.txt").read().split('\n')

fem = ["а","ь","я"]
gay = ["е","о"]

print("max: "+ str(len(first)*len(second)*len(third)))
print("press enter")
while True:
    if input()=="":
        name=[]
        name.append(first[randint(0,len(first))-1])
        name.append(second[randint(0,len(second)-1)])
        name.append(third[randint(0,len(third)-1)])
        if name[1][-1:] in fem:
            name[0] = name[0][:-2]+"ая"
        elif name[1][-1:] in gay:
            name[0] = name[0][:-2]+"ое"


        print(" ".join(str(i) for i in name))
        