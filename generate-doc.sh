#!/bin/bash

# actions

for actionsubdir in actions/*; do
    actionname="$(echo $actionsubdir | cut -d'/' -f2)"
    actionfilename="$actionsubdir/action.y*"
    mkdir -p "docs/references/actions/$actionname"
    outputdocfile="docs/references/actions/$actionname/Variables.md"
    echo "# Refenrences $actionname composite action" >$outputdocfile
    echo "## Inputs" >>$outputdocfile
    echo "## Outputs" >>$outputdocfile

    auto-doc -f $actionfilename --colMaxWidth 10000 --colMaxWords 2000 -o $outputdocfile
done

# workflows

for workflows in .github/workflows/* ; do
    currentworkflow="$(echo $workflows | cut -d'/' -f3)"
if [[ $currentworkflow != _* && $currentworkflow != "README.md" ]]; then
    workflowname="$(echo $currentworkflow | cut -d'.' -f1)"
    mkdir -p "docs/references/wokflows/$workflowname"
    workflowoutputdoc="docs/references/wokflows/$workflowname/Variables.md"

    echo "# Refenrences $workflowname reusable Workflow" > $workflowoutputdoc
    echo  "## Inputs" >> $workflowoutputdoc
    echo  "## Outputs" >> $workflowoutputdoc
    echo  "## Secrets" >> $workflowoutputdoc

    auto-doc -f $workflows --colMaxWidth 10000 --colMaxWords 2000 -o $workflowoutputdoc -r
fi
done
