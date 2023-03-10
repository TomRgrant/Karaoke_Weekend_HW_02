import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song
from src.pub import Pub

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("James", "Corden", 50.00, {"title": "Let It Be", "artist": "Beatles"})

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
        expected = {"title": "Let It Be", "artist": "Beatles"}
        actual = self.guest.fav_song
        self.assertEqual(expected, actual)

    def test_pay_entry_fee__sufficient_funds(self):
        entry_fee = 3.00
        self.guest.reduce_wallet(entry_fee)
        expected = 47.00
        actual = self.guest.wallet
        self.assertEqual(expected, actual)

    def test_pay_entry_fee__insufficient_funds(self):
        self.guest = Guest("Loid", "Forger", 4.00, {"title": "Mixed Nuts", "artist": "Official Hige Dandism"})
        entry_fee = 5.00
        self.guest.reduce_wallet(entry_fee)
        expected = 4.00
        actual = self.guest.wallet
        self.assertEqual(expected, actual)

    def test_playing_favourite_song(self):
        self.room = Room(9, 10,5)
        self.room.current_song = {"title": "Let It Be", "artist": "Beatles"}
        expected = "Whoo!"
        actual = self.guest.fav_song_playing(self.room.current_song)
        self.assertEqual(expected, actual)

    def test_buy_drink(self):
        self.guest = Guest("Loid", "Forger", 50.00, {"title": "Mixed Nuts", "artist": "Official Hige Dandism"})
        self.pub = Pub("Boar Hat", {"pint": {"price": 4.00},
                                    "cocktail": {"price": 7.00},
                                    "fizzy": {"price": 3.00},
                                    "wine": {"price": 6.00}} )
        self.guest.reduce_wallet(self.pub.drinks["fizzy"]["price"])
        expected = 47.00
        actual = self.guest.wallet
        self.assertEqual(expected, actual)

    def test_pay_entry_fee(self):
        self.guest = Guest("Loid", "Forger", 50.00, {"title": "Mixed Nuts", "artist": "Official Hige Dandism"})
        entry_fee = 5
        self.guest.reduce_wallet(entry_fee)
        expected = 45.00
        actual = self.guest.wallet
        self.assertEqual(expected, actual)

    def test_guest_pay_tab(self):
        self.room = Room(4, 11, 5)
        self.room.tab = 30
        self.guest = Guest("Loid", "Forger", 50.00, {"title": "Mixed Nuts", "artist": "Official Hige Dandism"})