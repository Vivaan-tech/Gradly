import customtkinter as ctk
from tkinter import *
import ServerSide
from PIL import Image
import ctypes

# window
window = ctk.CTk()
window.title("Gradly")
window.geometry('300x500')
window.resizable(False, False)
# photo = PhotoImage(Image.open('GradlyIconNew.png'))

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window.iconbitmap('GradlyNewIcon.ico')
# basic functions
def logIn():
    x = str(ServerSide.getStuName(userEntry.get(), passEntry.get()))
    if('Invalid' in x):
        errorMessage.place(x=50, y = 320)
        errorMessage.configure(text = "Invalid Credentials!")
    else:
        headerLabel.configure(text = x)
        headerLabel.configure(font=('afacad', 30))
        headerLabel2.configure(text = "Options")
        loginFrame.destroy()
        mainFrame.place(x=0,y=80)



    

# basic layout
topBox = ctk.CTkFrame(
    master = window,
    fg_color="ForestGreen",
    width=400,
    height = 80
)

loginFrame=ctk.CTkFrame(
    master = window,
    width=400,
    height = 520
)

#Error Frame
errorMessage = ctk.CTkLabel(
    master = loginFrame,
    text_color="white",
    font=('afacad', 20),
    bg_color="ForestGreen",
    corner_radius=20
)

headerLabel = ctk.CTkLabel(
    master = topBox,
    text = "Gradly",
    text_color='white',
    font=('afacad', 40)
)

headerLabel2 = ctk.CTkLabel(
    master = topBox,
    text = "Log In to HAC",
    text_color='white',
    font=('afacad', 20)
)

userEntry = ctk.CTkEntry(
    master = loginFrame,
    text_color="white",
    corner_radius=10,
    width=250,
    height=50,
    placeholder_text="Username",
    font=('afacad', 25)

)

passEntry = ctk.CTkEntry(
    master = loginFrame,
    text_color="white",
    corner_radius=10,
    width=250,
    height=50,
    placeholder_text="Password",
    font=('afacad', 25)

)

logInButton = ctk.CTkButton(
    master = loginFrame,
    bg_color='transparent',
    fg_color='ForestGreen',
    hover_color='DarkGreen',
    text_color="white",
    corner_radius=40,
    width=50,
    height=50,
    text="Log In",
    font=('afacad', 25),
    command=logIn
)

mainFrame = ctk.CTkFrame(
    width= 400, 
    height=420,
    master = window
)

class1Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 200,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=40,
    font=('afacad', 25)
)


class1Button.place(x=10, y = 10)
logInButton.place(x=85, y=250)
passEntry.place(x=20,y=150)
userEntry.place(x=20, y=80)
headerLabel2.place(x=10, y=50)
headerLabel.place(x=10,y=10)
topBox.place(x = 0, y = 0)
loginFrame.place(x=0, y=80)


















window.mainloop()