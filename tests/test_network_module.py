import unittest
from unittest.mock import patch, AsyncMock
from src.network import network_module
from src.config import config_loader
from hypothesis import given, strategies as st
import asyncio

class TestNetworkModule(unittest.TestCase):
    def setUp(self):
        self.config = config_loader.load_config("config/config.yaml")
        self.network_handler = network_module.create_network_handler(self.config)

    @given(st.text())
    @patch('aiohttp.ClientSession.get')
    def test_send_request_success_property(self, mock_get, response_text):
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.text = AsyncMock(return_value=response_text)
        mock_get.return_value = mock_response

        url = "http://test.com"
        response = asyncio.run(self.network_handler.send_request(url))
        self.assertEqual(response, response_text)

    @patch('aiohttp.ClientSession.get')
    def test_send_request_failure(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status = 404
        mock_get.return_value = mock_response

        url = "http://test.com"
        response = asyncio.run(self.network_handler.send_request(url))
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
