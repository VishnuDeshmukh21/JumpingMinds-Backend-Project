from django.shortcuts import render

# Create your views here.
# elevator_system/frontend/views.py
from django.shortcuts import render

def elevator_status_man(request):
    return render(request, 'frontend/index.html')
