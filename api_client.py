import requests

def get_access_token(username, password):
    """
    Get OAuth2 access token
    credentials should be like this: {'username':'USR', 'password': 'PWD'}
    :param credentials:
    :return:
    """
    credentials = {'username': username, 'password': password}
    response = requests.post('https://api.europace.de/login', data=credentials)
    return response.json()['access_token']

def get_angebote(vorgangs_nummer, access_token):
    headers = {'Authorization': 'Bearer ' + access_token,
               'content-type': 'application/json', 'cache-control': 'no-cache'}
    url = 'https://baufismart.api.europace.de/v2/ergebnisliste/ermittlung?vorgangsNummer=' + vorgangs_nummer
    response = requests.post(url, headers=headers)
    return response
