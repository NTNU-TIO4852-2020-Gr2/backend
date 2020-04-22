#!/bin/bash

DC_FILE="setup/docker-compose.dev.yml"
DC="docker-compose -f $DC_FILE"
DB_SUPER_USER="postgres"
DB_USER="eit"
DB_NAME="eit"
DB_PASS="eit"

set -eu

$DC start db

container_id="$($DC ps -q db)"

docker exec -i $container_id psql --username=$DB_SUPER_USER > /dev/null << END
DROP DATABASE IF EXISTS $DB_NAME;
DROP USER IF EXISTS $DB_USER;
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
ALTER ROLE $DB_USER SET client_encoding TO 'utf8';
ALTER ROLE $DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $DB_USER SET timezone TO 'Europe/Oslo';
GRANT ALL PRIVILEGES ON DATABASE $DB_USER TO $DB_NAME;
END

$DC stop db
