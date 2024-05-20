from django.shortcuts import render

# Create your views here.
def chatapp(request):
    return render(request, 'index.html')