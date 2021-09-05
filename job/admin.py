from django.contrib import admin
from .models import Job,Skill,materials_table,Material_skill,Job_skill
# Register your models here.

admin.site.register(Job)

admin.site.register(materials_table)

admin.site.register(Skill)
admin.site.register(Job_skill)
admin.site.register(Material_skill)
