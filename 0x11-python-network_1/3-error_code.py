#!/usr/bin/python3
"""Request content from URL and handle and display errors"""


from urllib.error import HTTPError


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf8')
            print(content)
    except HTTPError as error:
        print("Error code: {}".format(error.code))
