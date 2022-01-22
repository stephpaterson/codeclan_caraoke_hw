import unittest
import pdb

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Rock Classics", 6)
        self.guest = Guest("Kerry", 50, "Bohemian Rhapsody", "Queen")
        self.song = Song("Bohemian Rhapsody", "Queen")
        self.song_1 = Song("Livin' on a prayer", "Bon Jovi")

    # Test room has a name
    # Test you can add a song to the list
    # Test you can add a guest to the room
    # Test you can remove a guesst from the room
    # Test you can remove a guest by name from the room

    # Extension - test room capacity
    # Extension - test people can pay
    

    def test_room_has_name(self):
        self.assertEqual("Rock Classics", self.room.name)

    def test_add_song_to_list(self):
        # pdb.set_trace()
        self.room.add_song_to_room(self.song)
        self.assertEqual("Bohemian Rhapsody", self.room.songs[0].name)

    def test_add_guest_to_room(self):
        self.room.add_individual_guest_to_room(self.guest.name)
        self.assertEqual("Kerry", self.room.guests[0])

    def test_remove_all_guests_from_room(self):
        self.room.add_individual_guest_to_room(self.guest.name)
        self.room.remove_all_guests_from_room()
        self.assertEqual(len(self.room.guests), 0)

    def test_remove_guest_by_name_from_room(self):
        self.room.add_individual_guest_to_room(self.guest.name)
        self.room.remove_guest_by_name(self.guest.name)
        self.assertEqual(len(self.room.guests), 0)

    def test_decline_if_room_full(self):
        self.room.add_individual_guest_to_room(self.guest.name)
        self.room.add_individual_guest_to_room(self.guest.name)
        self.room.add_individual_guest_to_room(self.guest.name)
        self.room.add_individual_guest_to_room(self.guest.name)
        self.room.add_individual_guest_to_room(self.guest.name)
        self.room.add_individual_guest_to_room(self.guest.name)
        self.room.add_individual_guest_to_room(self.guest.name)
        self.assertEqual("Sorry, room full", self.room.capacity_check())

    def test_add_money_to_till(self):
        self.room.add_money_to_till()
        self.assertEqual(110, self.room.till)

    def test_take_entry_fee_from_guest(self):
        self.room.take_entry_fee_from_guest(self.guest)
        self.assertEqual(110, self.room.till)
        self.assertEqual(40, self.guest.wallet)
       
    def test_full_check_in_guest_sequence(self):
        self.room.full_check_in_guest_sequence(self.guest)
        self.room.add_individual_guest_to_room(self.guest.name)
        self.assertEqual("Kerry", self.room.guests[0])
        self.assertEqual(110, self.room.till)
        self.assertEqual(40, self.guest.wallet)