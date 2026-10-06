from django.shortcuts import render
from datetime import datetime

def name(request):
    d=datetime.now()
    return render(request,'payments-1.html',{'dt':d})

def lemon(request):
    return render(request,'payments-2.html')









