from django.shortcuts import render

# Create your views here.
# elevator_system/frontend/views.py
from django.shortcuts import render

def elevator_status(request):
    return render(request, 'frontend/index.html')
