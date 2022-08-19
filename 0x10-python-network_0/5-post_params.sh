#!/bin/bash
# make POST request with parameters in body
curl -s -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
