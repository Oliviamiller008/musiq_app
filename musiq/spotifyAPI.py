import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth 
from spotipy import util
import webbrowser

client_id = 'd7152a4d370b484c9635c7ad12ccfde2'
client_secret = 'e5e56c343d9d495d9063511aa8ece62d'
redirect_uri = 'http://127.0.0.1:8000/question1/'
scope = 'playlist-modify-public'
auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scope,client_id = client_id, client_secret = client_secret, redirect_uri = redirect_uri, show_dialog=True)
sp = spotipy.Spotify(auth_manager=auth_manager)


#brings user to authentication page
def authorize_user():
    auth_manager = spotipy.oauth2.SpotifyOAuth(scope=scope,client_id = client_id, client_secret = client_secret, redirect_uri = redirect_uri, show_dialog=True)
    auth_url = auth_manager.get_authorize_url()
    webbrowser.open(auth_url)
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



