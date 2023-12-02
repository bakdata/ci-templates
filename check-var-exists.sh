function check_var_exists {
    if [ -z $1 ]; then
        >&2 echo "ERROR: $2"
        exit 1
    fi
}
