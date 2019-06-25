#from gist_search.utils import get_gists
from utils import get_gists #- Only use this if you're running this file, if running from main you need to use the top import line.


def search_gists(username, description=None, file_name=None, ID = None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return

    gists = get_gists(username)
    
    results = []
    for gist in gists:
        if description and description not in gist['description']:
            continue
        
        if file_name:
            found = False
            for fname in gist['files']:
                if file_name.lower() in fname:
                    found = True
                    break                  
            if not found:
                continue
                
        if ID and ID.lower() not in gist['id']:
            continue
        
        results.append(gist)
       
    return results

gists = search_gists('santiagobasulto', file_name = 'failure')        
#gists = search_gists('santiago', description = 'time')
for gist in gists:
    print("{:<40} | {}".format(gist['id'], gist['description']))