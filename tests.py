import responses
from gist_search.utils import get_gists
from gist_search.search import search_gists
import test_data


USER_GIST_URL = 'https://api.github.com/users/santiagobasulto/gists'
USER_NOT_FOUND_GIST_URL = 'https://api.github.com/users/xyznotexists/gists'


@responses.activate
def test_search_gists_description():
    responses.add(responses.GET, USER_GIST_URL, json=test_data.SAMPLE_GISTS)
    gists = search_gists('santiagobasulto', description='timedelta')
    assert len(gists) == 1

    gist = gists[0]

    assert gist['id'] == '698f0ff660968200f873a2f9d1c4113c'
    description = ('A simple script to parse human readable '
                   'time deltas into Python datetime.timedeltas')
    assert gist['description'] == description


@responses.activate
def test_search_gists_filename():
    responses.add(responses.GET, USER_GIST_URL, json=test_data.SAMPLE_GISTS)
    gists = search_gists('santiagobasulto', file_name='timezone')
    assert len(gists) == 1

    gist = gists[0]

    assert gist['id'] == 'b9ac9697d4741fa7e477fece23f2d7a3'
    description = 'Generate time options for different timezones'
    assert gist['description'] == description

    files = gist['files']
    assert len(files) == 1
    assert 'timezone_options.py' in files


@responses.activate
def test_search_gists_description_and_filename():
    responses.add(responses.GET, USER_GIST_URL, json=test_data.SAMPLE_GISTS)
    gists = search_gists(
        'santiagobasulto', file_name='time', description='timezones')
    assert len(gists) == 1

    gist = gists[0]

    assert gist['id'] == 'b9ac9697d4741fa7e477fece23f2d7a3'
    description = 'Generate time options for different timezones'
    assert gist['description'] == description

    files = gist['files']
    assert len(files) == 1
    assert 'timezone_options.py' in files


# Internal Tests. Already implemented:


@responses.activate
def test_get_gists():
    responses.add(responses.GET, USER_GIST_URL, json=test_data.SAMPLE_GISTS)
    gists = get_gists('santiagobasulto')
    assert len(gists) == 2


@responses.activate
def test_get_gists_user_not_found():
    responses.add(responses.GET, USER_NOT_FOUND_GIST_URL, status=404)
    gists = get_gists('xyznotexists')
    assert gists is None
