# CI-templates

This is a collection of reusable workflows and composite actions for GitHub that bakdata uses for open-source projects.

## Using reusable workflows

You can use reusable workflows in this repository like this:

```yaml
---
jobs:
  call-workflow-passing-data:
    uses: bakdata/ci-templates/.github/workflows/my-workflow.yaml@main
    with:
      foo: bar
```

## Using composite actions

You can use composite actions in this repository like this:

```yaml
---
steps:
  - uses: bakdata/ci-templates/actions/my-action@main
    with:
      foo: bar
```

## Development setup

Install the dependencies using [mise-en-place](https://mise.jdx.dev/).

```sh
mise install
```

It will also install git commit hooks which are used to automatically create the documentation.
