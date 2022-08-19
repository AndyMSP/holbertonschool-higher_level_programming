#!/bin/bash
# Show requests options allowed by url
curl -isX OPTIONS "$1" | grep allow | sed 's/Allow: //'