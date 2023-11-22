#!/bin/sh

# for workflows in .github/workflows ; do
# # if [[ "$worklows" != "_*" && "$worklows" != "README" ]]; then
# echo "$worklows"
# # fi
# done

# for actionsubdir in actions/ ; do
# echo $actionsubdir
# done

for d in */ ; do
    echo "$d"
done
