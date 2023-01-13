packageInternalName = ""


from importlib.machinery import SourceFileLoader
import os
pkgRoot = os.getcwd + "/Packages/" + packageInternalName

mainFile = SourceFileLoader("main",pkgRoot+"/main.py").load_module()