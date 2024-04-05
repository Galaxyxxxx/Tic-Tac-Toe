import tkinter
import customtkinter

#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#App frame
app = customtkinter.CTk()
app.geometry("1280x720")
app.title("Tic-Tac-Toe")
app._window = customtkinter.CTk()

#Ui elements
mainfont = customtkinter.CTkFont(family= "Arial", size = 20, weight = "bold")
title = customtkinter.CTkLabel(app, text = "Tic-Tac-Toe", font = mainfont)
title.pack(pady = 30)

#Tic-Tac-Toe board
board = customtkinter.CTkFrame(master = app, width = 750, height = 450, bg_color = "white", border_width= 5, border_color = "white")
buttons = []
for row in range(3):
    for col in range(3):
        btn = customtkinter.CTkButton(board, text="", width= 250, height=150, fg_color= "transparent", border_width= 5, border_color = "white", font = mainfont)
        buttons.append(btn)
        btn.grid(row=row, column=col, sticky="nsew")
        
board.update_idletasks()
width = board.winfo_width()
height = board.winfo_height()
app._window.geometry(f"{width}x{height}")
board.pack(padx = 50)

#App run
app.mainloop()
