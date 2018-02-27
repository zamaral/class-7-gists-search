import json


with open('sample.json') as fp:
    SAMPLE_GISTS = json.loads(fp.read())
