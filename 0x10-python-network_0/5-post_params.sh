#!/bin/bash
# Scripts take input URL then sends POST request to it and show body of response.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
