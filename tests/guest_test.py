import unittest
import pdb

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.room = Room("Rock Classics", 6)
        self.song = Song("Bohemian Rhapsody", "Queen")
        self.song_1 = Song("Livin' on a prayer", "Bon Jovi")
        self.guest = Guest("Kerry", 50, "Bohemian Rhapsody", "Queen")
    
    def test_guest_has_name(self):
        self.assertEqual("Kerry", self.guest.name)

    def test_remove_money_from_wallet(self):
        self.guest.remove_money_from_wallet(10)
        self.assertEqual(40, self.guest.wallet)

    def test_favourite_song(self):
        # pdb.set_trace()
        self.room.add_song_to_room(self.song)
        fav_song_playing = self.guest.favourite_song_playing(self.room.songs)
        self.assertEqual("This is my favourite song!", fav_song_playing )

    def test_favourite_song_not_in_list(self):
        self.room.add_song_to_room(self.song_1)
        fav_song_playing = self.guest.favourite_song_playing(self.room.songs)
        self.assertEqual(False, fav_song_playing )

    def test_favourite_artist_in_list(self):
        self.room.add_song_to_room(self.song)
        fav_song_playing = self.guest.favourite_artist_playing(self.room.songs)
        self.assertEqual("I love Queen!", fav_song_playing )

    def test_least_favourite_artist_in_list(self):
        self.room.add_song_to_room(self.song_1)
        fav_song_playing = self.guest.favourite_artist_playing(self.room.songs)
        self.assertEqual("I hate Bon Jovi", fav_song_playing )