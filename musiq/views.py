from django.shortcuts import render #used to render html templates
from .forms import CHOICES
from .forms import OPTIONS
#from musiq.models import Quiz
from django.shortcuts import render
from musiq.spotifyAPI import create_playlist
from musiq.spotifyAPI import authorize_user
from django.http import HttpResponse

# Create your views here.
#This file takes web request and creates a web reponse in the form of HTML pages that the browers can display

def homepage(request):
    return render(request, 'musiq/homepage.html')

def login(request):
    authorize_user()
    return HttpResponse(status =200)

def question1(request):
    if request.method == 'POST':
        #CREATE FORM INSTANCE AND POPULATE WITH DATA FROM REQUEST
        form = OPTIONS(request.POST)
        return render(request, 'question1.html', {'question1answer': question1answer})

    return render(request, 'musiq/question1.html')

#def question1answer(request):
   
 #   if request.method == 'POST':
        #CREATE FORM INSTANCE AND POPULATE WITH DATA FROM REQUEST
  #      form = OPTIONS(request.POST)

   # return render(request, 'question1.html', {'question1answer': question1answer})

        #if 'submit_button' in request.form:
        #    user_answer = request.form['QUESTION1_CHOICES']
        

  #  if form.is_valid():
  #      question1_answer=form.cleaned_data.get("QUESTION1_CHOICES")
  #      print(selected)
        
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
    


