#!/bin/bash
# display only the status code of a response
curl -o /dev/null -w "%{http_code}" "$1"
