import os
from tkinter import filedialog
nvidia = "y0r6_logo_nvidia.bik"
oldNvidia = "y0r6_logo_nvidia_old.bik"
ubisoft = "y0r6_logo_ubisoft.bik"
oldUbisoft = "y0r6_logo_ubisoft_old.bik"
defaultFilepath = "C:\Program Files (x86)\Steam\steamapps\common\Tom Clancy's Rainbow Six Siege\\videos\startup"
filepath = ""
option = -999

def renameFiles(path=defaultFilepath):
    os.rename(path + nvidia, path + oldNvidia)
    os.rename(path + ubisoft, path + oldUbisoft)


def createFiles(path=defaultFilepath):
    open(path + nvidia, 'w')
    open(path + ubisoft, 'w')

if __name__ == "__main__":
    print("This script will make it so that the intro cutscenes do not play when loading Rainbow Six: Siege")

    print("Enter 1 to open file explorer, 2 to manually type or paste file path")
    print("Default directory: " + defaultFilepath)
    while (option != '1' and option != '2'):
        option = input("Enter option here: ")
        print()
        if option == "1":
            filepath = filedialog.askdirectory()
        elif option == "2":
            filepath = input("Enter filepath here: ")
            print()
        else:
            print("Invalid option")
            continue
        filepath += "/"
        try:
            renameFiles(filepath)
            
        except:
            option = -999
            print("Files not found at specified location")
    createFiles(filepath)
        

    print("Operation completed\n")
    print("Old bitmaps are stored as: ")
    print(filepath + oldNvidia)
    print(filepath + oldUbisoft)
    print("To play cutscenes during load again, delete files")
    print("/" + nvidia + " and /" + ubisoft)
    print("and remove \"_old\" from the two bitmap files that contain it")
    input("Press any key to exit")