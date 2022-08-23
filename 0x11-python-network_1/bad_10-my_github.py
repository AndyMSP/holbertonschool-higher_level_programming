#!/usr/bin/python3
"""Use GitHub API to print user id"""


if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    token = sys.argv[2]

    url = "http://api.github.com/users/andyMSP"
    payload = {'Authorization': 'token ' + token}

    r = requests.get(url, params=payload)
    data = r.json()
    print(data['id'])
