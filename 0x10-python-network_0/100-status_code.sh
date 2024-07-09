#!/bin/bash
# Sending GET request for URL then show the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
