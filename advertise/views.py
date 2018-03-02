from django.shortcuts import render

# Create your views here.
from advertise.entity.AdminUser import AdminPerson



def home(request):
    AdminPerson.objects.get(pd=1)
    return render(request, 'home.html')