import customtkinter
from PIL import Image, ImageTk
import customtkinter as ctk
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
# root.attributes("-fullscreen", True)

root.title("Mega Mart Self Checkout System")
root.attributes("-fullscreen", "True")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# root.geometry("1920x1080")

# def login():
#     print("Test")

#frame = customtkinter.CTkFrame(master=root)
#frame.pack(pady=0, padx=0, fill="both", expand=True)

# img = Image.open("gui/castle.jpg")
# label = ctk.CTkLabel(master=frame, image=img)
# label.pack()

#img = customtkinter.CTkImage(light_image=Image.open(os.path.join("gui/castle.jpg")), size=(1024 , 1024))
#label = customtkinter.CTkLabel(master=frame, image=img, text='')
#label.grid(column=0, row=0)

# image = Image.open("image.jpg")
# image = image.resize((1920, 1080), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(image)


# label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
# label.pack(pady=12, padx=10)

# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
# entry1.pack(pady=12, padx=10)

# entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
# entry2.pack(pady=12, padx=10)

# button = customtkinter.CTkButton(master=frame, text="Login", command=login)
# button.pack(pady=12, padx=10)

# checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
# checkbox.pack(pady=12, padx=10)

root.mainloop()

