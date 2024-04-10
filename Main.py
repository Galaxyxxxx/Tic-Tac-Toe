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
def handlendgame(result):
    win = CTkMessagebox.CTkMessagebox(title="Game Over", message=f"{player_turn} wins!", icon="info", option_2="Play Again", option_1="Exit The App")
    if(result == True):
        win
    else:
        win.configure(title="Game Over", message="It's a draw!", icon="info", option_2="Play Again", option_1="Exit The App")
    win.get() == "Exit The App" and app.destroy()
    win.get() == "Play Again" and firstplayerchoose()
def handleplayermove(row, col):
    btn = buttons[row][col]
    global player_turn
    if(btn._state !="disabled"):
        btn.configure(text = player_turn, font = xfont, text_color = "black", state="disabled")
        if(winconditions() == 1):
            handlendgame(True)
        elif(winconditions() == 2):
            handlendgame(False)
        else:
            handleplayerturn(player_turn)
    else:
            CTkMessagebox.CTkMessagebox(title="Arleady Taken", message="The field is already occupied", icon="cancel")
def handleplayerturn(lastturn):
    global player_turn
    if lastturn == "X":
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
        btn.configure(command=partial(handleplayermove, row, col))
        btn.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        board.grid_columnconfigure(col, weight=1)
        board.grid_rowconfigure(row, weight=1)
        buttons[row][col] = btn
    
def winconditions():
    for row in range(3):
        if buttons[row][0]._text == buttons[row][1]._text == buttons[row][2]._text != "test":
            return 1
    for col in range(3):
        if buttons[0][col]._text == buttons[1][col]._text == buttons[2][col]._text != "test":
            return 1
    if buttons[0][0]._text == buttons[1][1]._text == buttons[2][2]._text != "test":
        return 1
    if buttons[0][2]._text == buttons[1][1]._text == buttons[2][0]._text != "test":
        return 1
    if all(button._text != 'test' for row in buttons for button in row):
        return 2
#App run
app.mainloop()


