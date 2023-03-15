from django.shortcuts import render

# Create your views here.

def index(request) : 
    
    return render(request , "tempTag/index.html")

def other(request) : 
    
    return render(request , "temptag/other.html")

def relative(request) : 
    
    return render(request , "tempTag/relative.html")


