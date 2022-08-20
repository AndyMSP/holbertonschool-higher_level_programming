#!/usr/bin/python3
# fetches https://intranet.hbtn.io/status and formats body contents

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf8')}")
