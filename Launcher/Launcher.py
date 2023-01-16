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

packages = os.listdir("Packages")
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
            str(i) + " - " + pkgsInfo[i][0][1],
            "  * " + pkgsInfo[i][1][1]
        ]
        print("\n".join(info)+"\n")
        if i>=limit:
            print("and "+str(pkgN-i)+" more")
            print("use search or enter index")
            return

def packageWrapper(pkgIndex):
    try:
        __import__(pkgsInfo[pkgIndex][3][1])
        sys.modules.pop(pkgsInfo[pkgIndex][3][1])
    except IndexError:
        print("there is no requested package")

def processCommand(cmd: str):
    cmd = cmd.split(" ")
    if cmd[0] == "use" and len(cmd)>1:
        packageWrapper(int(cmd[1]))

    elif cmd[0] == "search":
        searchPkg(cmd[1:])

    elif cmd[0] == "help":
        showHelp()

    elif cmd[0] == "createpkg":
        from resources.Template.createTemplatePackage import main as mkpkg
        mkpkg()

    elif cmd[0] == "show":
        if len(cmd)>1:
            try:
                amount = int(cmd[1])
            except ValueError:
                amount = 5
        else:
            amount = 5
        showPackages(amount)

    elif cmd[0] in ["q","exit"]:
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

def makePackageDialogue():
    print("Package creating wizard")

def showMOTD():
    greetingfile = open(root + "/resources/greeting.txt")
    greetingmsg = greetingfile.read()
    greetingfile.close()
    print(greetingmsg)

def showHelp():
    helpfile = open(root + "/resources/help.txt")
    helpmsg = helpfile.read()
    helpfile.close()
    print(helpmsg)


launchArgs = sys.argv

if len(launchArgs)>1:
    
    for arg in launchArgs:

        if str(arg[0:3]) == "cmd":
            command = arg[4:]
            print(command)
            processCommand(command)
            sys.exit()

showMOTD()
showPackages(2)

while True:
    try:
        command = input(":")

        processCommand(command)

    except KeyboardInterrupt:
        print("\nbreak. type exit to exit")