import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(5, 1, 3.00)

    def test_has_room_number(self):
        expected = 5
        actual = self.room.room_num
        self.assertEqual(expected, actual)

    def test_has_total_population(self):
        expected = 1
        actual = self.room.total_pop
        self.assertEqual(expected, actual)

    def test_has_entry_fee(self):
        expected = 3.00
        actual = self.room.entry_fee
        self.assertEqual(expected, actual)

    def test_add_guest_increase_room_population(self):
        self.guest = Guest("Frank", "Joel", 20.00, {"title": "Blame It On Me", "title": "George Ezra"})
        self.room.increase_room_pop(self.guest.first_name)
        expected = 1
        actual = len(self.room.room_pop)
        self.assertEqual(expected, actual)

    def test_add_guest_increase_room_population__room_full(self):
        self.guest_1 = Guest("Paul", "Kerona", 40.00, {"title": "Stand By Me", "artist": "Oasis"})
        self.guest_2 = Guest("Mark", "Peters", 10.00, {"title": "Dance Monkey", "artist": "Tones And I"})
        self.room_1 = Room(7, 1, 3.00)
        self.room.increase_room_pop(self.guest_1.first_name)
        expected = "Room is full"
        actual = self.room.increase_room_pop(self.guest_2.first_name)
        self.assertEqual(expected, actual)

    def test_play_song(self):
        song_to_play = {"title": 'Im Not A Vampire', "artist": 'Falling In Reverse'}
        self.room.play_song(song_to_play)
        expected = {"title": 'Im Not A Vampire', "artist": 'Falling In Reverse'}
        actual = self.room.song_queue[0]
        self.assertEqual(expected, actual)

    def test_remove_guest_from_room(self):
        self.guest = Guest("Frank", "Joel", 20.00, {"title": "Blame It On Me", "artist": "George Ezra"})
        self.room.increase_room_pop(self.guest.first_name)
        self.room.remove_guest_from_room(self.guest.first_name)
        expected = 0
        actual = len(self.room.room_pop)
        self.assertEqual(expected, actual)

    def test_room_multipe_songs_in_queue(self):
        song_to_play_1 = {"title": 'Im Not A Vampire', "artist": 'Falling In Reverse'}
        song_to_play_2 = {"title": "Blame It On Me", "artist": "George Ezra"}
        song_to_play_3 = {"title": "Dance Monkey", "artist": "Tones And I"}
        self.room.play_song(song_to_play_1)
        self.room.play_song(song_to_play_2)
        self.room.play_song(song_to_play_3)
        expected = 3
        actual = len(self.room.song_queue)