#!/bin/bash
# Forming request to 0.0.0.0:5000/catch_me which returns message "You got me!".
curl -sL -X PUT -H "Origin: ALXSWE" -d "user_id=98" 0.0.0.0:5000/catch_me
