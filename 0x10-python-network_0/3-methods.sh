#!/bin/bash
# A Bash script that shows all allowed methods to the server.
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d ' ' -f 2-
