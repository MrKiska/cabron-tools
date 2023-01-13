from importlib.machinery import SourceFileLoader
import time
import os
import importlib
import lib.voter


print("\nInitializing mierda checker v0.1.34-13-12-2022...")
time.sleep(2)


namesList = []

opts = [
    [
        "Language",
        [
            "english",
            "russian"
        ]
    ],
    [
        "Use animations?",
        [
            "yes",
            "no"
        ]
    ],
    [
        "Choose names source",
        [
            "manually enter list",
            "give path to file (or drag and drop it to terminal)"
        ]
    ]
]

choices = lib.voter.askForOptions(opts)


if int(choices[2]) == 0 or choices[2] == "":
    print("enter names. To finsh list, enter empty string")
    while True:
        inp = input(str(len(namesList))+":")
        if inp=="":break
        namesList.append(inp)
else:
    print("enter path or drop file")
    namePath = input(":").replace("'","")
    print(namePath)
    fileobj=open(namePath)
    namesList=fileobj.read().split('\n')

if choices[1]==1:
    anim = True
else:
    anim = False



import Packages.Cabron_checker.main as mainPy

mainPy.main(
    anim = anim,
    names = namesList,
    first = "jabroni",
    second = "not jabroni",
    )
