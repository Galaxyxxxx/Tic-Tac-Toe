import tkinter
import customtkinter

#System settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

#App frame
app = customtkinter.CTk()
app.geometry("1280x720")
app.minsize(width = 1280, height = 720)
mainfont = customtkinter.CTkFont(family= "Arial", size = 20, weight = "bold")
app.title("Game center")

#Ui elements
