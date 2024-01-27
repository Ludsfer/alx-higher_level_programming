#!/bin/bash
# A script takes, sends a POST request to the URL. variable `email` value `test@gmail.com`. Use `curl`
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
