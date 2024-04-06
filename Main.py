import tkinter
import customtkinter
import CTkMessagebox
from functools import partial

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
xfont = customtkinter.CTkFont(family= "Arial", size = 100, weight = "bold")
title = customtkinter.CTkLabel(app, text = "Tic-Tac-Toe", font = mainfont)
title.pack(pady = 25)

#Game logic
def firstplayerchoose():
    global player_turn
    msg = CTkMessagebox.CTkMessagebox(title="Wybierz", message="Wybierz startującą figurę", icon="question", option_1="X", option_2="O")
    response = msg.get()
    if response=="X":
        player_turn = "X"      
    elif response=="O":
        player_turn = "O"

firstplayerchoose()
def handleplayermove(row, col, text):
    btn = buttons[row][col]
    global player_turn
    if(text != "X" and text != "O"):
        if(player_turn == "X"):
            btn.configure(text = "X", font = xfont, text_color = "black")
            print(player_turn)
            handleplayerturn(True)
        else:
            btn.configure(text = "O", font = xfont, text_color = "black")
            print(player_turn)
            handleplayerturn(False)
    else:
            CTkMessagebox.CTkMessagebox(title="Arleady taken", message="The field is already occupied", icon="cancel")
def handleplayerturn(lastturn):
    global player_turn
    if lastturn == True:
        player_turn = "O"
        currentplayerlabel.configure(text = f"Current Player: {player_turn}")
    else:
        player_turn = "X"
        currentplayerlabel.configure(text = f"Current Player: {player_turn}")
    
    
    
#Tic-Tac-Toe board
currentplayerlabel = customtkinter.CTkLabel(app, text = f"Current Player: {player_turn}", font = mainfont)
currentplayerlabel.pack()
board = customtkinter.CTkFrame(master = app, fg_color = "transparent", border_width= 0, border_color = "white")
board.pack(expand=True, fill="both", padx=35, pady=35)
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        btn = customtkinter.CTkButton(board, fg_color= "#e6e6e6", border_width= 0, border_color = "white", font = mainfont, corner_radius = 0, hover_color= "#cccccc", text="test")
        btn.configure(command=partial(handleplayermove, row, col, btn._text))
        btn.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        board.grid_columnconfigure(col, weight=1)
        board.grid_rowconfigure(row, weight=1)
        buttons[row][col] = btn
    
    
#App run
app.mainloop()


