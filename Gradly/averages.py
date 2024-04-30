# import json
# import os
# import requests
# from bs4 import BeautifulSoup

# def getAverages(login_data, link):
#     with requests.Session() as session:
#         login_url = link+"HomeAccess/Account/LogOn"
#         r = session.get(login_url)
#         soup = BeautifulSoup(r.content, 'lxml')
#         login_data['__RequestVerificationToken'] = soup.find('input', attrs={'name': '__RequestVerificationToken'})['value']
#         post = session.post(login_url, data=login_data)
#         classes = []
#         averages = []
#         assignments = session.get(link+'HomeAccess/Content/Student/Assignments.aspx')
#         content = BeautifulSoup(assignments.text, 'lxml')

#         for x in content.find_all('div', class_='AssignmentClass'):

#             header = x.find('div', class_="sg-header")
#             q = header.find('a', class_='sg-header-heading').text.strip()[12:]
#             w = header.find('span', class_='sg-header-heading')
#             classes.append(q.strip())
#             averages.append(w.text.strip()[18:])

#         ret = {}
#         for i in range(len(classes)):
#             ret[classes[i]] = averages[i]
        
#         if len(ret) == 0:
#             return None

#         return ret
    

# link = "https://homeaccess.katyisd.org/"
# payload = {
#     '__RequestVerificationToken' : 'WhTfwATBjQRvM7y07dev-d3B7v9qhU9pReGjcehgFTyc0G-CSIYcb_htbFDaxqoY0rJwsgmKmVdLfri6d9KxV5xSmUUFB6xmN8yFN7sfmVI1',
#     'SCKTY00328510CustomEnabled' : True,
#     'SCKTY00436568CustomEnabled' : True,
#     'Database' : 10,
#     'VerificationOption' : 'UsernamePassword',
#     'LogOnDetails.UserName' : username,
#     'tempUN' : '',
#     'tempPW' : '',
#     'LogOnDetails.Password' : password
# }
# print(getAverages(payload,link))
