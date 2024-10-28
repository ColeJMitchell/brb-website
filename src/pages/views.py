from django.shortcuts import render

def home(request):
    if request.method == "POST":
        return render(request, "home.html")
    return render(request, 'home.html')

def communities(request):
    if request.method == "POST":
        return render(request, "communities.html")
    
def aboutus(request):
    if request.method == "POST":
        return render(request, "aboutus.html")

def food(request):
    if request.method == "POST":
        return render(request, "food.html")

def healthcare(request):
    if request.method == "POST":
        return render(request, "healthcare.html")

def schools(request):
    if request.method == "POST":
        return render(request, "schools.html")

def events(request):
    if request.method == "POST":
        return render(request, "events.html")