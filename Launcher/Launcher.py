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

        for pkg in pkgList:
            print(pkg[0],"-",pkg[1]['title'])
            print("  *",pkg[1]['description'],"\n")

        print("Choose package")
        pkgChosen = int(input(":"))
        pkgPath = pkgList[pkgChosen-1][1]['initPath']

        pkgImport = pkgPath



        importlib.import_module(pkgImport)

    except KeyboardInterrupt:
        print("exit")
