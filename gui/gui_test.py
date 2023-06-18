import customtkinter
from PIL import Image, ImageTk
import customtkinter as ctk
import os
import win32api
import win32con
import pywintypes
import time


def endProgram():
    exit()

def ChangePicture(label):
    img = customtkinter.CTkImage(light_image=Image.open(os.path.join("gui/comb.jpg")), size=(512 , 512))
    label.image = img

#Very experimental
#The reasion is buggy fullscreen in customtkinter
devmode = pywintypes.DEVMODEType()
####################################################################

devmode.PelsWidth = 1280 # desired width
devmode.PelsHeight = 720 # desired height
devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
win32api.ChangeDisplaySettings(devmode, 0)
####################################################################

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry(f"{width}x{height}-10+0")
root.attributes('-fullscreen',True)


#Very experimental
#The reasion is buggy fullscreen in customtkinter
####################################################################
devmode.PelsWidth = 1920  # desired width
devmode.PelsHeight = 1080 # desired height
devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
win32api.ChangeDisplaySettings(devmode, 0)
####################################################################
half0=customtkinter.CTkFrame(master=root)#, height=height, width=width/2)
half0.grid(row=0, column=0, sticky="WENS")
half1=customtkinter.CTkFrame(master=root)#, height=height, width=width/2)
half1.grid(row=0, column=1, sticky="WENS")

PictureFrame=customtkinter.CTkFrame(master=half1,fg_color="green")
PictureFrame.grid(row=1, column=0, sticky="SENW")

img = customtkinter.CTkImage(light_image=Image.open(os.path.join("gui/comb.jpg")), size=(512 , 512))
label = customtkinter.CTkLabel(master=PictureFrame, image=img, text='')
label.grid()

ChangeButton=customtkinter.CTkButton(master=half0, text='', command=ChangePicture(label), width=100, height=100)
ChangeButton.place(relx=1.0, rely=0.0, anchor="ne")





EmptyFrame=customtkinter.CTkFrame(master=half1)
EmptyFrame.grid(row=0, column=0, sticky="SENW")

ExitButton=customtkinter.CTkButton(master=half1, text="Exit", command=endProgram, width=50, height=50)
ExitButton.place(relx=1.0, rely=0.0, anchor="ne")







root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

half1.columnconfigure(0, weight=1)
half1.rowconfigure(0, weight=1)
half1.rowconfigure(1, weight=1)

PictureFrame.rowconfigure(0, weight=1)
PictureFrame.columnconfigure(0, weight=1)


root.mainloop()
