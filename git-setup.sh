#!/bin/bash

source $(dirname "${BASH_SOURCE[0]}")/check-var-exists.sh

check_var_exists "$1" "Github username cannot be empty!"
check_var_exists "$2" "Github email cannot be empty!"

git config user.name "$1"
git config user.email "$2"
