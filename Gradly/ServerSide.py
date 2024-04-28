import json
import requests



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
        return 'Invalid User or Pass'
    
def getStuClasses(username, password):
    response =  requests.get(f"https://homeaccesscenterapi.vercel.app/api/ipr?link=https://homeaccess.katyisd.org/&user={username}&pass={password}")
    x = response.json()
    