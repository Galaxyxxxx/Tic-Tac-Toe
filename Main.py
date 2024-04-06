import tkinter
import customtkinter

#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#App frame
app = customtkinter.CTk()
app.geometry("1280x720")
app.minsize(width = 1280, height = 720)
app.title("Tic-Tac-Toe")


#Ui elements
mainfont = customtkinter.CTkFont(family= "Arial", size = 20, weight = "bold")
title = customtkinter.CTkLabel(app, text = "Tic-Tac-Toe", font = mainfont)
title.pack(pady = 30)

#Game logic
def handleplayermove(col, row):
    print("l", col, row)
    
    
#Tic-Tac-Toe board
board = customtkinter.CTkFrame(master = app, fg_color = "transparent", border_width= 0, border_color = "white")
board.pack(expand=True, fill="both", padx=50, pady=50)
buttons = []
for row in range(3):
    for col in range(3):
        btn = customtkinter.CTkButton(board, fg_color= "#e6e6e6", border_width= 0, border_color = "white", font = mainfont, corner_radius = 0, hover_color= "#cccccc", command=handleplayermove(col, row))
        buttons.append(btn)
        btn.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        board.grid_columnconfigure(col, weight=1)
        board.grid_rowconfigure(row, weight=1)

#App run
app.mainloop()


