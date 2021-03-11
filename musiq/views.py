from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'musiq/homepage.html')

def question1(request):
    return render(request, 'musiq/question1.html')