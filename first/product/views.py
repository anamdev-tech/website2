from django.shortcuts import render



def cake(request):
    return render(request,'product.html')
