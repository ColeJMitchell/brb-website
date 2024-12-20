from django.shortcuts import render
from django.conf import settings

def home(request):
    if request.method == "POST":
        return render(request, "home.html")
    return render(request, 'home.html')

def spanish_home(request):
    if request.method == "POST":
        return render(request, "spanish_home.html")
    return render(request, 'spanish_home.html')

def communities_networks(request):
    if request.method == "POST":
        return render(request, "communities_networks.html")

def communities_churches(request):
    if request.method == "POST":
        return render(request, "communities_churches.html")

def communities_forums(request):
    if request.method == "POST":
        return render(request, "communities_forums.html")
    
def aboutus(request):
    if request.method == "POST":
        return render(request, "aboutus.html")
    
def spanish_aboutus(request):
    if request.method == "POST":
        return render(request, "spanish_aboutus.html")
    return render(request, 'spanish_aboutus.html')

def food(request):
    if request.method == "POST":
        return render(request, "food.html")

def healthcare(request):
    if request.method == "POST":
        return render(request, "healthcare.html")

def schools(request):
    api_key = settings.MAP_API_KEY
    print(api_key)
    if request.method == "POST":
        return render(request, "schools.html", {"api_key": api_key})

def spanish_schools(request):
    api_key = settings.MAP_API_KEY
    print(api_key)
    if request.method == "POST":
        return render(request, "spanish_schools.html", {"api_key": api_key})

def events(request):
    if request.method == "POST":
        return render(request, "events.html")
    
