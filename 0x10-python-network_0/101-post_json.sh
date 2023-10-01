#!/bin/bash
# A script that sends a JSON POST request to URL, & displays the body of response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
