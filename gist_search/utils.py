import requests
from pprint import pprint

BASE_URL = 'https://api.github.com/users/{username}/gists'


def get_gists(username):
    url = BASE_URL.format(username=username)
    resp = requests.get(url, params={'per_page': 100})
    if not resp.ok:
        return None
    return resp.json()

gists = get_gists('santiagobasulto')
first_gist = gists[0]
first_three = gists[:3]

for gist in first_three:
    print("{:<40} | {}".format(gist['id'], gist['description']))
#pprint(first_gist)
