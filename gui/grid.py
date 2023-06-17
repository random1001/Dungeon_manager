import customtkinter 
 
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

#columnspan - number of column u go through
#rowspan - number of rows u go through

#columnconfigure
#rowconfigure


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

root.mainloop()