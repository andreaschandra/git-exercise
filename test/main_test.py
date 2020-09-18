"""
python test
"""
from unittest import TestCase

class TryTesting(TestCase):
    """
    Class for TryTesting
    """
    def test_always_passes(self):
        """
        unit test always passes
        """
        self.assertTrue("name".upper() == "NAME")

    def test_always_fails(self):
        """
        test always fails
        """
        self.assertTrue(3 != 4)
