#!/bin/bash
# extract from URL the byte size of HTTP response header.
curl -s "$1" | wc -c
