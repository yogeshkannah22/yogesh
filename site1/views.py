from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.

from django.http import HttpResponse

def index(request):
    print("first page")
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def ai(request):
    return render(request,"ai.html")

def ml(request):
    return render(request,"ml.html")

def nlp(request):
    return render(request,"nlp.html")

def dl(request):
    return render(request,"dl.html")

def web(request):
    return render(request,"web.html")


@csrf_protect
def signin(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        # Render the login page
        return render(request, 'signin.html')

