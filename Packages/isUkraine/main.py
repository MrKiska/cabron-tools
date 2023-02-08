from colorthief import ColorThief
from lib.colors import rgbToSimilarName


def main(image: str):
    print("is ua?\n")
    color_thief = ColorThief(image)
    palette = color_thief.get_palette(color_count=6)

    uaflag = ['blue','yellow']
    rufrflag = ['blue','red','white']
    plgeflag = ['red','white']

    symbolicNames = []
    for col in palette:
        symbolicNames.append(rgbToSimilarName(col))

    symbolicNames = [*set(symbolicNames)]
    symbolicNames.extend([""]*(6-len(symbolicNames)))

    # some bad solutions

    if symbolicNames[0] in uaflag and symbolicNames[1] in uaflag:
        print("Achtung! Hryu hryu alarm!")
        print("this is ukrainian flag1!!!!1!1")

    elif symbolicNames[0] in rufrflag and symbolicNames[1] in rufrflag and symbolicNames[2] in rufrflag:
        print('This could be Russian or French flag (maybe)')

    elif symbolicNames[0] in plgeflag and symbolicNames[1] in plgeflag:
        print("O kurwa! This is Polish flag (or not polish, idk)")
    else:
        print("Achtung! Hryu hryu alarm!")
        print("this is ukrainian flag1!!!!1!1")