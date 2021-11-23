#!/bin/bash

# set default to patch and convert to lowercase
releaseType=$(echo "${1:-patch}" | awk "{print tolower($0)}")

if [[ "${releaseType}" == "major" || "${releaseType}" == "minor" || "${releaseType}" == "patch" ]]; then
    echo "Bumping version with release type ${releaseType}"
    bump2version ${releaseType}
else
    echo "ERROR: Only major, minor or patch is allowed for input releaseType."
    exit 1
fi
