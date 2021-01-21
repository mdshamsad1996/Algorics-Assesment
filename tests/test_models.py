"""Unit Testing of Busioness logic"""

from unittest import TestCase
from unittest.mock import patch
from src.models import Models, rows


class TestModels(TestCase):
    """Test class for Models"""

    def setUp(self):
        """setup method"""
        self.mod = Models()

    def test_load_data(self):

        """unit testing of load_data method"""

        model = Models()

        model.load_data()

        actual = len(rows)

        expected = 100
        rows.clear()
        self.assertEqual(actual, expected)

    def test_provide_rating(self):

        """Unit tetse of provide_rating method"""

        model = Models()

        model.load_data()

        actual = model.provide_rating('shamsalam', 5)

        expected = {"message": "No song list found with provided id"}

        rows.clear()

        self.assertEqual(actual, expected)

    @patch('src.models.Models')
    def test_provide_rating_with_mocking(self, MockModels):

        """Unit test of provide_rating method with mocking object"""

        model = MockModels()  # create a mock object of Models class

        model.provide_rating.return_value = {"id": "5vYA1mW9g2Coh1HUFUSmlb", "star_ratoing": 3}

        actual = model.provide_rating("5vYA1mW9g2Coh1HUFUSmlb", 3)

        expected = {"id": "5vYA1mW9g2Coh1HUFUSmlb", "star_ratoing": 3}

        self.assertEqual(actual, expected)

    def test_get_songs_details_via_title(self):

        """Unit test of get_songs_details_via_titile method"""

        model = Models()

        model.load_data()

        actual = len(model.get_songs_details_via_title("3AM"))

        rows.clear()

        expected = 1

        self.assertEqual(actual, expected)

    def test_get_songs(self):

        """Unit test of get_songs method"""

        model = Models()

        model.load_data()

        fetched_record = model.get_songs(1, 1)

        actual = fetched_record[0]['id']

        expected = '5vYA1mW9g2Coh1HUFUSmlb'

        rows.clear()

        self.assertEqual(actual, expected)
