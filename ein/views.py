from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .models import User, Plant
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
import square
from square.client import Client
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.views.generic.base import TemplateView 
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class process_payment(TemplateView):
    template_name = "process_payment.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): 
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount =500,
            currency= 'usd',
            description= 'A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')

@login_required
def index(request):

    allplants = Plant.objects.all()

    return render (request, "index.html" , {"allplants":allplants})

@login_required
def add_new_plant(request):
    if request.method== "GET": 
        if request.user.id == 6 :
            return render (request, "add_new.html")
        else :
            return render (request, "error.html")

    else: 
        name_plant = request.POST["name_plant"] 
        Description = request.POST["Description"] 
        Price = request.POST["Price"] 
        Image = request.POST["Image"] 
        Region = request.POST["Region"] 
        plant_data = Plant(name = name_plant, description = Description, price = Price, image = Image, region = Region)
        plant_data.save()

        return HttpResponseRedirect(reverse("index"))


# Do post method and payment

@login_required
def addcart(request):

    if request.method== "POST": 
        plant_id = request.POST["plant_id"] 
        plant_data = Plant.objects.get(id = plant_id)

        return render (request, "cart.html" , {"plant":plant_data})


# Create your views here.
def register(request):
    
    if request.method== "GET": 
        return render (request, "register.html")
    
    else :
        first_name = request.POST["fname"] 
        last_name = request.POST["lname"] 
        email = request.POST["email"] 
        password = request.POST["password"] 
        confirm = request.POST["confirm"] 

        if password != confirm:
            return render (request, "register.html" ,{"message": "Passwords do not match"  })
        
        try :
            user = User.objects.create_user( username = email, email = email , password = password , first_name = first_name , last_name = last_name)
            user.save()

        except : 
            return render (request, "register.html" ,{"message": "Something went wrong"  })
        
        login (request, user)

        return HttpResponseRedirect(reverse('index'))
    
# Create your login here.
def login_view(request):
    
    if request.method== "GET": 
        return render (request, "login.html")
    
    else :
        email = request.POST["email"] 
        password = request.POST["password"]  
        
        try :
            user = authenticate(request, username=email, password=password)

        except : 
            return render (request, "login.html" ,{"message": "Something went wrong"  })
        
        login (request, user)

        return HttpResponseRedirect(reverse('index'))

def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse('login_view'))







    

