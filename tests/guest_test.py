import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("James", "Corden", 50.00, Song("Let It Be", " Beatles"))

    def test_has_name(self):
        expected = "James"
        actual = self.guest.first_name
        self.assertEqual(expected, actual)