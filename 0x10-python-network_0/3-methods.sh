#!/bin/bash
# Show requests options allowed by url
curl -isX OPTIONS "$1" | grep 'Allow' | sed 's/Allow: //'
