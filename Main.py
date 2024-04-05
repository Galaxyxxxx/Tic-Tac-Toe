import tkinter
import customtkinter

#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#App frame
app = customtkinter.CTk()
app.geometry("800x600")
app.title("Tic-Tac-Toe")

#Ui Elements
mainfont = customtkinter.CTkFont(family= "Arial", size = 20, weight = "bold")
title = customtkinter.CTkLabel(app, text = "Tic-Tac-Toe", font = mainfont)
title.pack(pady = 30)

#Tic-Tac-Toe board




#App run
app.mainloop()
