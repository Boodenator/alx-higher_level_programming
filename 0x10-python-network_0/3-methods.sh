#!/bin/bash
# Showing SERVER accepted HTTP methods of URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
