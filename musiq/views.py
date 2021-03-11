from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'musiq/homepage.html')
<<<<<<< Updated upstream

def Question2(request);
    return render(request, 'musiq/question2.html')
=======
    
def question3(request):
    return render(request,'musiq/question3.html')
>>>>>>> Stashed changes
