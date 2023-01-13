import os

textList = []

root = os.getcwd()

with open(root + "/Packages/Empire/Oxxxymiron-Empire.txt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        textList.append(line) #storing everything in memory!
print("press enter to continue, q to exit\n")
for i in range(0,int(len(textList)/2)):
    print(textList[i*2])
    print(textList[i*2+1])
    if input()=="q":
        break