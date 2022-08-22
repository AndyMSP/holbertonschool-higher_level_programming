#!/usr/bin/python3
"""Send POST request with email as a parameter"""


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    r = requests.post(url, payload)

    print(r.text)
