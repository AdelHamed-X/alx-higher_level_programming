#!/bin/bash
# A script that shows the byte count of HTTP Respnse
curl -s $1 | wc -c
