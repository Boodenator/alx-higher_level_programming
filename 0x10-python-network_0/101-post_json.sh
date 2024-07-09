#!/bin/bash
# Sendng a JSON POST request to URL with certain JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
