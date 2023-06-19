import vlc

import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
file_path = "../sounds/test_file.mp3"
player = vlc.MediaPlayer(file_path)
stop_image = ctk.CTkImage(light_image=Image.open("../buttons/stop.png"), size=(30, 30))
play_image = ctk.CTkImage(light_image=Image.open("../buttons/play.png"), size=(30, 30))
index = 0

root=ctk.CTk()

def play_mp3():
    global player
    player.play()

def stop_mp3():
    global player
    player.set_pause(1)

def continue_mp3():
    global player
    player.set_pause(0)

def control_mp3():
    global player
    global Button
    global index
    if index == 0:
        player.play()
        Button.configure(image=stop_image)
    else:
        player.set_pause(1)
        Button.configure(image=play_image)

    if index == 0: index = 1
    else: index = 0        


Button = ctk.CTkButton(root, border_color="Yellow", border_width=2, image=play_image, text='', width=35 , command=control_mp3)
Button.pack(pady=20)

root.mainloop()