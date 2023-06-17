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

#frame = customtkinter.CTkFrame(master=root, height=512, width=512, fg_color="green")
#frame.pack()
# frame1 = customtkinter.CTkFrame(master=root, fg_color="green", width=1500, height=908)
# frame1.grid()

MainFrame=customtkinter.CTkFrame(master=root, fg_color="yellow", height=250, width=250)
MainFrame.grid(row=0, column=0, sticky="WENS")

Frame0=customtkinter.CTkFrame(master=root, fg_color="green", height=200, width=200)
Frame0.grid(row=1, column=0, sticky="WENS")

Frame1=customtkinter.CTkFrame(master=root, fg_color="blue", height=250, width=250)
Frame1.grid(row=0, column=1, sticky="WENS")

Frame2=customtkinter.CTkFrame(master=root, fg_color="purple", height=100, width=150)
Frame2.grid(row=1, column=1, sticky="NSEW")

horizontal=customtkinter.CTkFrame(master=root, fg_color="#386A18", height=100, width=500)
horizontal.grid(row=2, column=0, columnspan=2, sticky="WENS")

vertical=customtkinter.CTkFrame(master=root, fg_color="#B43838", height=300, width=100)
vertical.grid(row=0, column=2, rowspan=3, sticky="NSEW")


#Configuration
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# frame2 = customtkinter.CTkFrame(master=root, fg_color="green")
# frame2.place(relx=1.0, rely=0.0, anchor="ne", y=200)

# picture = customtkinter.CTkFrame(master=root, height=512, width=512, fg_color="green")
# picture.pack()

# img = customtkinter.CTkImage(light_image=Image.open(os.path.join("gui/comb.jpg")), size=(512 , 512))
# label = customtkinter.CTkLabel(master=picture, image=img, text='')
# label.grid(column=0, row=0)

# parent_frame = customtkinter.CTkFrame(root, fg_color="#D3D3D3", width=100, height=100)
# parent_frame.place(relx=0.2, rely=0.2, anchor="ne")

# child_frame = customtkinter.CTkFrame(parent_frame, fg_color="white", width=90, height=90)
# child_frame.place(relx=0.5, rely=0.5, anchor="center")

# img = customtkinter.CTkImage(light_image=Image.open(os.path.join("gui/weight.png")), size=(80 , 80))
# label = customtkinter.CTkLabel(master=parent_frame, image=img, text='')
# label.place(relx=0.5, rely=0.5, anchor="center")

# button = customtkinter.CTkButton(master=root, text="Exit", command=endProgram,  width=100, height=100)
# button.place(relx=1.0, rely=0.0, anchor="ne")

root.mainloop()
