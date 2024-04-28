import json
import requests
from bs4 import BeautifulSoup



def fetch_student_classes(username, password):
    
    data = {
        'link': "https://homeaccess.katyisd.org/",
        'username': username,
        'password': password
    }
 
    url = 'https://homeaccesscenterapi.vercel.app/api/classes?link=https://homeaccess.katyisd.org/&user='+username+'&pass='+password
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()


        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

# username = input('username: ')
# password = input('password: ')

#fetch_student_classes(username, password)

# 'user' : username
# 'pass' : password
# 'route' : 'Classes'
# 
# response =  requests.get(f"https://homeaccesscenterapi.vercel.app/api/ipr?link=https://homeaccess.katyisd.org/&user={username}&pass={password}")
# print(response.json())

def getStuName(username, password):
    response = requests.get(f"https://homeaccesscenterapi.vercel.app/api/name?link=https://homeaccess.katyisd.org/&user={username}&pass={password}")
    x = response.json()
    if 'name' in x:
        return x['name']
    else:
        print(x)
        return 'Invalid User or Pass'
    
# def getStuClasses(username, password):
#     response =  requests.get(f"https://homeaccesscenterapi.vercel.app/api/ipr?link=https://homeaccess.katyisd.org/&user={username}&pass={password}")
#     x = response.json()
#     mainList = x['data']
#     classList = []
#     for row in mainList:
#         for col in row:
#             if(mainList[mainList.index(row)] > -1 and mainList[mainList.index(row)] < 6):
#                 classList+=col
#     print(classList)

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
    '__RequestVerificationToken' : 'WhTfwATBjQRvM7y07dev-d3B7v9qhU9pReGjcehgFTyc0G-CSIYcb_htbFDaxqoY0rJwsgmKmVdLfri6d9KxV5xSmUUFB6xmN8yFN7sfmVI1',
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
        if(result[x] == ""):
            classes.append("{:<25}{:>8}".format(x, "0"))
        else:
            classes.append("{:<25}{:>8}".format(x, result[x])) 
    return classes
