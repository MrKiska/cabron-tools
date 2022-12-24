import json
import os

root = os.getcwd()

pkg = input("choose package")
pkgListFile = open(root +"/Launcher/pkgList.json")



with pkgListFile as f:
    pkgList = list(json.load(f).items())

cc = "Cabron_checker"

__import__(cc+".entry")