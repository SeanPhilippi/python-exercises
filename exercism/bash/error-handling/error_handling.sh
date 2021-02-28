#!/usr/bin/env bash

if [ $# -eq 0 ] || [ $# -eq 2 ]; then
    echo "Usage: error_handling.sh <person>"
    exit 1
else
    echo "Hello, $1"
fi
