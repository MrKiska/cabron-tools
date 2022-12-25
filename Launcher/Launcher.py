import importlib
import json
import os

root = os.getcwd()


pkgListFile = open(root +"/Launcher/pkgList.json")



with pkgListFile as f:
    pkgList = list(json.load(f).items())



for pkg in pkgList:
    print(pkg[0],"-",pkg[1]['title'])



pkgChosen = int(input("choose package"))
pkgPath = pkgList[pkgChosen-1][1]['initPath']

pkgImport = pkgPath

print(pkgImport)

importlib.import_module(pkgImport)