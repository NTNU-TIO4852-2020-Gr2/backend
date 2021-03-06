#!/bin/bash

# Note: Make sure you have only the Python 2 version of pip-tools installed.
# If you only have the Python 3 version, the deps will get messed up without errors.

export CUSTOM_COMPILE_COMMAND="manage/update-deps.sh"

set -eu

# Activate venv and deactivate on exit
# Allow undefined vars
set +u
source "$(dirname "$BASH_SOURCE[0]")/activate-venv.sh"
trap deactivate EXIT
set -u

# Install pip-tools (needs to be inside venv to prevent conflict between the Python 2 and 3 versions)
pip install pip-tools

if [[ ! -f requirements/all.txt ]]; then
    touch requirements/all.txt
fi
if [[ ! -f requirements.txt ]]; then
    touch requirements.txt
fi
cp requirements/all.txt requirements/all.old.txt

echo "Updating requirements files ..."
pip-compile --quiet --upgrade requirements/development.in
pip-compile --quiet --upgrade requirements/production.in
pip-compile --quiet --upgrade requirements/testing.in
pip-compile --quiet --upgrade requirements/all.in

# Create requirements.txt for dependency analyzers etc.
echo "#" > requirements.txt
echo "# This file contains all requirements and is meant for dependency analyzers etc." >> requirements.txt
echo "# Do not use this file to install requirements, use one of the \"requirements/*.txt\" files instead." >> requirements.txt
cat requirements/all.txt >> requirements.txt

echo "Dependency changes:"
diff requirements/all.old.txt requirements/all.txt || true
rm -f requirements/all.old.txt