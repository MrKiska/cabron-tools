# just a launcher and arguments preparing for main.py

import Packages.ExamplePackage.main as mainPy
import os
import json

root = os.getcwd()

moduleRoot = root + "/Packages/ExamplePackage/"

with open(moduleRoot+"info.json") as f:
    moduleInfo = list(json.load(f).items())

print(moduleInfo)

mainPy.onStart

while True:
    mainPy.main