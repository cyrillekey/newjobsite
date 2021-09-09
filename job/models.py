from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch import receiver 
# Create your models here.
#function to store the thumbnail of the image
def upload_location(instance,filname):
    file_path='displayjob/{job_id}/{job_name}-{filename}'.format(
        job_id=str(instance.job_id),job_name=str(instance.job_name),filename=filname
    )
    return file_path

#class to hold further reading materials and link to other reading materials
class materials_table(models.Model):
    material_id=models.CharField(max_length=50,null=False,blank=False,primary_key=True)
    material_name=models.CharField(max_length=50,null=False,blank=False)
    skill_gained=models.CharField(max_length=50,null=False,blank=False)
    material_type=models.CharField(max_length=50,null=False,blank=False)
    material_url=models.URLField(max_length=200)
    
    def __str__(self):
        return str(self.material_name)
#class to hold skills needed for a particular job
class Skill(models.Model):
    skill_id=models.CharField(max_length=25,null=False,blank=False,primary_key=True)
    skill_name=models.CharField(max_length=50,null=False,blank=False)
    skills_desc=models.CharField(max_length=50,null=False,blank=False)
    skill_type=models.CharField(max_length=50,null=False,blank=False)
    skill_material_id=models.ManyToManyField(materials_table,through='Material_skill')
    def __str__(self):
        return str(self.skill_name)
#many to many relationship between skills and materials
class Material_skill(models.Model):
    inter_material_id=models.ForeignKey(materials_table,on_delete=models.CASCADE)   
    inter_skills_id=models.ForeignKey(Skill,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.inter_skills_id)
    class Meta:
        unique_together=[['inter_material_id','inter_skills_id']]        
#class to hold the actual information for a job    
class Job(models.Model):
    job_id=models.CharField(max_length=50,null=False,blank=False,primary_key=True)
    job_name=models.CharField(max_length=50,null=False,blank=False)
    job_description=models.CharField(max_length=500,null=False,blank=False)
    job_thumnail=models.ImageField(upload_to=upload_location,default='displayjob/default/download.jpeg')
    job_average_salary=models.IntegerField()
    job_skill_id=models.ManyToManyField(Skill,through='Job_skill')
    slug=models.SlugField()
    job_education=models.JSONField()

    def __str__(self):
        return str(self.job_name)
#class to hold information about futher reading materials on the skills needed for the skill

#class holding information associated with a patricular job

#many to many relationship through which the relationship between skills and materials is maintained        


#class to hold the job and which skill is needed for the job
class Job_skill(models.Model):
    inter_job_id=models.ForeignKey(Job,on_delete=models.CASCADE)
    inter_skill_id=models.ForeignKey(Skill,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.inter_skill_id)
    class Meta:
        unique_together=[['inter_job_id','inter_skill_id']]
      