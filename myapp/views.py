from django.shortcuts import render

def index(request):
    # Base index view
    return render(request, 'index.html')