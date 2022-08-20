#!/usr/bin/python3
"""Send request to URL and print value of x-Request-Id from response header"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('x-Request-Id'))
