import importlib
import json
import os
import sys
from lib.voter import askForOptions

root = os.getcwd()


pkgListFile = open(root +"/Launcher/pkgList.json")
greeting = open(root + "/resources/greeting.txt").read()

packages = os.listdir("Packages")
print(packages)
pkgsInfo = []

for i in range(0,len(packages)):
    inf = "Packages/"+packages[i]+"/info.json"
    if os.path.exists(inf):
        with open(inf) as f:
            moduleInfo = list(json.load(f).items())
        pkgsInfo.append(moduleInfo)
    else:
        continue

def showPackages():
    for i in range(0,len(pkgsInfo)):
        info = [
            str(i) + " - " + pkgsInfo[i][0][1], # name of package
            "  * " + pkgsInfo[i][1][1]
        ]
        print("\n".join(info)+"\n")

def packageWrapper(pkgIndex):
    __import__(pkgsInfo[pkgIndex][3][1])
    sys.modules.pop(pkgsInfo[pkgIndex][3][1])

def processCommand(cmd: str):
    cmd = cmd.split(" ")
    if cmd[0] == "use":
        packageWrapper(int(cmd[1]))

    elif cmd[0] == "search":
        searchRes = searchPkg(cmd[0])
        print("not implemented")
    elif cmd[0] == "help":
        print(
            "commands:\n help\n use <pkgIndex>"
        )
    elif cmd[0] == "q":
        exit()

def searchPkg(query):
    pass

while True:
    try:

        print(greeting)
        showPackages()
        command = input(":")

        processCommand(command)





    except KeyboardInterrupt:
        print("exit")