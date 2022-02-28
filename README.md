# ci-templates
This is a collection of reusable workflows and composite actions for Github that Bakdata uses for open source projects.


## Using reusable workflows
You can use reusable workflows in this repository like this:

```yaml
...
jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/my-workflow.yaml@main
    with:
      var1: foo
...
```

## Using composite actions
The composite actions only work if you check them out into the `ci-templates` folder in the root directory. To checkout the repository in a workflow you can use these steps:

```yaml
...
steps:
  # check out current repository
  - uses: actions/checkout@v2

  # check out ci-templates into ./ci-templates
  - uses: actions/checkout@v2
    with:
      repository: "bakdata/ci-templates"
      path: "ci-templates"
```
