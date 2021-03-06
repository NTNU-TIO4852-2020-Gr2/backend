#!/bin/bash

LOCAL_DIR=".local/docker"
CONFIG_FILE="src/settings/local.docker.py"
DB_FILE="$LOCAL_DIR/db.sqlite3"
DC_FILE="setup/docker-compose.dev.yml"
DC="docker-compose -f $DC_FILE"

set -eu

# Check if config file exists
if [[ ! -f $CONFIG_FILE ]]; then
    echo "App config not found: $SETTINGS_FILE" 1>&2
    exit -1
fi

# Check if DB file exists
if [[ ! -f $DB_FILE ]]; then
    echo "DB file not found: $DB_FILE" 1>&2
    exit -1
fi

# Check if no command was specified
if [[ -z $@ ]]; then
    echo "No command was specified." 1>&2
    exit -1
fi

$DC run app $@
