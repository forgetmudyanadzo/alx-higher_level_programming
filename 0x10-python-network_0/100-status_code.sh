#!/bin/bash
# Script that send request to URL as an argument, & displays only the status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
