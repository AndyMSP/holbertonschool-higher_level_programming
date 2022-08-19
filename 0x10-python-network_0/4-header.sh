#!/bin/bash
# Sends a GET request with an extra header attribute
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
