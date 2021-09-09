import requests
from bs4 import BeautifulSoup
alfalist=['b','c','d','d','e','f','g','h','i','j','k']
skills_data=[]
for alpha in alfalist:
    url='https://www.zippia.com/computer-and-mathematical-industry/alpha/'
    webpage=requests.get(url,'html.parser')
    soup=BeautifulSoup(webpage.content,features='lxml')
    skills=soup.find_all(attrs={'class':'list-link'})

    
    for skill in (skills):
        skill=skill.get_text()
        skill=skill.replace(". ","")
        skill=skill.replace(" ","-")
        skill=skill.replace("/","-")
        skill=skill.lower()
        skill=skill+"-jobs"
        skills_data.append(skill)

print(skills_data)