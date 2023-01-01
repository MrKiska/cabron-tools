import importlib
import json
import os

root = os.getcwd()


pkgListFile = open(root +"/Launcher/pkgList.json")
greeting = open(root + "/resources/greeting.txt").read()
with pkgListFile as f:
    pkgList = list(json.load(f).items())

while True:
    try:

        print(greeting)
        print( pkgsInfo)
        for i in range(0,len(pkgsInfo)):
            info = [
                str(i) + " - " + pkgsInfo[i][0][1], # name of package
                "  * " + pkgsInfo[i][1][1]
            ]
            print("\n".join(info))
        chosenPkg = input(":")

        if chosenPkg == "q":
            exit()

        if chosenPkg.isdigit():
            pkgIndex = int(chosenPkg)

        __import__(pkgsInfo[pkgIndex][3][1])
        # importlib.import_module(pkgPath)

    except KeyboardInterrupt:
        print("exit")