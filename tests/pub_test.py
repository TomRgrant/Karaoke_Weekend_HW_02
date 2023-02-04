import unittest
from src.room import Room
from src.guest import Guest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Boar Hat", {"pint": {"price": 4.00},
                                    "cocktail": {"price": 7.00},
                                    "fizzy": {"price": 3.00},
                                    "wine": {"price": 6.00}} )

    def test_has_name(self):
        expected = "Boar Hat"
        actual = self.pub.name
        self.assertEqual(expected, actual)

    def test_has_drinks(self):
        expected = 4
        actual = len(self.pub.drinks)
        self.assertEqual(expected, actual)