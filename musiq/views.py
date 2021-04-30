from django.shortcuts import render #used to render html templates
from django.shortcuts import render
from musiq.spotifyAPI import create_playlist
from musiq.spotifyAPI import authorize_user
from musiq.spotifyAPI import add_song
from musiq.spotifyAPI import song_dict
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
        request.session['answer1'] = request.POST.get("group1")

    return render(request, 'musiq/question1.html')


def question2(request):
    
    if request.method == 'POST':
        request.session['answer2'] = request.POST.get("group2")
      
    return render(request, 'musiq/question2.html')
        
def question3(request):

    if request.method == 'POST':
        request.session['answer3'] = request.POST.get("group3")
        
    return render(request,'musiq/question3.html')

def question4(request):
    if request.method == 'POST':
        request.session['answer4'] = request.POST.get("group4")
      
    return render(request, 'musiq/question4.html')

def question5(request):
    if request.method == 'POST':
        request.session['answer5'] = request.POST.get("group5")
        
    return render(request, 'musiq/question5.html')

def endingpage(request):
    
    playlist_id = create_playlist()
    answer1 = request.session['answer1']
    answer2 = request.session['answer2']
    answer3 = request.session['answer3']
    answer4 = request.session['answer4']
    answer5 = request.session['answer5']


    # add the songs based on question 1 answer
    if(answer1 == 'q1op1'):
        add_song(playlist_id, song_dict['You Make my Dreams Come True'])
        add_song(playlist_id, song_dict['Come On Eileen'])

    elif(answer1 == 'q1op2'):
        add_song(playlist_id, song_dict['The Lazy Song'])
        add_song(playlist_id, song_dict['Landslide'])
            
    elif(answer1 == 'q1op3'):
        add_song(playlist_id, song_dict['The Take Over, The Breaks Over'])
        add_song(playlist_id, song_dict['All Apologies'])
    else:
        add_song(playlist_id, song_dict['River'])
        add_song(playlist_id, song_dict['Daylight']) 
    
    # add songs based on question 2
    if(answer2 == 'q2op1'):
        add_song(playlist_id, song_dict['Beginning Middle End'])
        add_song(playlist_id, song_dict['Shallow'])

    elif(answer2 == 'q2op2'):
        add_song(playlist_id, song_dict['All The Time'])
        add_song(playlist_id, song_dict['Work Song'])
            
    elif(answer2 == 'q2op3'):
        add_song(playlist_id, song_dict['Disturbia'])
        add_song(playlist_id, song_dict['Gasolina'])
    else:
        add_song(playlist_id, song_dict['Barcelona'])
        add_song(playlist_id, song_dict['Galway Girl']) 
    
    #add songs based on question 3 answer
    if(answer3 == 'q3op1'):
        add_song(playlist_id, song_dict['Smells Like Teen Spirit'])
        add_song(playlist_id, song_dict['Somebody Like You'])

    elif(answer3 == 'q3op2'):
        add_song(playlist_id, song_dict['Summertime'])
        add_song(playlist_id, song_dict['Sincerity is Scary'])
            
    elif(answer3 == 'q3op3'):
        add_song(playlist_id, song_dict['A Thousand Miles'])
        add_song(playlist_id, song_dict['Piano Man'])
    else:
        add_song(playlist_id, song_dict['2009'])
        add_song(playlist_id, song_dict['You Raise Me Up']) 

    # add songs based on question 4 answers
    if(answer4 == 'q4op1'):
        add_song(playlist_id, song_dict['Yellow'])
        add_song(playlist_id, song_dict['Yellow Eyes'])

    elif(answer4 == 'q4op2'):
        add_song(playlist_id, song_dict['Little Black Dress'])
        add_song(playlist_id, song_dict['Blackbird'])
            
    elif(answer4 == 'q4op3'):
        add_song(playlist_id, song_dict['Blue Tacoma'])
        add_song(playlist_id, song_dict['Blue World'])
    else:
        add_song(playlist_id, song_dict['Gold Rush'])
        add_song(playlist_id, song_dict['Golden Days']) 
    
    #add songs based on question 5 answers
    if(answer5 == 'q5op1'):
        add_song(playlist_id, song_dict['Here Comes The Sun'])
        add_song(playlist_id, song_dict['Story Of My Life'])

    elif(answer5 == 'q5op2'):
        add_song(playlist_id, song_dict['Life Changes'])
        add_song(playlist_id, song_dict['Seven Summers'])
            
    elif(answer5 == 'q5op3'):
        add_song(playlist_id, song_dict['Youre The Inspiration'])
        add_song(playlist_id, song_dict['Hey There Delilah'])
    else:
        add_song(playlist_id, song_dict['Green Light'])
        add_song(playlist_id, song_dict['Dream']) 

    return render(request, 'musiq/endingpage.html')


    


