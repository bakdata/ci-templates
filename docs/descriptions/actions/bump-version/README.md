# Description bump-version composite action

This action will bump the version of your project according to the `.bumpversion.cfg` file.

## Prerequisites

You need a `.bumpversion.cfg` file in `working-directory` (repository root by default). A minimal configuration could look like this:

```cfg
[bumpversion]
current_version = 0.0.1
```

> **Note**
> Changes made to the `.bumpversion.cfg` file by this action are **not** pushed back to GitHub. If you need this functionality, please use the [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push) action subsequently.

## Usage

Add the following steps to your workflow:

```yaml
steps:
  # check out current repository
  - uses: bakdata/ci-templates/actions/checkout@1.32.0

  # bump the version of your project
  - name: Bump version
    uses: bakdata/ci-templates/actions/bump-version@main
    with:
    release-type: "patch"
    working-directory: "."
    new-version: "2.0.0"
```
