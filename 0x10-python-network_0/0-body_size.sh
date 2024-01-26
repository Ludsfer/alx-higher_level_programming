#!/bin/bash
# A bash script that takes and sends a request a URL, display body in byte. use `curl`
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2
