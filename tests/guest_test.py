import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.guest = Guest("Kerry", 50)
    
    def test_guest_has_name(self):
        self.assertEqual("Kerry", self.guest.name)

    def test_remove_money_from_wallet(self):
        self.guest.remove_money_from_wallet(10)
        self.assertEqual(40, self.guest.wallet)