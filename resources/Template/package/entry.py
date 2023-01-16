packageInternalName = ""


from importlib.machinery import SourceFileLoader
import os, json


pkgRoot = os.getcwd() + "/Packages/" + packageInternalName # getting root of package

with open(pkgRoot + "/info.json") as f: # getting package info
    packageJson = json.load(f).items()

mainFile = SourceFileLoader("main",pkgRoot+"/main.py").load_module()

# there are preparings before start of main script

mainFile.main(packageInternalName = packageInternalName) # loads main script

# something to do after exec