# Description of release-tag-versions reusable Workflow

This workflow enables the release of tag versions as well as the creation of a new snapshot version for developers to work on the next release. The workflow allows you to choose the sort of release that will be performed as well as how to generate the snapshot version.

## Prerequisites

Create, and configure your `.bumpversion.cfg` file and make sure it's in the `version-configs-dir` directory. A minimal configuration with `Chart.yaml` being the versioning file could look like this:

```cfg
[bumpversion]
current_version = 1.0.1-SNAPSHOT
parse = (?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(-(?P<suffix>\w+))?
serialize =
  {major}.{minor}.{patch}-{suffix}
  {major}.{minor}.{patch}

[bumpversion:file:path/to/Chart.yaml]
search =
  version: {current_version}
  appVersion: {current_version}
replace =
  version: {new_version}
  appVersion: {new_version}
```

## Dependencies

- [bakdata/ci-templates/actions/checkout@1.32.0](https://github.com/bakdata/ci-templates/blob/1.32.0/actions/checkout)
- [bakdata/ci-templates/actions/java-gradle-setup@v1.16.0](https://github.com/bakdata/ci-templates/blob/v1.16.0/actions/java-gradle-setup)

## References

### Inputs

<!-- AUTO-DOC-INPUT:START - Do not remove or modify this section -->

| INPUT                   | TYPE   | REQUIRED | DEFAULT      | DESCRIPTION                                                                                                |
| ----------------------- | ------ | -------- | ------------ | ---------------------------------------------------------------------------------------------------------- |
| next-dev-release-suffix | string | false    | `"SNAPSHOT"` | The suffix to add for the developer version                                                                |
| next-dev-release-type   | string | true     |              | Scope of the next release (minor or patch) for developers                                                  |
| release-type            | string | true     |              | Scope of the release (major, minor or patch).                                                              |
| version-configs-dir     | string | true     |              | The Path to the directory containing the file where the versioning is defined and `.bumpversion.cfg` file. |

<!-- AUTO-DOC-INPUT:END -->

### Outputs

<!-- AUTO-DOC-OUTPUT:START - Do not remove or modify this section -->

No outputs.

<!-- AUTO-DOC-OUTPUT:END -->

### Secrets

<!-- AUTO-DOC-SECRETS:START - Do not remove or modify this section -->

| SECRET          | REQUIRED | DESCRIPTION                                     |
| --------------- | -------- | ----------------------------------------------- |
| github-email    | true     | The GitHub email for committing the changes.    |
| github-token    | true     | The GitHub token for committing the changes.    |
| github-username | true     | The GitHub username for committing the changes. |

<!-- AUTO-DOC-SECRETS:END -->
