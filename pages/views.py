from django.shortcuts import render


def Home(request):
    return render(request, 'pages/home.html')
# Create your views here.
