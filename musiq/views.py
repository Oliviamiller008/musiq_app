from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'musiq/homepage.html')

def Question2(request);
    return render(request, 'musiq/question2.html')