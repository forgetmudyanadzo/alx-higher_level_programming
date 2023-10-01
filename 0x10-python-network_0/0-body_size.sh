#!/bin/bash
# send request to URL with curl,& display size of the body of response
curl -s "$1" | wc -c
