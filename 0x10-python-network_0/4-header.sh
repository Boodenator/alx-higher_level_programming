#!/bin/bash
# Script takes input URL as argument then sends GET request to URL alongwith showing body of the response
curl "$1" -sX GET -H "X-School-User-Id: 98"
