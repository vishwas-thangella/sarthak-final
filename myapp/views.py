from django.shortcuts import render, HttpResponse, redirect
from myapp.models import PersonalDetails
from myapp.models import Education
from myapp.models import Experiences
from myapp.models import AchivementsModel,Affiliations,Publications
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):

    pdt = PersonalDetails.objects.all()

    print(pdt[0].profile.url,"is the url")

    data = {
        "personalDetails":pdt[0]
    }

    return render(request,"index.html",data)

def Services(request):
    edudet = Education.objects.all()
    experiences = Experiences.objects.all()
    affiliations = Affiliations.objects.all()
    publications = Publications.objects.all()
    data = {
        "Education":edudet,
        "Experiences":experiences,
        "Affiliations":affiliations,
        "Publications":publications
    }
    return render(request,"service.html",data)

def contact(request):
    details = PersonalDetails.objects.all()

    data = {
        'contact':details[0]
    }

    return render(request,"contact.html",data)

def Appointment(request):
    return render(request,"appointment.html")

def achivements(request):
    achivements = AchivementsModel.objects.all()

    data = {
        "achivements":achivements
    }

    return render(request,'achivements.html',data)
    