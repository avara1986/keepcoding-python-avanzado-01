from unittest import TestCase

from mock import Mock, patch

from curso.example02 import get_animal


class TestGetAnimal(TestCase):

    @patch('requests.get')
    def test_get_animal_server_error_raises_exception(self, mock_get):
        mocked_response = Mock()
        mocked_response.status_code = 500
        mock_get.return_value = mocked_response
        with self.assertRaises(Exception):
            get_animal("test", 100)
