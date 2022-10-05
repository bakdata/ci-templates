# bump-version

This action will bump the version of your project according to the `.bumpversion.cfg` file.

## Prerequisites

You need a `.bumpversion.cfg` file in the root directory of your repository. A minimal configuration could look like this:

```cfg
[bumpversion]
current_version = 0.0.1
commit = False
tag = False
```

> **Note**
> Changes made to the `.bumpversion.cfg` file by this action are **not** pushed back to GitHub. If you need this functionality, please use the [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push) action subsequently.

## Input Parameters

| Name              | Required |     Default Value     | Description                                           |
| ----------------- | :------: | :-------------------: | ----------------------------------------------------- |
| release-type      |    ✅     |           -           | The scope of the release (major, minor or patch)      |
| working-directory |    ❌     | `.` (repository root) | The directory containing the `.bumpversion.cfg` file. |

### Outputs

This action outputs the following variables:

| Name        | Description                                           |
| ----------- | ----------------------------------------------------- |
| old-tag     | Defines the old version in your .bumpversion.cfg file |
| release-tag | The bumped version of your project                    |

## Usage

Add the following steps to your workflow:

```yaml
...
steps:
  # check out current repository
  - uses: actions/checkout@v3

  # bump the version of your project
  - name: Bump version
    uses: bakdata/ci-templates/actions/bump-version@main
    with:
    release-type: "patch"
...
```
