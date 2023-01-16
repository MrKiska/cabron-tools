# with dialogue
from os import getcwd, mkdir
from shutil import copyfile
import io

def main():
    while True:
        inName = input("enter internal package name (without spaces)\n:").replace(" ","_").replace(".","_")
        norName = input("enter package normal name\n:")
        desc = input("enter package description\n:")
        version = input("enter package version\n:")
        print("Is this right?")
        print("short name:....",inName)
        print("full name:.....",norName)
        print("description:...",desc)
        print("version:.......",version)
        if input("if right, press enter, else type something") == "":
            break

    root = getcwd()
    newPackageRoot = root + "/Packages/" + inName

    mkdir(newPackageRoot)
    print("created directory")

    copyfile(root + "/resources/Template/package/entry.py",newPackageRoot + "/entry.py")
    print("copied entry script")
    copyfile(root + "/resources/Template/package/main.py",newPackageRoot + "/main.py")
    print("copied main script")

    with io.open(newPackageRoot + "/entry.py", 'r+') as file:
        efile = str(file.read())
        file.close()
    with io.open(newPackageRoot + "/entry.py", 'w') as file:
        efile = efile.replace('packageInternalName = ""','packageInternalName = "'+ inName +'"')
        file.truncate(0)
        file.write(efile)
        file.close()
    print("edited entry script")

    # Achtung! This is the worst solution i made in my whole programming way. REWORK IT ASAP (or close eyes on it)

    infoJson = "{\n\"name\": \"%s\",\n\"description\": \"%s\",\n\"version\": \"%s\",\n\"loadFile\": \"Packages.%s.entry\"\n}" % (norName,desc,version,inName)

    with io.open(newPackageRoot + "/info.json", 'w') as jfile:
        jfile.write(infoJson)
        jfile.close()

    # replace {inName} in files with {inName} from dialogue
    # print info about it