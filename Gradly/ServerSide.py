import json
import requests
from bs4 import BeautifulSoup
#import cchardet




def getStuName(username, password):
    response = requests.get(f"https://homeaccesscenterapi.vercel.app/api/name?link=https://homeaccess.katyisd.org/&user={username}&pass={password}")
    x = response.json()
    if 'name' in x:
        return x['name']
    else:
        #print(x)
        return 'Invalid User or Pass'
    

def callAverages(login_data):
    with requests.Session() as session:
        login_url = "https://homeaccess.katyisd.org/HomeAccess/Account/LogOn"
        r = session.get(login_url)
        soup = BeautifulSoup(r.content, 'lxml')
        login_data['__RequestVerificationToken'] = soup.find('input', attrs={'name': '__RequestVerificationToken'})['value']
        post = session.post(login_url, data=login_data)
        classes = []
        averages = []
        assignments = session.get('https://homeaccess.katyisd.org/HomeAccess/Content/Student/Assignments.aspx')
        content = BeautifulSoup(assignments.text, 'lxml')

        for x in content.find_all('div', class_='AssignmentClass'):

            header = x.find('div', class_="sg-header")
            q = header.find('a', class_='sg-header-heading').text.strip()[12:]
            w = header.find('span', class_='sg-header-heading')
            classes.append(q.strip())
            averages.append(w.text.strip()[18:])

        ret = {}
        for i in range(len(classes)):
            ret[classes[i]] = averages[i]
        
        if len(ret) == 0:
            return None

        return ret

def getAverages(user, passw):
    username = user
    password = passw
    payload = {
    '__RequestVerificationToken' : '',
    'SCKTY00328510CustomEnabled' : True,
    'SCKTY00436568CustomEnabled' : True,
    'Database' : 10,
    'VerificationOption' : 'UsernamePassword',
    'LogOnDetails.UserName' : username,
    'tempUN' : '',
    'tempPW' : '',
    'LogOnDetails.Password' : password
    }
    result = callAverages(payload)
    #print(result)
    classes = [] 
    for x in result:
        classes.append(x)
    for x in result:
        if(result[x] == ""):
            classes.append("0.0")
        else:
            #print(result[x])
            classes.append(result[x]) 
    return classes