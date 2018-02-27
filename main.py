import click

from gist_search.search import search_gists


@click.command()
@click.option('-u', '--user', required=True)
@click.option('-d', '--description', required=False)
@click.option('-f', '--file-name', required=False)
def main(user, description, file_name):
    gists = search_gists(user, description=description, file_name=file_name)

    if not gists:
        return
    if len(gists) == 0:
        print("No results...")
        return

    print("Results ({}):".format(len(gists)))
    for gist in gists:
        print("\tID: {}".format(gist['id']))
        print("\tURL: {}".format(gist['html_url']))
        print("\tDescription: {}".format(gist['description']))
        files = gist['files']
        files_concat = ' | '.join(files.keys())
        print('\tFiles: {} - ({})'.format(len(files), files_concat))
        print('-' * 60)


if __name__ == '__main__':
    main()
