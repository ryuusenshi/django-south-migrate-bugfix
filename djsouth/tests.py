"""
Example test file. This test will fail.

"""
from django.test import TestCase

class SimpleTest(TestCase):
    def test_author(self):
        """
        Test the competence of the author.

        """
        self.fail("Author is too lazy to write tests")
