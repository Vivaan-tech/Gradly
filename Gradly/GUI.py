from PIL import Image
import customtkinter as ctk
from ServerSide import getAverages, getStuName
import ctypes


# window
window = ctk.CTk()
window.title("Gradly")
window.geometry('300x500')
window.resizable(False, False)
# photo = PhotoImage(Image.open('GradlyIconNew.png'))

myappid = 'GradlyNewIcon.ico'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window.iconbitmap('GradlyIcons/GradlyNewIcon.ico')


username = ""
password = ""
dashboardButtonWidth = 10
# basic functions
def logIn():
    username = userEntry.get()
    password = passEntry.get()
    x = str(getStuName(username, password))
    #print(x)
    if('Invalid' in x):
        errorMessage.place(x=60, y = 320)
        errorMessage.configure(text = "Invalid Credentials!")
    else:
        headerLabel.configure(text = "Grades")
        headerLabel.configure(font=('Poppins', 30))
        headerLabel2.configure(text = x)
        options(username, password, dashboardButtonWidth)
        loginFrame.place_forget()
        mainFrame.place(x=0,y=80)
        
def viewPassword():
    if passEntry.cget('show') == '*':
        passEntry.configure(show='')
    else:
        passEntry.configure(show='*')


# basic layout
topBox = ctk.CTkFrame(
    master = window,
    bg_color='white',
    fg_color="ForestGreen",
    width=400,
    height = 80
)

loginFrame=ctk.CTkFrame(
    bg_color="white",
    fg_color="white",
    master = window,
    width=400,
    height = 520
)

#Error Frame
errorMessage = ctk.CTkLabel(
    master = loginFrame,
    text_color="white",
    font=('Poppins', 20),
    fg_color="ForestGreen",
    height=20,
    bg_color = "white",
    corner_radius= 5 
)

headerLabel = ctk.CTkLabel(
    master = topBox,
    text = "Gradly",
    text_color='white',
    font=('Poppins', 40)
)

headerLabel2 = ctk.CTkLabel(
    master = topBox,
    text = "Log In to HAC",
    text_color='white',
    font=('Poppins', 20)
)

userEntry = ctk.CTkEntry(
    fg_color= "white",
    border_color="ForestGreen",
    bg_color="white",
    master = loginFrame,
    text_color="dimgray",
    corner_radius=10,
    width=250,
    height=50,
    placeholder_text="Username",
    font=('Poppins', 15)

)

passEntry = ctk.CTkEntry(
    border_color="ForestGreen",
    fg_color= "white",
    bg_color="white",
    master = loginFrame,
    text_color="dimgray",
    corner_radius=10,
    width=250,
    height=50,
    placeholder_text="Password",
    font=('Poppins', 15),
    show='*'
)

passView = ctk.CTkButton(
    master = passEntry,
    bg_color='transparent',
    fg_color='ForestGreen',
    hover_color='DarkGreen',
    text_color="white",
    corner_radius=10,
    width=25,
    height=25,
    text="View",
    command=viewPassword
)


logInButton = ctk.CTkButton(
    master = loginFrame,
    bg_color='transparent',
    fg_color='ForestGreen',
    hover_color='DarkGreen',
    text_color="white",
    corner_radius=10,
    width=200,
    height=50,
    text="Log In",
    font=('Poppins', 25),
    command=logIn
)

mainFrame = ctk.CTkFrame(
    bg_color="white",
    fg_color="white",
    width= 400, 
    height=420,
    master = window
)

settingsFrame = ctk.CTkFrame(
    bg_color="white",
    fg_color="white",
    width= 400, 
    height=420,
    master = window
)

class1Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover = False,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 19)
)

class2Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover = False,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 19)
)

class3Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover = False,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 19)
)

class4Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover = False,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 19)
)

class5Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover = False,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 19)
)

class6Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover = False,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 19)
)

class7Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover = False,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 19)
)

class1Label = ctk.CTkButton(
    master = class1Button,
    fg_color="dimgrey",
    hover_color="dimgrey",
    width=5,
    height = 20,
    corner_radius=10,
    font = ("Poppins", 14),
    text_color="white"
)

class2Label = ctk.CTkButton(
    bg_color="transparent",
    master = class2Button,
    fg_color="dimgray",
    hover_color="dimgray",
    width=5,
    height = 20,
    corner_radius=10,
    font = ("Poppins", 14),
    text_color="white"
)

class3Label = ctk.CTkButton(
    bg_color="transparent",
    master = class3Button,
    fg_color="dimgray",
    hover_color="dimgray",
    width=5,
    height = 20,
    corner_radius=10,
    font = ("Poppins", 14),
    text_color="white"
)

class4Label = ctk.CTkButton(
    bg_color="transparent",
    master = class4Button,
    fg_color="dimgray",
    hover_color="dimgray",
    width=5,
    height = 20,
    corner_radius=10,
    font = ("Poppins", 14),
    text_color="white"
)

