#!/bin/bash
echo "Running test suite with coverage report at the end"
echo -e "( would require coverage python package to be installed )\n"

# comma separated list of directories to omit from report
OMIT="djsouth/tests/*,djsouth/tests.py"
# comma separeted list of packages to monitor when coverage is run
SOURCE="djsouth"

coverage run --source "$SOURCE" setup.py test
coverage report -m --omit "$OMIT"
