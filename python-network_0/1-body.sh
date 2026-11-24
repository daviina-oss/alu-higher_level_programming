#!/bin/bash
# Follows redirects and displays the body of the response only if the final status is 200
t=$(mktemp); [ "$(curl -sL -o "$t" -w '%{http_code}' "$1")" = "200" ] && cat "$t"; rm -f "$t"
