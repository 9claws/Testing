from unittest import TestCase
from YandexTests import create_folder

class TestApi(TestCase):
    def test_creation_folder_1(self):
        response = create_folder('Папка')
        expected = 201
        self.assertEqual(response, expected)


    def test_creation_folder_2(self):
        response = create_folder('Папка')
        expected = 409
        self.assertEqual(response, expected)