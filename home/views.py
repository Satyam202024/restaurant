from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'servics.html')

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        number = request.POST.get('number')
        pcode = request.POST.get('pcode')
        address= request.POST.get('address')
        contact = Contact(name=name,number=number,pcode=pcode,address=address)
        contact.save()

    return render(request, 'contact.html')

