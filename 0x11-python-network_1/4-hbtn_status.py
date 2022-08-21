#!/usr/bin/python3
"""Use request package to fetch web resource"""

if __name__ == "__main__":
    import requests

    r = requests.get('http://intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
