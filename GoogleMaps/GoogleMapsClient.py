import os.path

import googlemaps
from dotenv import load_dotenv


class GoogleMapsClient:

    def __init__(self):
        self._load_env()
        self.client = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

    @staticmethod
    def _load_env():
        load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))
