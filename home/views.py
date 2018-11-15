from django.shortcuts import render, redirect

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def test(request):
    return render(request, "test.html")

def facebook(request):
    return redirect("https://web.facebook.com/interiorworkskenya")