class5Label = ctk.CTkButton(
    bg_color="transparent",
    master = class5Button,
    hover_color="dimgray",
    fg_color="dimgray",
    width=5,
    height = 20,
    corner_radius=10,
    font = ("Poppins", 14),
    text_color="white"
)

class6Label = ctk.CTkButton(
    bg_color="transparent",
    master = class6Button,
    hover_color="dimgray",
    fg_color="dimgray",
    width=5,
    height = 20,
    corner_radius=10,
    font = ("Poppins", 14),
    text_color="white"
)

class7Label = ctk.CTkButton(
    master = class7Button,
    fg_color="dimgray",
    hover_color="dimgray",
    width=5,
    height = 20,
    corner_radius=10,
    font = ("Poppins", 14),
    text_color="white",
    bg_color="transparent",
)

def logOut():
    userEntry.delete(0, len(userEntry.get()))
    passEntry.delete(0, len(passEntry.get()))
    dashboard.place_forget()
    mainFrame.place_forget()
    settingsFrame.place_forget()
    headerLabel.configure(text = "Gradly")
    headerLabel2.configure(text = "Log In to HAC")
    loginFrame.place(x=0, y= 80)

logOutButton = ctk.CTkButton(
    master = settingsFrame,
    bg_color='transparent',
    fg_color='forestGreen',
    hover_color='DarkGreen',
    text_color="white",
    corner_radius=10,
    width=200,
    height=50,
    text="Log Out",
    font=('Poppins', 25),
    command=logOut
)

def displaySettings():
    mainFrame.place_forget()
    settingsFrame.place(x = 0 , y = 80)
    headerLabel.configure(text = "Settings")
    #headerLabel2.configure(text = "")
    logOutButton.place(x=50, y = 280)

def displayGrades():
    headerLabel.configure(text = "Grades") 
    settingsFrame.place_forget()
    mainFrame.place(x=0, y = 80)

dashboard = ctk.CTkFrame(
    master=window,
    width=300,
    height=60,
    fg_color='ForestGreen',
    bg_color="white"
    )


dashboard1Button = ctk.CTkButton(
    master = dashboard,
    fg_color='forestgreen',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 18)
)

dashboard2Button = ctk.CTkButton(
    master = dashboard,
    fg_color='forestgreen',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 18)
)

GradesTabImage = ctk.CTkImage(Image.open("GradlyIcons/HomeButton.png"), size=(30, 30))
dashboard3Button = ctk.CTkButton(
    master = dashboard,
    fg_color='forestgreen',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 18),
    image=GradesTabImage,
    command = displayGrades
)

dashboard4Button = ctk.CTkButton(
    master = dashboard,
    fg_color='forestgreen',#2b2b2b
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 18)
)

settingsImage = ctk.CTkImage(Image.open("GradlyIcons/SettingsIcon.png"), size=(30, 30))
dashboard5Button = ctk.CTkButton(
    master = dashboard,
    fg_color='forestgreen',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Poppins', 18),
    image=settingsImage,
    command = displaySettings
)


mainButtonList = [class1Button, class2Button, class3Button, class4Button,class5Button
                  , class6Button, class7Button, class1Label, class2Label, class3Label, 
                  class4Label, class5Label, class6Label, class7Label]

mainDashboardList = [dashboard, dashboard1Button, dashboard2Button, 
                     dashboard3Button, dashboard4Button, dashboard5Button]
def options(user, passw, dashboardButtonWidth):
    posX = 25
    num= dashboardButtonWidth*(len(mainDashboardList)-1)
    classes = getAverages(user , passw)
    #print(classes)
    for x in range(0, len(classes) - 7):
        #s = len(classes[x]) + 10
        mainButtonList[x].configure(text = "{:<29}".format(classes[x]))
        mainButtonList[x+7].configure(text = classes[x+7])
    for x in range(0, len(mainButtonList) - 7):
        mainButtonList[x].place(x = 10, y = ((x+1) * 40)-20)
        mainButtonList[x+7].place(x = 235, y = 3)
    for i in range(1, len(mainDashboardList)+1):
        if i == 1:
            mainDashboardList[i-1].place(x=0, y=440)
        else:
            #((i-2)*((300/(len(mainDashboardList)-1))-dashboardButtonWidth)) + num
            mainDashboardList[i-1].configure(text = "", hover_color="forestgreen")
            mainDashboardList[i-1].place(x=posX, y = 10)
            posX += 50
            #(300/(len(mainDashboardList)-1))-dashboardButtonWidth





logInButton.place(x=50, y=250)
passEntry.place(x=30,y=150)
passView.place(x=190, y=13)
userEntry.place(x=30, y=80)
headerLabel2.place(x=10, y=50)
headerLabel.place(x=10,y=4)
topBox.place(x = 0, y = 0)
loginFrame.place(x=0, y=80)




window.mainloop()