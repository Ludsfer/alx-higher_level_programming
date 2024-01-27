#!/usr/bin/python3
"""Sends a request to URL and displays the response body
"""

if __name__ == '__main__':
    from sys import argv
    import requests

    url = argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print(f'Error code: {res.status_code}')
    else:
        print(res.text)
