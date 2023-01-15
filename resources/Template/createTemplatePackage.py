# with dialogue



def main():
    while True:
        inName = input("enter internal package name (without spaces)\n:")
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
    # copy content of /resources/Tempalte/package to /Packages/{inName}
    # replace {inName} in files with {inName} from dialogue
    # print info about it