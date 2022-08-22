#!/usr/bin/python3
"""Send POST request and format and display response"""


if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    r = requests.post(url, payload)

    try:
        data = r.json()
        if data == {}:
            print("No result")
        else:
            print("[i{}] {}".format(data.get('id'), data.get('name')))
    except Exception:
        print('Not a valid JSON')
