#!/bin/bash
#Prints body size of http response to URL GET request
curl -s "$1" | wc -c
