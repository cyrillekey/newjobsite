from bs4 import BeautifulSoup
import requests
import json

jobs=['administrator-jobs','business-analyst-jobs','data-engineer-jobs','data-scientist-jobs','developer-jobs','devops-engineer','information-technology-project-manager-jobs','information-technology-specialist-jobs','java-developer-jobs','lead-technician-jobs','network-engineer-jobs','principal-software-engineer-jobs','security-engineer-jobs','senior-software-development-engineer-jobs','senior-oftware-engineer-jobs','senior-systems-engineer-jobs','software-developer-jobs','software-development-engineer-jobs','software-engineer-jobs','software-engineer-lead-jobs','software-engineering-manager-jobs','solutions-architect-jobs','specialist-jobs','staff-software-engineer-jobs','support-jobs','support-associate-jobs','support-specialist-jobs','systems-administrator-jobs','systems-engineer-jobs','technical-support-specialist-jobs']
for job in jobs:
    #get the job
    url='https://www.zippia.com/'+job+'/'
    webpage=requests.get(url,'html.parser')
    soup=BeautifulSoup(webpage.content,features='lxml')
    result=soup.find(attrs={'id':'whatTheyDo'})
    description=result.get_text()
    salary=soup.find(attrs={'class':'average-salary-num'})
    name=job.replace("-"," ")
    name=name.replace('jobs',".")
    salary=salary.get_text()
    #get the needed skills for the job
    url='https://www.zippia.com/administrator-jobs/skills/'
    webpage=requests.get(url,'html.parser')
    soup=BeautifulSoup(webpage.content,features='lxml')
    skills=soup.find_all(attrs={'class':'skillNameText'})
    
    skills_data=[]
    education_data=[]
    for skill in (skills):
        skill=skill.get_text()
        skill=''.join(i for i in skill if not i.isdigit())
        skill=skill.replace(". ","")
        skills_data.append(skill)


    url='https://www.zippia.com/administrator-jobs/education/'
    webpage=requests.get(url,'html.parser')
    soup=BeautifulSoup(webpage.content,features='lxml')
    educations=soup.find_all(attrs={'class':'certification-title'})
    
    education_data=[]
    for education in educations:
        education=education.get_text()
        education=''.join(i for i in education if not i.isdigit())
        education=education.replace(". ","")
        education_data.append(education)    
    #get the most commmon needed education requirements     
    print(education_data)
    #print(name)
    #print(description)
    #print(salary)