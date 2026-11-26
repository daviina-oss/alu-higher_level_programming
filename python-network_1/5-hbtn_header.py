#!/usr/bin/python3
"""Displays the X-Request-Id header of the response from a URL."""
import sys
import requests

if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get("X-Request-Id"))
