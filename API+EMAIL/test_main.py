import unittest
from unittest.mock import patch, MagicMock
from main import *

class TestAPIEmail(unittest.TestCase):
    def setUp(self):
        self.valid_email = 'test@example.com'
        self.invalid_email = 'invalid_email'
        
    def test_valid_email(self):
        self.assertTrue(validate_email(self.valid_email))
        
    def test_invalid_email(self):
        self.assertFalse(validate_email(self.invalid_email))
        
    def test_get_weather_data(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'weather': [{'description': 'sunny'}], 'main': {'temp': 22.5}}
            
            data = get_weather_data('London')
            
            self.assertTrue(data['description'] == 'sunny')
            self.assertTrue(data['temperature'] == 22.5)
            
    def test_get_exchange_rate_data(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = {'rates': {'GBP': 0.88}}
            
            data = get_exchange_rate_data('USD', 'GBP')
            
            self.assertTrue(data['rate'] == 0.88)
            self.assertTrue(data['source'] == 'USD')
            self.assertTrue(data['destination'] == 'GBP')
            
    def test_invalid_api(self):
        with self.assertRaises(ValueError):
            main(['test@example.com', 'invalid_api'])
            
    def test_valid_api_weather(self):
        with patch('main.get_weather_data') as mock_get_weather, patch('main.send_email') as mock_send_email:
            mock_get_weather.return_value = {'description': 'sunny', 'temperature': 22.5}
            main(['test@example.com', 'weather'])
            
            mock_get_weather.assert_called_once_with('London')
            mock_send_email.assert_called_once_with('test@example.com', 'Weather Update', 'The weather in London is sunny and the temperature is 22.5C.')
            
    def test_valid_api_exchange_rate(self):
        with patch('main.get_exchange_rate_data') as mock_get_exchange, patch('main.send_email') as mock_send_email:
            mock_get_exchange.return_value = {'rate': 0.88, 'source': 'USD', 'destination': 'GBP'}
            main(['test@example.com', 'exchange'])
            
            mock_get_exchange.assert_called_once_with('USD', 'GBP')
            mock_send_email.assert_called_once_with('test@example.com', 'Exchange Rate Update', 'The exchange rate from USD to GBP is 0.88.')
        
if __name__ == '__main__':
    unittest.main()
