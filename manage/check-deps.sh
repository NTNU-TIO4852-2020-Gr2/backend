#!/bin/bash

export CUSTOM_COMPILE_COMMAND="manage/upgrade-deps.sh"

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
cp requirements.txt requirements.old.txt

echo "Temporarily upgrading requirements files ..."
pip-compile --quiet --upgrade --output-file requirements.tmp.txt requirements.in

echo "Dependency updates:"
diff requirements.old.txt requirements.tmp.txt || true

rm -f requirements.old.txt
rm -f requirements.tmp.txt
