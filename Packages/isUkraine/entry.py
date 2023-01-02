import os
import Packages.isUkraine.main as mainPy

root = os.getcwd()


def go():
    image = input("give path to image (drag and drop) or q to exit\n")
    if image == "q": return
    image = image.replace("'","")
    mainPy.main(image=image)



go()