from django.test import TestCase
from unittest.mock import patch
from .views import get_crypto_data


class GetCryptoDataTests(TestCase):
    @patch('bitcoin.views.requests.get')
    def test_returns_empty_list_on_exception(self, mock_get):
        mock_get.side_effect = Exception('API error')
        self.assertEqual(get_crypto_data(), [])
