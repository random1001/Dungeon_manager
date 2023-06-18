import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


#Images
default_image = ctk.CTkImage(light_image=Image.open("gui/comb.jpg"), size=(512, 512))
new_image = ctk.CTkImage(light_image=Image.open("gui/profile_pic.jpg"), size=(512, 512))

root=ctk.CTk()


image_label = ctk.CTkLabel(root, image=default_image, text="")  # display image with a CTkLabel
image_label.pack()

def SwapPicture():
    image = image_label.cget('image')
    if image == default_image:
        image_label.configure(image=new_image)
    else:
        image_label.configure(image=default_image)

Button = ctk.CTkButton(root, border_color="Yellow", border_width=2, text="Swap picture", width=200, height=50, command=SwapPicture)
Button.pack(pady=20)

root.mainloop()