import unittest
from unittest.mock import patch, AsyncMock
from src.ai.ai_module import AI_Agent

class TestAIAgent(unittest.TestCase):

    def setUp(self):
        self.config = {
            'ai': {
                'epsilon': 0.1,
                'gamma': 0.9,
                'max_concurrent_tasks': 5,
                'alert_threshold': 0.7
            },
            'exploit': {
                'default_exploit': 'default_exploit'
            }
        }
        self.agent = AI_Agent(self.config)

    @patch('src.ai.ai_module.aiohttp.ClientSession.get', new_callable=AsyncMock)
    def test_monitor_network_traffic(self, mock_get):
        mock_get.return_value.__aenter__.return_value.text = AsyncMock(return_value='test_data')
        url = 'http://test.com'
        result = asyncio.run(self.agent.monitor_network_traffic(mock_get, url))
        self.assertEqual(result, 'test_data')

    @patch('src.ai.ai_module.aiohttp.ClientSession.get', new_callable=AsyncMock)
    def test_process_network_traffic(self, mock_get):
        mock_get.return_value.__aenter__.return_value.text = AsyncMock(return_value='test_data')
        urls = ['http://test1.com', 'http://test2.com']
        asyncio.run(self.agent.process_network_traffic(urls))
        self.assertEqual(mock_get.call_count, 2)

    def test_adjust_alert_threshold(self):
        self.agent.adjust_alert_threshold(0.8)
        self.assertEqual(self.agent.alert_threshold, 0.77)
        self.agent.adjust_alert_threshold(0.6)
        self.assertEqual(self.agent.alert_threshold, 0.693)

if __name__ == '__main__':
    unittest.main()
