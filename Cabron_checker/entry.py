from importlib.machinery import SourceFileLoader
import time
import os
import importlib
import lib.voter

print(os.getcwd())

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


if choices[2] == 1:
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




mainPy = SourceFileLoader("main",os.getcwd()+"/Cabron_checker/main.py").load_module()

mainPy.main(
    anim = anim,
    names = namesList,
    first = "jabroni",
    second = "not jabroni",
    )
