import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("James", "Corden", 50.00, Song("Let It Be", " Beatles"))

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