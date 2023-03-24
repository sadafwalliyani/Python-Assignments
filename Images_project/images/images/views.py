from django.shortcuts import render

def i_home(resuest):
    return render(resuest,'home.html')