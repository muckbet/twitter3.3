from docs import twitter_api, coordinates, map


def main(name):
    """
    (None) -> None

    Call all functions
    Create a map with the locations of the friends of the user that you enter
    """
    user_dict = twitter_api.main(name)
    if user_dict == "":
        return "no_name"
    user_points_dict = coordinates.convert_to_coordinates(user_dict)
    map.create_map(user_points_dict, name)
