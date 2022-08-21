#!/usr/bin/python3
"""Use request package to fetch web resource"""

import requests

if __name__ == '__main__':

    try:
        r = requests.get('http://0.0.0.0:5050/status')
    except Exception:
        r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
