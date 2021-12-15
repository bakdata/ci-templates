#!/bin/bash

source $(dirname $(dirname "${BASH_SOURCE[0]}"))/check-var-exists.sh

check_var_exists "$1" "Release type cannot be empty!"

# set default to patch and convert to lowercase
releaseType=$(echo "${1:-patch}" | awk '{print tolower($0)}')

if [[ "${releaseType}" == "major" || "${releaseType}" == "minor" || "${releaseType}" == "patch" ]]; then
    echo "Bumping version with release type ${releaseType}"
    bump2version ${releaseType}
else
    >&2 echo "ERROR: Only major, minor or patch is allowed as release type."
    exit 1
fi
