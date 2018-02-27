# Class 7: Gist Search

This project provides basic search functionality for a user's public gists.

### Usage

```bash
$ python main.py -u <username> -d [description] -f [file-name]
```

* **`username`** (required): owner of the gists to search for
* **`description`** (optional): Description of gists must contain the passed parameter
* **`file-name`** (optional): The gist contains a file with the given parameter.

**Example**

```bash
# searches all the gists which contain the word "time" in the description
$ python main.py -u <santiagobasulto> -d time

# searches all the gists which have at least 1 file that contains the word "time" in the name
$ python main.py -u <santiagobasulto> -f time
```

