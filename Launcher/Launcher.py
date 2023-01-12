# This is fucking undocumented shit, if you are more brave than smart, dive deep and try to understand what the fuck is going here
# you has been warned, so now it's on you what to do:
# run and scream
# or
# get some glasses or paths and with them try to clean this augean horse stables of this uncommented, self written shit.

import importlib
import json
import os
import sys
from lib.voter import askForOptions
from fuzzywuzzy import fuzz

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

def showPackages(limit: int):
    pkgN = len(pkgsInfo)-1
    for i in range(0,pkgN+1):
        info = [
            str(i) + " - " + pkgsInfo[i][0][1], # name of package
            "  * " + pkgsInfo[i][1][1]
        ]
        print("\n".join(info)+"\n")
        if i>=limit:
            print("and "+str(pkgN-i)+" more")
            print("use search or enter index")
            return

def packageWrapper(pkgIndex):
    __import__(pkgsInfo[pkgIndex][3][1])
    sys.modules.pop(pkgsInfo[pkgIndex][3][1])

def processCommand(cmd: str):
    cmd = cmd.split(" ")
    if cmd[0] == "use":
        packageWrapper(int(cmd[1]))

    elif cmd[0] == "search":
        searchRes = searchPkg(cmd[0])
    elif cmd[0] == "help":
        print(
            "commands:\n help\n use <pkgIndex>"
        )
    elif cmd[0] == "q":
        exit()

def searchPkg(query):
    print("search results:")
    for i in range(0,len(pkgsInfo)):
        pname = pkgsInfo[i][0][1]
        pdesc = pkgsInfo[i][1][1]
        sameness = fuzz.token_set_ratio(query,pname)
        if sameness>=25:
            ostr = "id: "+ str(i) + " name: " + pname + "\n * " + pdesc + "\n"
            print(ostr)
    cmd = input("press any key to return to launcher or enter index\n:")
    if cmd.isdigit():
        processCommand("use "+str(cmd))

while True:
    try:

        print(greeting)
        showPackages(2)

        command = input(":")

        processCommand(command)


    except KeyboardInterrupt:
        print("exit")