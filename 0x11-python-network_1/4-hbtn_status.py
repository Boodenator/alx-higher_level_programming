#!/usr/bin/python3
"""Pythin Script fetches https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
