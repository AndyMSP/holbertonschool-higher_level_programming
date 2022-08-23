#!/usr/bin/python3
"""Use GitHub API to print user id"""


if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    pat = sys.argv[2]

    url = "http://api.github.com/user"
    payload = {'authorization': pat}
    print(payload)

    r = requests.get(url, params=payload)
    print(r.headers['X-RateLimit-Limit'])
    print(r.headers['x-ratelimit-remaining'])
