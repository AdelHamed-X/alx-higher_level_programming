#!/bin/bash
# A Bash script that shows all allowed methods to the server.
curl -siX OPTIONS "$1"
