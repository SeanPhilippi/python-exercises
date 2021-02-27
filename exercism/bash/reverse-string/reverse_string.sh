#!/usr/bin/env bash
set -o noglob

WORD=$1
echo "$WORD" | rev 
