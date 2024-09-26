# Sample tests

from django.test import SimpleTestCase
from app import add

class AddTest(SimpleTestCase):
    def test_add(self):
        res = add.add(7,6)
        self.assertEqual(res, 11)