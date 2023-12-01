#!/bin/bash
#scripts that sends a POST request to a given URL.
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
