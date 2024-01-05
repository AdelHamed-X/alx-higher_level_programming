#!/bin/bash
# A Bash script that shows all allowed methods to the server.
curl -s -i -X OPTIONS "$1" | grep Allow | cut -d ' ' -f 2
