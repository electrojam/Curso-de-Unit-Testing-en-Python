import unittest

from src.api_client import get_location
from unittest.mock import patch

class ApiClientTest(unittest.TestCase):

    @patch('src.api_client.requests.get')   # vamos a sobreescribir la línea método requests.get de api_client.py
    def test_get_location_returns_expected_data(self, mock_get):  # prueba de función get_location
        mock_get.return_value.status_code = 200 #cuando se consulte requests.get retornarrá status code = 200        
        mock_get.return_value.json.return_value = { #cuando ejecute requests.get retornará este json
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI"
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8") # confirmamos que nuestro método se llamó, al menos una vez, que la ip es la correcta
