import argparse
from typing import Dict, List

from GoogleMaps.GoogleMapsGeocodeClient import GoogleMapsGeocodeClient


def convert_street_address(address: str) -> str:
    # Instantiating google maps class and making the call
    gmgc = GoogleMapsGeocodeClient()
    result = gmgc.geocode(address=address)

    if isinstance(result, list):
        # getting only one result filtered by street address types
        new_result = list(filter(lambda x: 'street_address' in x.get('types'), result))
        result = new_result[0]

    if not result or 'address_components' not in result or not result.get('address_components'):
        # Raising error if google maps didn't recognize as a valid address
        raise ValueError(f"{address=} is not recognized by google maps")

    address_components: List[Dict] = result.get('address_components')
    list_of_result = [None, None, None, None]
    headers = ['route', 'postal_code', 'locality', 'country']

    # for every object getting only the types in headers variable and putting the long_name value in order in the
    # list_of_result list variable
    for object_element in address_components:
        for num, header in enumerate(headers):
            if header in object_element.get('types'):
                list_of_result[num] = object_element.get('long_name')
                continue

    return ','.join(list_of_result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Luxoft Interview", description='Query external API to translate free text '
                                                                          'formatted address to structured address',
                                     epilog="Output is in format: <Street>,<Zip-code>,<City>,<Country>")
    parser.add_argument('-t', metavar='address', default='5 Av. Anatole, Paris, Champ de Mars',
                        type=ascii,
                        nargs='?',
                        help='Provides input of free text formatted address')
    args = parser.parse_args()
    print(convert_street_address(address=args.t))
