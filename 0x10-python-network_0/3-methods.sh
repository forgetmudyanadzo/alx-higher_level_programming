#!/bin/bash
# display all URL and shows the Allowed OPTIONS
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
