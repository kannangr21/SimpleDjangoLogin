from django.shortcuts import render,redirect
from .models import Destination
from django.contrib import messages
# Create your views here.


def errorlog(request):
    messages.info(request,"Please login to view the content")
    return redirect("/")
    
def index(request):
    de1 = Destination()
    de1.place = "Trichy, Tamil Nadu"
    de1.desc = "Best part of life!!"
    de1.img = "tpj.jpg"
    de2 = Destination()
    de2.place = "Chennai, Tamil Nadu"
    de2.desc = "The Capital"
    de2.img = "chn.jpg"
    de3 = Destination()
    de3.place = "Salem, Tamil Nadu"
    de3.desc = "City of Mangoes"
    de3.img = "slm.jpg"
    objs = [de1,de2,de3]
    d="Thanks for visiting this Project! This is my first project using the framework 'DJANGO'"
    return render(request,"index.html",{'objs':objs,'descrip':d})
