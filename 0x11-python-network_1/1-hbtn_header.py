#!/usr/bin/python3
"""
Python script takes input URL, sends request to the URL
and provide the value of the X-Request-Id variable
located in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
