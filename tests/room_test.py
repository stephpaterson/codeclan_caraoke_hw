import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Rock Classics")
        self.guest = Guest("Kerry", 50)
        self.guest_1 = Guest("Rosie", 25)
        self.song = Song("Bohemian Rhapsody", "Queen")

    # Test room has a name
    # Test you can add a song to the list
    # Test you can add a guest to the room
    # Test you can remove a guesst from the room
    # Test you can remove a guest by name from the room
    

    def test_room_has_name(self):
        self.assertEqual("Rock Classics", self.room.name)

    def test_add_song_to_list(self):
        self.room.add_song_to_room(self.song.name)
        self.assertEqual("Bohemian Rhapsody", self.room.songs[0])

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest.name)
        self.assertEqual("Kerry", self.room.guests[0])

    def test_remove_all_guests_from_room(self):
        self.room.add_guest_to_room(self.guest.name)
        self.room.remove_all_guests_from_room()
        self.assertEqual(len(self.room.guests), 0)

    def test_remove_guest_by_name_from_room(self):
        self.room.add_guest_to_room(self.guest.name)
        self.room.add_guest_to_room(self.guest_1.name)
        self.room.remove_guest_by_name(self.guest.name)
        self.assertEqual(len(self.room.guests), 1)
   