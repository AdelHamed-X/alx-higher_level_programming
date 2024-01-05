#!/bin/bash
# A script that shows the byte count of HTTP Respnse
curl -sI $1 | grep Content-Length | cut -d ' ' -f 2