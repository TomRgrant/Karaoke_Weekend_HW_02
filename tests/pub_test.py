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