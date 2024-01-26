#!/bin/bash
# Bash script sends DELETE request to URL passed as the first argument, displays response body. Use curl
curl -sX DELETE "$1"
