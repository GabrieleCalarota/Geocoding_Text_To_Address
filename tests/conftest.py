import pytest as pytest

result = [{'address_components': [{'long_name': 'Champ de Mars', 'short_name': 'Champ de Mars',
                                   'types': ['establishment', 'park', 'point_of_interest', 'tourist_attraction']},
                                  {'long_name': '2', 'short_name': '2', 'types': ['street_number']},
                                  {'long_name': 'Allée Adrienne Lecouvreur', 'short_name': 'All. Adrienne Lecouvreur',
                                   'types': ['route']},
                                  {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']},
                                  {'long_name': 'Département de Paris', 'short_name': 'Département de Paris',
                                   'types': ['administrative_area_level_2', 'political']},
                                  {'long_name': 'Île-de-France', 'short_name': 'IDF',
                                   'types': ['administrative_area_level_1', 'political']},
                                  {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']},
                                  {'long_name': '75007', 'short_name': '75007', 'types': ['postal_code']}],
           'formatted_address': 'Champ de Mars, 2 All. Adrienne Lecouvreur, 75007 Paris, France',
           'geometry': {'location': {'lat': 48.8556475, 'lng': 2.2986304}, 'location_type': 'ROOFTOP',
                        'viewport': {'northeast': {'lat': 48.8589402, 'lng': 2.3030755},
                                     'southwest': {'lat': 48.85265709999999, 'lng': 2.2933651}}}, 'partial_match': True,
           'place_id': 'ChIJB0gcnCBw5kcRHoIAPcTEApc',
           'plus_code': {'compound_code': 'V74X+7F Paris, France', 'global_code': '8FW4V74X+7F'},
           'types': ['establishment', 'park', 'point_of_interest', 'tourist_attraction']}, {
              'address_components': [{'long_name': '5', 'short_name': '5', 'types': ['street_number']},
                                     {'long_name': 'Avenue Anatole France', 'short_name': 'Av. Anatole France',
                                      'types': ['route']},
                                     {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']},
                                     {'long_name': 'Département de Paris', 'short_name': 'Département de Paris',
                                      'types': ['administrative_area_level_2', 'political']},
                                     {'long_name': 'Île-de-France', 'short_name': 'IDF',
                                      'types': ['administrative_area_level_1', 'political']},
                                     {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']},
                                     {'long_name': '75007', 'short_name': '75007', 'types': ['postal_code']}],
              'formatted_address': '5 Av. Anatole France, 75007 Paris, France',
              'geometry': {'location': {'lat': 48.8581951, 'lng': 2.2946885}, 'location_type': 'ROOFTOP',
                           'viewport': {'northeast': {'lat': 48.8598027802915, 'lng': 2.297116830291502},
                                        'southwest': {'lat': 48.8571048197085, 'lng': 2.294418869708498}}},
              'partial_match': True, 'place_id': 'ChIJuX7JjuFv5kcRbLER0b_rtC4',
              'plus_code': {'compound_code': 'V75V+7V Paris, France', 'global_code': '8FW4V75V+7V'},
              'types': ['street_address']}]


class MyGoogleMapsGeocodeClient:
    def geocode(self, address):
        return result


@pytest.fixture()
def mock_google_maps():
    import GoogleMaps.GoogleMapsGeocodeClient
    real_class = GoogleMaps.GoogleMapsGeocodeClient.GoogleMapsGeocodeClient
    GoogleMaps.GoogleMapsGeocodeClient.GoogleMapsGeocodeClient = MyGoogleMapsGeocodeClient
    yield
    GoogleMaps.GoogleMapsGeocodeClient.GoogleMapsGeocodeClient = real_class
