#!/bin/bash

if [[ $CI != "true" ]]; then
    echo "Error: This isn't a CI environment" 2>&1
    exit -1
fi

set -eu # Exit on error and undefined var is error

MANAGE="python3 src/manage.py"

[[ ! -e log ]] && mkdir -p log

# Add temporary config
cp setup/local.ci.py src/settings/local.py

# Run Django tests
$MANAGE test
