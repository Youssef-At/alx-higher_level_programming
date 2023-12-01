#!/bin/bash
# script to get the allowed methods in an server if availaible through OPTIONS http request
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
