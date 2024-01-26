#!/bin/bash
# A bash script that takes a URL, displays all HTTP methods the server will accept. Use `curl`
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
