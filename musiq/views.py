from django.shortcuts import render #used to render html templates
from .forms import CHOICES
from .forms import OPTIONS
#from musiq.models import Quiz
from django.shortcuts import render
from musiq.spotifyAPI import create_playlist
from musiq.spotifyAPI import authorize_user
from musiq.spotifyAPI import add_song
from django.http import HttpResponse

# Create your views here.
#This file takes web request and creates a web reponse in the form of HTML pages that the browers can display

def homepage(request):
    return render(request, 'musiq/homepage.html')

def login(request):
    authorize_user()
    return HttpResponse(status =200)

 
def question1(request):
    playlist_id = create_playlist()
    if request.method == 'POST':
        answer1 = request.POST.get("group1")
        song = ['6rqhFgbbKwnb9MLmUQDhG6']
        if(answer1 == 'q1op1'):
            add_song(playlist_id, song)

 
    return render(request, 'musiq/question1.html')


def question2(request):
    if request.method == 'POST':
        answer2 = request.POST.get("group2")
      
    return render(request, 'musiq/question2.html')
        
def question3(request):

    if request.method == 'POST':
        answer3 = request.POST.get("group3")
        
    return render(request,'musiq/question3.html')

def question4(request):
    if request.method == 'POST':
        answer4 = request.POST.get("group4")
      
    return render(request, 'musiq/question4.html')

def question5(request):
    if request.method == 'POST':
        answer5 = request.POST.get("group5")
        
    return render(request, 'musiq/question5.html')

def endingpage(request):
    return render(request, 'musiq/endingpage.html')


    


