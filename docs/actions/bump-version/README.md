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
  - uses: bakdata/ci-templates/actions/checkout@main

  # bump the version of your project
  - name: Bump version
    uses: bakdata/ci-templates/actions/bump-version@main
    with:
    release-type: "patch"
    working-directory: "."
    new-version: "2.0.0"
```

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT             | TYPE   | REQUIRED | DEFAULT  | DESCRIPTION                                           |
| ----------------- | ------ | -------- | -------- | ----------------------------------------------------- |
| allow-dirty       | string | false    | `"true"` | Allow unclean Git status in the working directory.    |
| new-version       | string | false    |          |                                                       |
| release-type      | string | true     |          | The type of the release (major, minor or patch).      |
| working-directory | string | false    | `"."`    | The directory containing the `.bumpversion.cfg` file. |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

| OUTPUT          | TYPE   | DESCRIPTION                                      |
| --------------- | ------ | ------------------------------------------------ |
| old-version     | string | The old version in your `.bumpversion.cfg` file. |
| release-version | string | The bumped version of your project.              |

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets
