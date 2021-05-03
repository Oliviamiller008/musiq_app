import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth 
from spotipy import util
import webbrowser

client_id = 'd7152a4d370b484c9635c7ad12ccfde2' #given at registration of application
client_secret = 'e5e56c343d9d495d9063511aa8ece62d' 
redirect_uri = 'http://127.0.0.1:8000/question1/' #where user gets directed to after login
response_type = "code" #how to know if the request went through or if an error occured
scope = 'playlist-modify-public' #what type of authorization is given
auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scope,client_id = client_id, client_secret = client_secret,redirect_uri = redirect_uri, show_dialog=True)
sp = spotipy.Spotify(auth_manager=auth_manager)


#Dictionary of all the track ids we are using 
song_dict = {
    'You Make my Dreams Come True' : ['4o6BgsqLIBViaGVbx5rbRk'],
    'Come On Eileen' : ['3MrWxJaD2AT0W9DjWF64Vm'],
    'The Lazy Song' : ['1ExfPZEiahqhLyajhybFeS'],
    'Landslide' : ['5ihS6UUlyQAfmp48eSkxuQ'],
    'The Take Over, The Breaks Over' : ['3rG8ZkmKHb4Ms6CsSzEITv'],
    'All Apologies' : ['1Ic9pKxGSJGM0LKeqf6lGe'],
    "River" : ['3hhbDnFUb2bicI2df6VurK'],
    'Daylight' : ['7ryS0xBZNYjQqql34GCkDp'],
    'Beginning Middle End' : ['2kFHjWko1il6O9L3eK9IzG'],
    'Shallow' : ['2VxeLyX666F8uXCJ0dZF8B'],
    'All The Time' : ['0qI1W6chJgvrSAzAkX9JBa'],
    'Work Song' : ['5TgEJ62DOzBpGxZ7WRsrqb'],
    'Disturbia' : ['2VOomzT6VavJOGBeySqaMc'],
    'Gasolina' : ['6jEZLz3YpnEBRpVkv35AmP'],
    'Barcelona' : ['3ieLey98V9mIIh3W9gBlPF'],
    'Galway Girl' : ['0afhq8XCExXpqazXczTSve'],
    'Smells Like Teen Spirit' : ['5ghIJDpPoe3CfHMGu71E6T'],
    'Somebody Like You' : ['0b9djfiuDIMw1zKH6gV74g'],
    'Summertime' : ['2gNjmvuQiEd2z9SqyYi8HH'],
    'Sincerity is Scary' : ['6HguG9HRb1Ke1bhihfE4m8'],
    'A Thousand Miles' : ['4w1lzcaoZ1IC2K5TwjalRP'],
    'Piano Man' : ['70C4NyhjD5OZUMzvWZ3njJ'],
    '2009' : ['6dFn6my1sHK2bcf23GlHwM'],
    'You Raise Me Up' : ['4TbNLKRLKlxZDlS0pu7Lsy'],
    'Yellow' : ['3AJwUDP919kvQ9QcozQPxg'],
    'Yellow Eyes' : ['3HOXNIj8NjlgjQiBd3YVIi'],
    'Little Black Dress' : ['4lxaurdMyGkt1tOrdwRoVO'],
    'Blackbird' : ['5jgFfDIR6FR0gvlA56Nakr'],
    'Blue Tacoma' : ['5PBx0zFfehUMyv5H4YXVAU'],
    'Blue World' : ['2hwOoMtWPtTSSn6WHV7Vp5'],
    'Gold Rush' : ['4mT5mVFaU7trA3UdbGqfB9'],
    'Golden Days' : ['3fwKVZ73y7UUGMyR6rVCRa'],
    'Here Comes The Sun' : ['6dGnYIeXmHdcikdzNNDMm2'],
    'Story Of My Life' : ['4nVBt6MZDDP6tRVdQTgxJg'],
    'Life Changes' : ['4Vxu50qVrQcycjRyJQaZLC'],
    'Seven Summers' : ['0tbjiOUl4k492KPdWZS9sy'],
    'Youre The Inspiration' : ['1sUQJeihi2iSAQOXtxRjkz'],
    'Hey There Delilah' : ['4RCWB3V8V0dignt99LZ8vH'],
    'Green Light' : ['6ie2Bw3xLj2JcGowOlcMhb'],
    'Dream' : ['3Txe8uB20MQ7psuOoCbAW7']

}

#brings user to authentication page
def authorize_user():
    #if(response_type == "some valid authentication reponse?")
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scope,client_id = client_id, client_secret = client_secret,redirect_uri = redirect_uri, show_dialog=True)
    auth_url = auth_manager.get_authorize_url()
    webbrowser.open(auth_url)
    # elseif(response_type == "access_denied"){
        #cancel the request
    #}
    
    return auth_url

#creates a playlist called "Your MUSIQ Playlist" and returns playlist id
def create_playlist():  
    playlist_name = "Your MUSIQ Playlist"
    user_id = sp.me()['id']
    print('creating playlist')
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name,public=True)
    json_string = json.dumps(playlist, indent=4)
    data = json.loads(json_string)
    playlist_id = (data["id"])
    return playlist_id
 
#adds a song to the created playlist 
def add_song(playlist_id, track_id):
    user_id = sp.me()['id']
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_id, position=None)

def open_playlist(playlist_id):
    results = sp.playlist(playlist_id)
    print(json.dumps(results, indent=4))