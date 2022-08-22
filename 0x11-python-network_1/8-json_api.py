#!/usr/bin/python3
"""Send POST request and format and display response"""


if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = 'http://tacobell.tech'
    payload = {'q': letter}

    r = requests.post(url, payload)

    try:
        data = r.json()
        if (data.get('id') and data.get('name')):
            id, name = data.get('id'), data.get('name')
            print("[i{}] {}".format(id, name))
        else:
            print("No result")
    except Exception:
        print('Not a valid JSON')