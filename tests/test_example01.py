from unittest import TestCase
try:
    from unittest import mock
except ImportError:
    import mock
from curso.example01 import mi_funcion2


class TestMiFuncion(TestCase):

    @mock.patch('curso.example01.mi_funcion')
    def test_get_text(self, mocked_response):
        mocked_response.return_value = 'mi_mock'
        response = mi_funcion2()
        self.assertEqual(response, 'mi_mock')
