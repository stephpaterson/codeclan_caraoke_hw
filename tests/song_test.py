import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Bohemian Rhapsody", "Queen")

    def test_song_has_name(self):
        self.assertEqual("Bohemian Rhapsody", self.song.name)