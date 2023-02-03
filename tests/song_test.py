import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("The Drug In Me Is You", "Falling In Reverse")

    def test_has_title(self):
        expected = "The Drug In Me Is You"
        actual = self.song.title
        self.assertEqual(expected, actual)


