import folium


def add_markers(dictionary):
    """
    (dict) -> <class 'folium.map.FeatureGroup'>

    Returns loactions to add it to the map
    """
    friends = folium.FeatureGroup("Friends Locations")
    for name in dictionary:
        points = dictionary[name][0]
        if friends:
            icon = folium.features.CustomIcon(dictionary[name][1],
                                              icon_size=(35, 35))
            friends.add_child(folium.Marker(location=[points[0],
                                                      points[1]],
                                            popup=name,
                                            icon=icon))
    return friends


def create_map(dictionary, name):
    """
    (None) -> None

    Creates a map with folium in HTML file

    """
    map = folium.Map()
    # ADD MARKERS
    friends = add_markers(dictionary)
    map.add_child(friends)
    map.add_child(folium.LayerControl())
    map.save("./templates/" + name + "_map.html")
