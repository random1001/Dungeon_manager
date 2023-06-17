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

frame = customtkinter.CTkFrame(master=root, height=512, width=512, fg_color="green")
frame.pack()

img = customtkinter.CTkImage(light_image=Image.open(os.path.join("gui/comb.jpg")), size=(512 , 512))
label = customtkinter.CTkLabel(master=frame, image=img, text='')
label.grid(column=0, row=0)

button = customtkinter.CTkButton(master=root, text="Exit", command=endProgram)
button.pack(pady=12, padx=10)


root.mainloop()
