import customtkinter as ctk
from PIL import Image
import os
import glob

#Global index variable
index = 0

#Note this script requires folder with jpg files in location ""../images"
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

image = list()
file_count = len(glob.glob("../images/" + '/*.jpg'))
for filename in os.listdir("../images"):
    if filename.endswith(".jpg"):
        img = ctk.CTkImage(light_image=Image.open("../images/"+filename), size=(512, 512))
        image.append(img)    

root=ctk.CTk()

image_label = ctk.CTkLabel(root, image=image[0], text="")
image_label.pack()


def NextPicture():
    global index #Access to global variable
    index += 1
    image_label.configure(image=image[index])
    if index == file_count - 1: index=0

Button = ctk.CTkButton(root, border_color="Yellow", border_width=2, text="Next picture", font=("Roboto", 20), width=200, height=50, command=NextPicture)
Button.pack(pady=20)

root.mainloop()


