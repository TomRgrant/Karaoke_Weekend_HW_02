import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("James", "Corden", 50.00, "Let It Be", "Beatles")

    def test_has_first_name(self):
        expected = "James"
        actual = self.guest.first_name
        self.assertEqual(expected, actual)

    def test_has_last_name(self):
        expected = "Corden"
        actual = self.guest.last_name
        self.assertEqual(expected, actual)

    def test_has_wallet(self):
        expected = 50.00
        actual = self.guest.wallet
        self.assertEqual(expected, actual)

    def test_favourite_song(self):
        expected = "Let It Be", "Beatles"
        actual = self.guest.fav_song
        self.assertEqual(expected, actual)

    def test_pay_entry_fee__sufficient_funds(self):
        entry_fee = 3
        self.guest.pay_entry_fee(entry_fee)
        expected = 47.00
        actual = self.guest.wallet
        self.assertEqual(expected, actual)