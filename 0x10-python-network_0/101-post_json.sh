#!/bin/bash
# A bash script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response. Use `curl`
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
