# ci-templates
This is a collection of Github actions that Bakdata uses for open source projects.


## Checkout repository
These actions only work if you check them out into the `ci-templates` folder in the root directory. To checkout the repository in a workflow you can use these steps:

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
