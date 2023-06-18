import os

def removeFIF(dir):
    for filename in os.listdir(dir):
        if filename.endswith(".jfif"):
            os.rename(filename, filename[:-3]+"pg")

removeFIF(".")

