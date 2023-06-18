# from screeninfo import get_monitors
# for m in get_monitors():
#     print(str(m))

# import customtkinter
# root = customtkinter.CTk()
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()

# print(width, height)

import customtkinter as tk
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def change_image():
    # Change the image filename/path based on your requirements
    image_path = os.path.join("gui/doctor_who.png")
    image = tk.PhotoImage(file=image_path)
    image_label.config(image=image)
    image_label.image = image  # Update reference to avoid garbage collection

# Create the main window
window = tk.CTk()

# Create a button
button = tk.CTkButton(window, text="Change Image", command=change_image)
button.pack(side=tk.LEFT)

# Create an image label
image_path = os.path.join("gui/weight.png")  # Replace with your default image path
image = tk.CTkImage(light_image=image_path, size=(512 , 512))
image_label = tk.CTkLabel(window, image=image)
image_label.pack(side=tk.RIGHT)

# Run the application
window.mainloop()
