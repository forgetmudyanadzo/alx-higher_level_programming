#!/bin/bash
# Bash script that take a URL, send a GET request & display only body of 200 status code response
curl -sL "$1"
