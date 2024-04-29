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

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

window.iconbitmap('GradlyNewIcon.ico')


username = ""
password = ""
dashboardButtonWidth = 10
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
        headerLabel.configure(font=('Tahoma', 30))
        headerLabel2.configure(text = "Options")
        options(username, password, dashboardButtonWidth)
        loginFrame.destroy()
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
    font=('Tahoma', 20),
    bg_color="ForestGreen",
    corner_radius=20
)

headerLabel = ctk.CTkLabel(
    master = topBox,
    text = "Gradly",
    text_color='white',
    font=('Tahoma', 40)
)

headerLabel2 = ctk.CTkLabel(
    master = topBox,
    text = "Log In to HAC",
    text_color='white',
    font=('Tahoma', 20)
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
    font=('Tahoma', 15)

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
    font=('Tahoma', 15),
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
    font=('Tahoma', 25),
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
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

class2Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

class3Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

class4Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

class5Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

class6Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

class7Button = ctk.CTkButton(
    master = mainFrame,
    fg_color='ForestGreen',
    width = 280,
    height = 30,
    hover_color="DarkGreen",
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

def displaySettings():
    mainFrame.place_forget()
    settingsFrame.place(x = 0 , y = 80)

def displayGrades():
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
    fg_color='white',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

dashboard2Button = ctk.CTkButton(
    master = dashboard,
    fg_color='white',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

dashboard3Button = ctk.CTkButton(
    master = dashboard,
    fg_color='white',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

dashboard4Button = ctk.CTkButton(
    master = dashboard,
    fg_color='white',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18)
)

settingsImage = ctk.CTkImage(Image.open("gear.png"), size=(10, 10))
dashboard5Button = ctk.CTkButton(
    master = dashboard,
    fg_color='white',
    width = dashboardButtonWidth,
    height = 10,
    text_color='white',
    corner_radius=10,
    font=('Tahoma', 18),
    image=settingsImage,
    command = displaySettings
)


mainButtonList = [class1Button, class2Button, class3Button, class4Button,class5Button, class6Button, class7Button]
mainDashboardList = [dashboard, dashboard1Button, dashboard2Button, dashboard3Button, dashboard4Button, dashboard5Button]
def options(user, passw, dashboardButtonWidth):
    num= dashboardButtonWidth*(len(mainDashboardList)-1)
    classes = getAverages(user , passw)
    #print(classes)
    for x in range(0, len(classes)):
        mainButtonList[x].configure(text = classes[x])
    for x in range(0, len(mainButtonList) ):
        mainButtonList[x].place(x = 10, y = ((x+1) * 40)-20)
    for i in range(1, len(mainDashboardList)+1):
        if i == 1:
            mainDashboardList[i-1].place(x=0, y=440)
        else:
            posX = ((i-2)*((300/(len(mainDashboardList)-1))-dashboardButtonWidth)) + num
            mainDashboardList[i-1].configure(text = "", hover_color="#171717")
            mainDashboardList[i-1].place(x=posX, y = 20)
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
