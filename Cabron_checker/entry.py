from importlib.machinery import SourceFileLoader
import time
import os
import importlib
import lib.voter

print(os.getcwd())

print("\nInitializing mierda checker v0.1.34-13-12-2022...")
time.sleep(2)


print("choose names source (1 - default):")
print("1 - manually enter list")
print("2 - give path to file (or drag and drop it to terminal)")

namesList = []

opts = [
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


choice = input(":")
if choice == "": choice="1"

if choice == "1":
    print("enter names. To finsh list, enter empty string")
    while True:
        inp = input(str(len(namesList))+":")
        if inp=="":break
        namesList.append(inp)
else:
    namePath = input("enter path or drop file")
    print(namePath)
    fileobj=open(namePath)
    namesList=fileobj.read().split('\n')

print("use animation? (1 - default)\n 1 - yes\n 2 - no")
choice = input(":")
if choice == "": choice="1"

if choice == "1":
    anim = True
else:
    anim = False




mainPy = SourceFileLoader("main",os.getcwd()+"/Cabron_checker/main.py").load_module()

mainPy.main(
    anim = anim,
    names = namesList,
    first = "jabroni",
    second = "not jabroni"
    )
