#!/usr/bin/python3
"""Send POST request with email as a parameter and display
response body in utf-8"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    payload = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(url, payload)

    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf8')
        print(content)
