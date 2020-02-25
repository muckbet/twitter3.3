from geopy.geocoders import Nominatim


def convert_to_coordinates(dictionary):
    """
    (dict) -> dict

    Connects with API and returns dictionary with coordinates
    dictionary: name - coordinates in tuple

    >>> convert_to_coordinates({'Betrayal': ['New Orleans Louisiana USA',
    'url']})
    {'Betrayal': [(29.9536991119385, -90.077751159668), 'url']}
    """
    geolocator = Nominatim(user_agent='application.py')
    dict_coordinates = {}
    for name in dictionary:
        point = dictionary[name][0]
        try:
            location = geolocator.geocode(point)
            if location != None:
                dict_coordinates[name] = [(location.latitude,
                                           location.longitude),
                                          dictionary[name][1]]
        except:
            continue
    return dict_coordinates
