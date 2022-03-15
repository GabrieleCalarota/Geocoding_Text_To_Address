from typing import Dict

from GoogleMaps.GoogleMapsClient import GoogleMapsClient


class GoogleMapsGeocodeClient(GoogleMapsClient):

    def __init__(self):
        super().__init__()

    def geocode(self, address: str) -> Dict:
        """Careful! This function is a paid API service"""
        return self.client.geocode(address)
