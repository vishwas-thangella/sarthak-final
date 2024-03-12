from django.contrib import admin
from myapp.models import PersonalDetails
from myapp.models import Education
from myapp.models import Experiences
from myapp.models import AchivementsModel,Publications,Affiliations


class MyModelAdmin(admin.ModelAdmin):
  list_display = ('name', 'address', 'email','profile')

class MyModelEducation(admin.ModelAdmin):
  list_display = ('year','name','location')

class ExperienceModel(admin.ModelAdmin):
  list_display = ('name','designation','timePeriod')

class Achivement(admin.ModelAdmin):
  list_display = ("name","year","location")

class PublicationsSection(admin.ModelAdmin):
  list_display = ("desc","year")

class AffiliationsSec(admin.ModelAdmin):
  list_display = ("association","data","reg","date")

admin.site.register(PersonalDetails, MyModelAdmin)
admin.site.register(Education,MyModelEducation)
admin.site.register(Experiences,ExperienceModel)
admin.site.register(AchivementsModel,Achivement)
admin.site.register(Publications,PublicationsSection)
admin.site.register(Affiliations,AffiliationsSec)
