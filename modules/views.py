from django.shortcuts import render
from.models import Review,Contact

# Create your views here.

def home(request):
    return render(request,'modules/home.html')


def suggest(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sug = request.POST['suggestions']
        suggestvar = Review(name=name, email=email, sug=sug)
        suggestvar.save()

    return render(request,'modules/home.html')


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        comments = request.POST['comments']
        contact = Contact(name=name, email=email, phone=phone, address=address, comments=comments)
        contact.save()

    return render(request,'modules/contact.html')



def projects(request):
    return render(request,'modules/projects.html')