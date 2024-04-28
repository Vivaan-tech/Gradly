import customtkinter as ctk
from ServerSide import getAverages, getStuName
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


username = ""
password = ""
# basic functions
def logIn():
    x = str(getStuName(userEntry.get(), passEntry.get()))
    if('Invalid' in x):
        errorMessage.place(x=50, y = 320)
        errorMessage.configure(text = "Invalid Credentials!")
    else:
        username = userEntry.get()
        password = passEntry.get()
        headerLabel.configure(text = x)
        headerLabel.configure(font=('Noto Sans', 30))
        headerLabel2.configure(text = "Options")
        options(username, password)
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
    font=('Noto Sans', 20),
    bg_color="ForestGreen",
    corner_radius=20
)

headerLabel = ctk.CTkLabel(
    master = topBox,
    text = "Gradly",
    text_color='white',
    font=('Noto Sans', 40)
)

headerLabel2 = ctk.CTkLabel(
    master = topBox,
    text = "Log In to HAC",
    text_color='white',
    font=('Noto Sans', 20)
)

userEntry = ctk.CTkEntry(
    master = loginFrame,
    text_color="white",
    corner_radius=10,
    width=250,
    height=50,
    placeholder_text="Username",
    font=('Noto Sans', 25)

)

passEntry = ctk.CTkEntry(
    master = loginFrame,
    text_color="white",
    corner_radius=10,
    width=250,
    height=50,
    placeholder_text="Password",
    font=('Noto Sans', 25)

)

logInButton = ctk.CTkButton(
    master = loginFrame,
    bg_color='transparent',
    fg_color='ForestGreen',
    hover_color='DarkGreen',
    text_color="white",
    corner_radius=10,
    width=50,
    height=50,
    text="Log In",
    font=('Noto Sans', 25),
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
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Noto Sans', 18)
)

class2Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Noto Sans', 18)
)

class3Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Noto Sans', 18)
)

class4Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Noto Sans', 18)
)

class5Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Noto Sans', 18)
)

class6Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Noto Sans', 18)
)

class7Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Noto Sans', 18)
)

mainButtonList = [class1Button, class2Button, class3Button, class4Button,class5Button, class6Button, class7Button]

def options(user, passw):
    classes = getAverages(user , passw)
    #print(classes)
    for x in range(0, len(classes)):
        mainButtonList[x].configure(text = classes[x])
    for x in range(0, len(mainButtonList) ):
        mainButtonList[x].place(x = 10, y = ((x+1) * 40)-20)


logInButton.place(x=100, y=250)
passEntry.place(x=20,y=150)
userEntry.place(x=20, y=80)
headerLabel2.place(x=10, y=50)
headerLabel.place(x=10,y=10)
topBox.place(x = 0, y = 0)
loginFrame.place(x=0, y=80)




window.mainloop()
