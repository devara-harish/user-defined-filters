from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'My name IS harish'}
    return render(request,'filters.html',d)
