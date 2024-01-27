#!/usr/bin/python3
"""Python script that takes GitHub credentials
(username and password), uses GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    user = str(sys.argv[1])
    pw = str(sys.argv[2])
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(user, pw)))

    try:
        data = result.json()
        print(data["id"])
    except:
        pass
