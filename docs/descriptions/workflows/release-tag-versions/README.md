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