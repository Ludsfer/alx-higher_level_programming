#!/usr/bin/python3
"""api thing"""

if __name__ == "__main__":
    import sys
    import requests
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    result = requests.get(url)
    try:
        d = result.json()
        for i in range(10):
            print("{}: {}".format(d[i]["sha"],
                                  d[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
