function check_var_exists {
    if [ -z $1 ]; then
        echo >&2 "ERROR: $2"
        exit 1
    fi
}
