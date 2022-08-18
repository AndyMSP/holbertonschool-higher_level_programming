#!/bin/bash
# Prints body size of http response to URL GET request
curl -sI "$1" | awk '/Content-Length/ {print $2}'