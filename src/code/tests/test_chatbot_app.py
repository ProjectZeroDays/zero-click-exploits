import unittest
from unittest.mock import patch, MagicMock
from src.chatbot.app import app, get_copilot_response

class TestChatbotApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('src.chatbot.app.get_copilot_response')
    def test_copilot_endpoint(self, mock_get_copilot_response):
        mock_get_copilot_response.return_value = "Test response"
        response = self.app.post('/copilot', json={'user_input': 'Test input'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['response'], 'Test response')
        mock_get_copilot_response.assert_called_once_with('Test input')

    @patch('src.chatbot.app.openai.Completion.create')
    def test_get_copilot_response(self, mock_create):
        mock_create.return_value.choices = [MagicMock(text='Test response')]
        response = get_copilot_response('Test input')
        self.assertEqual(response, 'Test response')
        mock_create.assert_called_once_with(
            engine="text-davinci-003",
            prompt='Test input',
            max_tokens=150
        )

if __name__ == '__main__':
    unittest.main()
