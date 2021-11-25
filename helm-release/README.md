# helm-release
This action will lint all charts, bump the version according to the `.bumpversion.cfg` file and create releases for all changed charts. To use this action you need to have a few things setup in the repository:

1. Add a `./github/lint-config.yaml` file with the following content and set `target-branch` to the default branch of your repository:
```yaml
# check https://github.com/helm/chart-testing/blob/main/pkg/config/test_config.yaml for possible configurations
target-branch: "main"
```

2. Add an empty branch `gh-pages` for the index.yaml to be hostet publically:
```
git checkout --orphan gh-pages
git rm --cached .
git commit -m "Initial commit" --allow-empty
git push --set-upstream origin gh-pages
```

3. Add a `.bumpversion.cfg` file in the root directory of your repository with the following content. Make sure to replace the `CHART_NAME` with the folder name to your chart and `CHART_VERSION` with the current version of your chart found in the `Chart.yaml` file. If you have multiple charts in the same repository just copy the second block multiple times, but be aware that all charts in the same repository need to have the same version:
```cfg
[bumpversion]
current_version = CHART_VERSION
commit = True
tag = False

[bumpversion:file:charts/CHART_NAME/Chart.yaml]
search = version: {current_version}
replace = version: {new_version}
```

4. Add the following steps to your workflow:
```yaml
...
steps:
  # check out current repository
  - uses: actions/checkout@v2
    with:
      # needed because the releaser scans for chart changes in multiple commits
      fetch-depth: 0
      # needed to push the bumped charts
      persist-credentials: false

  # check out ci-templates repository into ./ci-templates
  - uses: actions/checkout@v2
    with:
      repository: "bakdata/ci-templates"
      path: "ci-templates"
  
  # lint, bump version and release all changed charts
  - name: Release charts
      uses: ./ci-templates/helm-release
      with:
        githubToken: "${{ secrets.GH_TOKEN }}"
        githubUsername: "${{ secrets.GH_USERNAME }}"
        githubEmail: "${{ secrets.GH_EMAIL }}"
```

## Optional parameters
You can optionally set the `releaseType` to `major`, `minor` or `patch`. This can also be done via a workflow input:
```yaml
name: release

on:
  workflow_dispatch:
    inputs:
      releaseType:
        description: "The type of the release."
        default: "patch"
        required: false

jobs:
  release:
    runs-on: ubuntu-20.04
    steps:
      # check out current repository
      - uses: actions/checkout@v2
        with:
          # needed because the releaser scans for chart changes in multiple commits
          fetch-depth: 0
          # needed to push the bumped charts
          persist-credentials: false

      # check out ci-templates repository into ./ci-templates
      - uses: actions/checkout@v2
        with:
          repository: "bakdata/ci-templates"
          path: "ci-templates"
      
      # lint, bump version and release all changed charts
      - name: Release charts
          uses: ./ci-templates/helm-release
          with:
            githubToken: "${{ secrets.GH_TOKEN }}"
            githubUsername: "${{ secrets.GH_USERNAME }}"
            githubEmail: "${{ secrets.GH_EMAIL }}"
            releaseType: "${{ github.event.inputs.releaseType }}"
```
