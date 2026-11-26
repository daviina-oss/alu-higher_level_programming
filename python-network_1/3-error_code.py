#!/usr/bin/python3
"""Displays the body of the response, or the error code if there is one."""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
