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

This workflow is built from multiple composite actions listed below:

- [bump-version](https://github.com/bakdata/ci-templates/tree/main/actions/bump-version)
- [commit-and-push](https://github.com/bakdata/ci-templates/tree/main/actions/commit-and-push)

## Calling the workflow

```yaml
name: Release multiple Helm Charts
on:
  workflow_dispatch:
    inputs:
      release-type:
        description: "Scope of the release (major, minor or patch)."
        required: true
        type: string
      next-dev-release-type:
        description: "Scope of the next release (minor or patch) for developers"
        required: true
        type: string
jobs:
  call-workflow-passing-data:
    name: Release & Publish Helm chart
    uses: bakdata/ci-templates/.github/workflows/release-tag-versions.yaml@main
    with:
      version-configs-dir: "."
      release-type: "${{ inputs.release-type }}"
      next-dev-release-type: "${{ inputs.next-dev-release-type }}"
      next-dev-release-suffix: "SNAPSHOT"
    secrets:
      github-email: "${{ secrets.GH_EMAIL }}"
      github-username: "${{ secrets.GH_USERNAME }}"
      github-token: "${{ secrets.GH_TOKEN }}"
```

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

| SECRET                            | REQUIRED | DESCRIPTION                                                |
| --------------------------------- | -------- | ---------------------------------------------------------- |
| GOOGLE_PROJECT_ID                 | true     | The id of the project which contains the secrets           |
| GOOGLE_SERVICE_ACCOUNT            | true     | The service account to use to fetch the secrets            |
| GOOGLE_WORKLOAD_IDENTITY_PROVIDER | true     | The workload identity provider to use for fetching secrets |

<!-- AUTO-DOC-SECRETS:END -->
