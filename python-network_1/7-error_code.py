#!/usr/bin/python3
"""Displays the body of the response, or the error code if it is 400+."""
import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
