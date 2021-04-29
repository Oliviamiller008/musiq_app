from django.test import TestCase
from musiq.spotifyAPI import create_playlist
from musiq.spotifyAPI import authorize_user
# Create your tests here.
#For testing our system

class MusiqTests(TestCase):

#tests that authorize user opens correct url
    def test_authorize_user(self):
        testurl = authorize_user()
        self.assertEqual(testurl, 'https://accounts.spotify.com/authorize?client_id=d7152a4d370b484c9635c7ad12ccfde2&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fquestion1%2F&scope=playlist-modify-public&show_dialog=True')

#tests that create playlist creates unique playlist id of length 22
    def test_create_playlist(self):
        playlist_id = create_playlist()
        self.assertEqual(len(playlist_id), 22)
    