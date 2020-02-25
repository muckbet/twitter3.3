import urllib.request, urllib.parse, urllib.error
from docs import twurl
import json
import ssl


def ignore_ssl_er():
    """
    (None) -> <class 'ssl.SSLContext'>

    Return a new SSLContext object with some settings.
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def create_get_request(account):
    """
    (str) -> str

    Return created GET request
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    # get url
    url = twurl.augment(TWITTER_URL, {'screen_name': account, 'count': '150'})
    return url


def get_url_data(url, ctx):
    """
    () -> <class 'http.client.HTTPResponse'>, str

    Return client HTTP response and information about friends
    """
    # connection = client HTTP response
    connection = urllib.request.urlopen(url, context=ctx)
    # data is equal all the info in str
    data = connection.read().decode()
    return connection, data


def data_to_json_file(path, data):
    """
    (str, str) -> None

    Data to json file
    """
    f = open(path, "w")
    print(data, file=f)
    f.close()


def from_json_file_info(path):
    """
    (str) -> dict

    """
    f = open(path, encoding='utf-8')
    info = json.load(f)
    f.close()
    return info


def get_user_location_pics(json_dict):
    """
    (dict) -> dict

    Return names with their location names and pics url
    """
    user_dict = {}
    for user in json_dict['users']:
        user_dict[user['screen_name']] = [user['location'],
                                          user['profile_image_url']]
    return user_dict


def main(name):
    """
    (None) -> dict

    Call all the functions
    Return names with their location names and pics
    """
    ctx = ignore_ssl_er()
    twitter_account = name
    if not twitter_account:
        return False
    try:
        url = create_get_request(twitter_account)
        connection, data = get_url_data(url, ctx)
    except:
        return False
    path = "friends.json"
    data_to_json_file(path, data)
    json_dict = from_json_file_info(path)
    user_dict = get_user_location_pics(json_dict)
    return user_dict
