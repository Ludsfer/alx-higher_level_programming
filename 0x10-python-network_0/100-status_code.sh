#!/bin/bash
# A bash script sends request to a URL passed as an argument, displays only the status code of the response. Use `curl`
curl -s -o /dev/null -w "%{http_code}" "$1"
