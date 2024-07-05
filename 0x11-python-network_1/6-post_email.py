#!/usr/bin/python3
"""
Python Script with input URL and an email address, sends a POST request to the
passed URL with the email as a parameter, the view the body
of the response.
Usage: ./6-post_email.py <URL> <email>
  - viewing the response body.
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)

    print(req.text)
