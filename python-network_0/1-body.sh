#!/bin/bash
# Sends a GET request to the URL and displays the body, only for a 200 status
tmp=$(mktemp)
status=$(curl -s -o "$tmp" -w "%{http_code}" "$1")
if [ "$status" = "200" ]; then
    cat "$tmp"
fi
rm -f "$tmp"
