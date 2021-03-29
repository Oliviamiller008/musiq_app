from django.shortcuts import render #used to render html templates
#from musiq.models import Quiz
from django.shortcuts import render
from musiq.spotifyAPI import create_playlist
from musiq.spotifyAPI import authorize_user
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'musiq/homepage.html')

def login(request):
    authorize_user()
    return HttpResponse(status =200)

def question1(request):
    create_playlist() 
    return render(request, 'musiq/question1.html')

    
def question2(request):
    return render(request, 'musiq/question2.html')
        
def question3(request):
    return render(request,'musiq/question3.html')

def question4(request):
    return render(request, 'musiq/question4.html')

def question5(request):
    return render(request, 'musiq/question5.html')

def endingpage(request):
    return render(request, 'musiq/endingpage.html')

#def musiqQuiz(request):
 #   results=Quiz.objects.all()
 #   return render(request, 'Question1.html', {"Quiz":results}) #be able to reference chosen results from quiz
    


