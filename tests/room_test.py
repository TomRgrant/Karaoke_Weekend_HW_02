import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(5, 10, 3)

    def test_has_room_number(self):
        expected = 5
        actual = self.room.room_num
        self.assertEqual(expected, actual)

    def test_has_total_population(self):
        expected = 10
        actual = self.room.total_pop
        self.assertEqual(expected, actual)