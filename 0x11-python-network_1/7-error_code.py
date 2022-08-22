#!/usr/bin/python3
"""Sends request and prints response or any error message > 400"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    r = requests.get(url)

    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
